import os
import psycopg2
import validators
from dotenv import load_dotenv
from flask import (
    get_flashed_messages,
    flash,
    Flask,
    redirect,
    render_template,
    request,
    url_for
)
from page_analyzer.url_repository import UrlRepository

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
repo = UrlRepository(conn)


@app.route("/")
def home_page():
    messages = get_flashed_messages(with_categories=True)
    return render_template('home.html', messages=messages)


@app.post('/')
def url_post():
    url_data = request.form.to_dict()
    if validators.url(url_data['url']) is True:
        repo.save(url_data)
        flash('Страница успешно добавлена', 'success')
        return redirect(url_for('home_page'), code=302)
    else:
        return render_template(url_for('home_page'))


@app.route('/urls/<id>')
def users_show(id):
    url = repo.find(id)
    return render_template(
        'show.html',
        url=url,
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