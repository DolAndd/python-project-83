import os
from urllib.parse import urlparse
import requests

import psycopg2
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)

from page_analyzer.url_repository import UrlRepository
from page_analyzer.validate_url import validate_url

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
repo = UrlRepository(conn)


@app.route("/")
def home_page():
    messages = get_flashed_messages(with_categories=True)
    return render_template('home.html', messages=messages)


@app.post('/urls')
def urls_post():
    url_data = request.form.get('url')
    if validate_url(url_data) is not True:
        flash('Некорректный URL', 'error')
        messages = get_flashed_messages(with_categories=True)
        return render_template("home.html", url=url_data, messages=messages)

    parsed_url = urlparse(url_data)
    new_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    if repo.find_name(new_url):
        url_id = repo.find_name(new_url)['id']
        flash('Страница уже существует', 'info')
        return redirect(url_for('urls_show', id=url_id), code=302)

    url_id = repo.save_url(new_url)
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('urls_show', id=url_id), code=302)


@app.route('/urls/<id>')
def urls_show(id):
    messages = get_flashed_messages(with_categories=True)
    url = repo.find_id(id)
    url_checks = repo.get_url_check(id)
    return render_template(
        'show.html',
        url=url,
        url_checks=url_checks,
        messages=messages
    )


@app.route('/urls')
def urls_index():
    messages = get_flashed_messages(with_categories=True)
    urls = repo.get_content()
    return render_template(
        'index.html',
        urls=urls,
        messages=messages
    )


@app.post('/urls/<id>/checks')
def url_check(id):
    url = repo.find_id(id)['name']
    try:
        result = requests.get(url)
        result.raise_for_status()
    except Exception:
        flash('Произошла ошибка при проверке', 'error')
        return redirect(url_for('urls_show', id=id), code=302)
    repo.save_url_check(id, result.status_code)
    flash('Страница успешно проверена', 'success')
    return redirect(url_for('urls_show', id=id), code=302)
