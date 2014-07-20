from google.appengine.ext import ndb


class Poop(ndb.Model):
  """Representation of a single poop. Can't believe I just typed that."""

  poop_length = ndb.FloatProperty() # in seconds
  poop_value = ndb.FloatProperty() # calculated
  poop_timestamp = ndb.DateTimeProperty(auto_now_add=True)
 

class UserInformation(ndb.Model):
  """Models an individual user entry with user, address, salary, poops, etc"""
  user = ndb.UserProperty()
  
  wage_hourly = ndb.FloatProperty()
  wage_yearly = ndb.FloatProperty()
  wage_per_minute = ndb.FloatProperty() # calculated and then stored for speed
  total_value = ndb.FloatProperty() # sum of all poops

  address_street_1 = ndb.StringProperty()
  address_street_2 = ndb.StringProperty()
  address_city = ndb.StringProperty()
  address_zip = ndb.StringProperty()
  address_country = ndb.StringProperty()
  # geolocation = ndb.GeoPt() # lat, lon

  poops = ndb.StructuredProperty(Poop, repeated=True) # store a set of poops
  # see this https://developers.google.com/appengine/docs/python/ndb/properties#structured
  # for an example of using the structured property
