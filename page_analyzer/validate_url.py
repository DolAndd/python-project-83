import validators


def validate_url(url):
    if len(url) < 225 and validators.url(url) is True:
        return True
