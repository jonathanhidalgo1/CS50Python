from working import convert

def test_time_am_am():
    assert convert("5 AM to 5 AM") == "05:00 to 05:00"
    assert convert("9 AM to 9 AM") == "09:00 to 09:00"
    
    
def test_time_am_pm():
    assert convert("5 AM to 5 PM") == "05:00 to 17:00"
    assert convert("5 AM to 9 PM") == "05:00 to 21:00"
    
def test_time_pm_am():
    assert convert("5 PM to 5 AM") == "17:00 to 05:00"
    assert convert("11 PM to 5 AM") == "23:00 to 05:00"
    
def test_time_pm_pm():
    assert convert("5 PM to 5 PM") == "17:00 to 17:00"
    assert convert("12 PM to 8 PM") == "00:00 to 20:00"