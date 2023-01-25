from plates import is_valid

def test_twoletters():
    assert is_valid("HELLO") == True
    
def test_6characters():
    assert is_valid("HELLOOOOO") == False
    
def test_numbers_middle():
    assert is_valid("HEL2LO") == False

def test_numbers_end():
    assert is_valid("CS50") == True    
    
def test_special_characters():
    assert is_valid("HELLO, WOLRD") == False

    
    