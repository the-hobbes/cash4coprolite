# TODO(pheven): name this file something better than login. You need to be able to log in to use it,
# but really it renders the profile page

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

  def post(self):
    pass
    # TODO(pheven): implement the post handler, which then passes validated data to the datastore