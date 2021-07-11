import os
import re

import webapp2
import jinja2

import hashlib

import hmac

import random
import string

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
ID = 2000
SECRET = 'mysecret'
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s)) 

def check_secure_val(h):
    val = h.split("|")[0]
    if h == make_secure_val(val):
        return val

def make_salt():
    salty=''
    for x in range(5):
        salty+=random.choice(string.ascii_letters)
    return salty

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "%s,%s" % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Rot13(BaseHandler):
    def get(self):
        self.render('rot13-form.html')

    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')

        self.render('rot13-form.html', text = rot13)


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(BaseHandler):

    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            global ID 
            ID +=1
            user_id_hash = make_secure_val(str(ID))
            self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % user_id_hash)
            self.redirect('/welcome')

class Welcome(BaseHandler):
    def get(self):
        cookie_user_id = self.request.cookies.get('user_id')
        user_id = cookie_user_id.split('|')[0]
        if check_secure_val(cookie_user_id):
            self.render('welcome.html', username = user_id)
        else:
            self.redirect('/signup')

app = webapp2.WSGIApplication([('/rot13', Rot13),
                               ('/signup', Signup),
                               ('/welcome', Welcome)],
                              debug=True)
