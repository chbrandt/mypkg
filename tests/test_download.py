import pytest
import os

from mypkg import download

_testdata = {
    'success': ('https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg', 'The_Earth_seen_from_Apollo_17.jpg'),
    'fail': ('http://web4host.net/improbable_file_gjh9825y.what', '')
}

def test_download_success():
    given_in, expected_out = _testdata['success']
    
    out = download.download_file(given_in)

    assert out == expected_out
    assert os.path.isfile(out)

    
def test_download_success_rename():
    given_in = _testdata['success'][0]
    expected_out = 'earth.jpg'
    
    out = download.download_file(given_in, expected_out)
    
    assert out == expected_out
    assert os.path.isfile(out)

