from twttr import shorten

def test_lowletter():
    assert shorten("teste") == "tst"
    
def test_upperletter():
    assert shorten("BOLA") == "BL"

