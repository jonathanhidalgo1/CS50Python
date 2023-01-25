from jar import Jar

def test_init():
    pass

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposite(1)
    assert str(jar) == "🍪"
    jar.deposite(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    
def test_deposite():
    jar = Jar()
    
    assert jar.deposite(1) == "🍪"
    assert jar.deposite(11) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    
def test_withdraw():
    jar = Jar()
    jar.deposite(5)
    assert jar.withdraw(5) == ""
    jar.deposite(4)
    assert jar.withdraw(3) == "🍪"