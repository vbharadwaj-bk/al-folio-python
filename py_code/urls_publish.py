import yaml 

def make_functions():
    config = None
    with open('content/config.yml', "rb") as stream:
        config = yaml.safe_load(stream)

    if config["baseurl"] is not None: 
        BASEURL = "/" + config["baseurl"] + "/"
    else:
        BASEURL = "/"

    ABSOLUTE_URL = config["url"] + BASEURL 

    def relative_url(url, BASEURL=BASEURL):
        return BASEURL + url 

    # For development, absolute and relative urls are the same thing
    def absolute_url(url, ABSOLUTE_URL=ABSOLUTE_URL):
        return ABSOLUTE_URL + url
    
    return relative_url, absolute_url 