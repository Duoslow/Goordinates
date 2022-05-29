import requests, re
from urllib.parse import unquote

def get_cordinate(url):
    """
    get latitude and longitude information from a Google Map URL.

    Parameters
    ----------
        url : str
            google map url
    Returns
    ----------
        lat : str
            latitude from url
        lng : str
            longitude from url
    
    """
    
    if '/maps/embed' in url:
        pattern = re.compile(r'!2d(-?\d+(?:\.\d+)?)!3d(-?\d+(?:\.\d+))')
        match = re.search(pattern, url)
        if match:
            lng = match.group(1)
            lat = match.group(2)
            return lat,lng
        else:
            return None,None

    elif '/maps/place' in url:
        pattern = re.compile(r'@(-?\d+\.\d+),(-?\d+\.\d+)')
        match = re.search(pattern, url)
        if match:
            lat = match.group(1)
            lng = match.group(2)
            return lat, lng
        else:
            return None, None
    
    elif 'goo.gl/maps/' in url:
        raw_url = requests.get(url).url
        raw_url = unquote(raw_url)              # YAVAŞ SÜREN KISIM
        
        if len(raw_url.split("@",1)) == 2:
            lat = raw_url.split("@",1)[1].split(",",2)[0]
            lng = raw_url.split("@",1)[1].split(",",2)[1]
            return lat, lng
        else:
            lat = raw_url.split("ll=",1)[1].split("&",1)[0].split(",",1)[0]
            lng = raw_url.split("ll=",1)[1].split("&",1)[0].split(",",1)[1]
            return lat, lng
    else:
        print("[Goordinates] This url is not supported.")
        return None, None
