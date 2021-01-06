import string
import unittest
import random

from api import app, init_db, get_db


def get_client():

    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            init_db()
        return client


class TestApp(unittest.TestCase):

    @unittest.skip("This is only used to generate data in SQLite DB db/database.db")
    def test_load_data(self):

        db = get_db()

        for i in range(1, 10):
            id = 100_000 + i
            user_id = random.randint(100_000, 9_999_999)
            amount = random.randint(1, 999_999_999_999)
            iban = 'XX' + str(random.randint(1000_000, 1000_000_000))
            reference = ''.join(random.choice(string.ascii_uppercase) for i in range(25))
            sql = "INSERT OR IGNORE INTO payments(id, user_id, iban, amount, reference) VALUES({id}, {user_id}, '{iban}', {amount}, '{reference}')".format(
                id=id, user_id=user_id, amount=amount, iban=iban, reference=reference
            )
            print(sql)
            db.execute(sql)
            db.commit()

        db.close()

    def test_index(self):

        print('Testing requesting index path: /')

        client = get_client()
        response = client.get('/')
        self.assertEquals(b'Welcome to Payment REST API from <b>Bank of Hong Kong Luna</b>', response.data)