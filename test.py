from unittest import TestCase
from app import app, db
from user import views
from flask_login import current_user, login_user
from models import User
import unittest
from user import forms
from flask import Flask


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.client = self.app.test_client()
        db.create_all()
        User.register('Tester', 'Tester123*')

    def tearDown(self):
        db.drop_all()
        self.app_ctx.pop()

    def test_login(self):
        r = self.client.get('/login')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('<h1>login</h1>' in r.get_data(as_text=True))
        r = self.client.post('/login',
                             data={'username': 'Test@user.com', 'password': 'Tester123*'},
                             follow_redirects=True)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(('<h1>home page</h1>' in r.get_data(as_text=True)))


class FlaskTestCase(unittest.TestCase):

    # If user is removed from database, Test will fail
    def test_new_user(self):
        user = User(username='Tester',
                    email='test@user.com',
                    password='Tester123*',
                    first_name='Test',
                    last_name='Test')
        assert user.email == 'test@user.com'
        assert user.password != 'Tester123*'

    '''def test_user_registration(self):
        with self.client:
            response = self.register.post(
                '/register', data=dict(
                    username="Tester",
                    email="test@user.com",
                    password="Tester123*",
                    confirm_password='Tester123*',
                    first_name="Test",
                    last_name="Test"), follow_redirects=True
            )
            self.assertIn('Registered', response.data)
            self.assertTrue(current_user.name == "test@user.com")
            self.assertTrue(current_user.is_active())'''

    '''def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('login' in response.data)

    def test_valid_registration(self):
        response = self.register('test@user.com', 'Tester123*')
        self.assertEqual(response.status_code, 200)
        self.assertIn('You are logged in')'''

    '''# Ensures that Flask was set up correctly
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/base', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the login page loads
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('login' in response.data)

    # Ensures login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='Tester', password='Tester123*'), follow_redirects=True)
        self.assertIn('Logged in' in response.data)

    # Ensures login behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='Tester', password='Tester123*'), follow_redirects=True)
        self.assertIn('Email or password is incorrect' in response.data)

    # Ensures logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login',
                    data=dict(username='Tester', password='Tester123*'),
                    follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn('/home' in response.data)

    def test_register_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertTrue('register' in response.data)

    def test_correct_register(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(username='Tester', password='Tester123*'), follow_redirects=True)
        self.assertIn('Registered' in response.data)

    def test_incorrect_register(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(username='Tester', password='Tester123*'), follow_redirects=True)
        self.assertIn('validation errors' in response.data)'''


if __name__ == '__main__':
    unittest.main()
