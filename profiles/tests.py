import unittest

class transaction:
    def __init__(self, account, tid, amount, date, memo):
        self.account = account
        self.tid = tid
        self.amount = amount
        self.date = date
        self.memo = memo

# SHUaccount = transaction.account("gacardillo")
# SHUtid = transaction.id("101100567")
# SHUamount = transaction.amount("100")
# SHUdate = transaction.date("12/04/2016")
# SHUmemo = transaction.memo("Transaction complete")

t = transaction("gacardillo", 101100567, 100, "12/04/2016", "Transaction complete")

class Test_account(unittest.TestCase):
    def test_account(self):
        try:
            self.assertEqual((t.account), "gacardillo", "equal")
        except AssertionError:
            print 'not equal'
    def test_account_false(self):
        try:
            self.assertFalse(t.account != "santana")
        except AssertionError:
            print 'invaild user'

class Test_ID(unittest.TestCase):
    def test_tid(self):
        try:
            self.assertEqual((t.tid), "101100567", "equal")
        except AssertionError:
            print 'not equal'
    def test_tid_false(self):
        try:
            self.assertFalse(t.tid != "1545638790")
        except AssertionError:
            print 'invaild ID'
class Test_amount(unittest.TestCase):
    def test_amount(self):
        try:
            self.assertEqual((t.amount), "100", "equal")
        except AssertionError:
            print 'not equal'
    def test_amount_false(self):
        try:
            self.assertFalse(t.amount != "500")
        except AssertionError:
            print 'invaild amount'
class Test_date(unittest.TestCase):
    def test_date(self):
        try:
            self.assertEqual((t.date), "12/04/2016", "equal")
        except AssertionError:
            print 'invalid date'
    def test_date_false(self):
        try:
            self.assertFalse(t.date != "11/30/2016")
        except AssertionError:
            print 'Date not valid'
class Test_memo(unittest.TestCase):
    def test_memo(self):
        try:
            self.assertEqual((t.memo), "Transaction complete", "equal")
        except AssertionError:
            print 'Not complete'
    def test_memo_false(self):
        try:
            self.assertFalse(t.date != "11/30/2016")
        except AssertionError:
            print 'Transaction not complete'

if __name__ == '__main__':
    unittest.main()


