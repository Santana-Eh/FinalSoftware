import unittest
from Unittest_userDB import user_db
class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Test_login (unittest.TestCase):
    def test_username(self):
        try:
            self.assertTrue("gacardillo" in user_db.keys())
        except AssertionError:
            print 'Not vaild username'
            return
        try:
            self.assertTrue("CS604" == user_db["gacardillo"])
        except AssertionError:
            print 'Not vaild passwored'
class Test_login_failed(unittest.TestCase):
    def test_username_failed(self):
        try:
            self.assertFalse("gacardillo" in user_db.keys())
        except AssertionError:
            print 'username active'
        try:
            self.assertFalse("CS604" == user_db["gacardillo"])
        except AssertionError:
            print 'username active'

if __name__ == '__main__':
    unittest.main()

