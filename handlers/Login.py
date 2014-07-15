import webapp2

from google.appengine.api import users
from handlers.base_handler import BaseHandler

class LoginHandler(BaseHandler):
  def get(self):
    user = users.get_current_user()

    if user:
      self.render('profile.html', user=user.nickname())
    else:
      self.redirect(users.create_login_url(self.request.uri))