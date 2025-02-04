from bs4 import BeautifulSoup


def get_check_url(url_text):
    soup = BeautifulSoup(url_text, 'html.parser')
    content = dict()
    h_1 = soup.find('h1')
    content['h1'] = h_1.string if h_1 else ''
    title = soup.find('title')
    content['title'] = title.string if title else ''
    contents = soup.find('meta', attrs={'name': 'description'})
    content['content'] = contents['content'] if contents else ''
    return content

