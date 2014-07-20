# TODO(pheven): name this file something better than login. You need to be able to log in to use it,
# but really it renders the profile page

import webapp2
import re

from google.appengine.api import users
from google.appengine.ext import ndb
from handlers.base_handler import BaseHandler
from handlers.Datastore import UserInformation

class LoginHandler(BaseHandler):
  USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
  # TODO(pheven): compile proper regular expressions to match address, city,
  # zip code, and wages. 

  def get(self):
    user = users.get_current_user()

    if user:
      self.render('profile.html', user=user.nickname())
    else:
      self.redirect(users.create_login_url(self.request.uri))

  def post(self):
    user = users.get_current_user()
    username = str(user.nickname)

    # TODO(pheven): server side data validation before storage
    has_error, params = self.validate_input(self.request)

    if has_error:
      self.render('profile.html', **params)
    else:
      wage_hourly = float(self.request.get('form_hourly_wage'))
      wage_yearly = float(self.request.get('form_yearly_wage'))
      address_street_1 = self.request.get('input_address_1')
      address_street_2 = self.request.get('input_address_2')
      address_city = self.request.get('input_city')
      address_zip = self.request.get('input_zip')
      address_country = self.request.get('select_country')

      user_info_entry = UserInformation(parent = ndb.Key('UserInfo', username),
                                        wage_hourly = wage_hourly,
                                        wage_yearly = wage_yearly,
                                        address_street_1 = address_street_1,
                                        address_street_2 = address_street_2,
                                        address_city = address_city,
                                        address_zip = address_zip,
                                        address_country = address_country)
      user_info_entry.put()
      self.redirect("/profile")

  def validate_input(self, request):
    wage_hourly = self.request.get('form_hourly_wage')
    wage_yearly = self.request.get('form_yearly_wage')
    address_street_1 = self.request.get('input_address_1')
    address_street_2 = self.request.get('input_address_2')
    address_city = self.request.get('input_city')
    address_zip = self.request.get('input_zip')
    address_country = self.request.get('select_country')

    params = {}

    if not self.valid_wage_hourly(wage_hourly):
      params['error_wage_hourly'] = "That's not a valid hourly wage."
      return True, params
    if not self.valid_wage_yearly(wage_yearly):
      params['error_wage_hourly'] = "That's not a valid yearly wage."
      return True, params
    if not self.valid_address_street_1(address_street_1):
      params['error_wage_hourly'] = "That's not a valid address."
      return True, params
    if not self.valid_address_street_2(address_street_2):
      params['error_wage_hourly'] = "That's not a valid address."
      return True, params
    if not self.valid_address_city(address_city):
      params['error_wage_hourly'] = "That's not a valid city."
      return True, params
    if not self.valid_address_zip(address_zip):
      params['error_wage_hourly'] = "That's not a valid zip code."
      return True, params
    if not self.valid_address_country(address_country):
      params['error_wage_hourly'] = "That's not a valid country."
      return True, params

  def valid_wage_hourly(self, wage_hourly):
    return username and self.USER_RE.match(username) # TODO(pheven): see RE class variable above
