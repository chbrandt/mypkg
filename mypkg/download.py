import requests

def download_file(url, filename=None):
    """
    Download file (silently)

    Usage:
        download_file_silent('http://web4host.net/5MB.zip', 'local_filename.zip')
    """
    if filename is None:
        filename = url.split('/')[-1]

    try:
        r = requests.get(url)
        with open(filename,'wb') as f:
            f.write(r.content)
    except Exception as err:
        # TODO: print to stderr
        print(err)
        return None
    return filename
