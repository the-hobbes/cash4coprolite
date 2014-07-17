# TODO(pheven): implement a simple datastore to keep track of a user account,
# the amount of time they've spent on the toilet, their pay, their location, etc...
# probably will want to break out the regular profile information from the other data
# that will be calculated. 

from google.appengine.ext import ndb
from google.appengine.api import users

class UserInformation(ndb.Model):
  """Models an individual user entry with user, address, salary."""
  user = ndb.UserProperty()
  
  wage_hourly = ndb.FloatProperty()
  wage_yearly = ndb.FloatProperty()

  address_street_1 = ndb.StringProperty()
  address_street_2 = ndb.StringProperty()
  address_city = ndb.StringProperty()
  address_zip = ndb.StringProperty()
  address_country = ndb.StringProperty()