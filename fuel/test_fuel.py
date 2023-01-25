from fuel import convert

def test_half_gauge():
    assert convert("1/2") == "50%"
    
def test_empty():
    assert convert("0/1") == "E"
    
def test_full():
    assert convert("1/1") == "F"
    
def test_quarter():
    assert convert("3/4") == "75%"