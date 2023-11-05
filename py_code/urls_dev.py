def relative_url(url):
    return '/' + url

# For development, absolute and relative urls are the same thing
def absolute_url(url):
    return relative_url(url)

