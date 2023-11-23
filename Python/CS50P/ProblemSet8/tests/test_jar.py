import unittest
from jar import Jar

class TestJar(unittest.TestCase):
    def test_init(self):
        pass
    def test_str(self):
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
        jar.withdraw(8)
        assert str(jar) == "🍪🍪🍪🍪"
    def test_deposit():
        pass
    def test_withdraw():
        pass


if __name__ == "__main__":
    unittest.main()
