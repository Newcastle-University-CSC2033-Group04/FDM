from unittest import TestCase
from app import app, db
from user import views
from flask_login import current_user, login_user
from models import User
import unittest
from user.forms import RegisterForm, LoginForm
from flask import Flask
import os
import tempfile


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

    # Ensures that Flask was set up correctly
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
        self.assertIn('validation errors' in response.data)


if __name__ == '__main__':
    unittest.main()
