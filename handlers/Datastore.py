<<<<<<< HEAD
# TODO(pheven): implement a simple datastore to keep track of a user account,
# the amount of time they've spent on the toilet, their pay, their location, etc
# probably will want to break out the regular profile information from the other
# data that will be calculated. 
=======
import sys
sys.path.insert(0, 'libs')
>>>>>>> e060dbf8c99e52cae07e4e7a6c5da50309dee6a8

from geopy import *
from google.appengine.ext import ndb


class Poop(ndb.Model):
  """Representation of a single poop. Can't believe I just typed that."""

  poop_length = ndb.FloatProperty() # in seconds
  poop_value = ndb.FloatProperty() # calculated
  poop_timestamp = ndb.DateTimeProperty(auto_now_add=True)

  def put(self):
    """Override default put method to perform calculation automatically."""
    pass
 


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
<<<<<<< HEAD

  geolocation = ndb.GeoPt() # lat,lon calc'ed from address

  total_value = ndb.FloatProperty() # sum of all poops


class Poop(ndb.Model):
  """Represents a single poop. That was tough to type."""
  poop_length = ndb.FloatProperty()
  
=======
  # geolocation = ndb.GeoPt() # lat, lon

  poops = ndb.StructuredProperty(Poop, repeated=True) # store a set of poops
  # see this https://developers.google.com/appengine/docs/python/ndb/properties#structured
  # for an example of using the structured property

  def put(self):
    """Override default put method to perform calculation automatically."""
    # TODO: figure out if this overriding is the best way to do this, or if these
    # values should be calculated in the post method for the handler and then passed into the datastore

    # TODO: also, figure out the right data path for the geolocation point. I am clearly misusing
    # its concept. 
    MINUTES_IN_HOUR = 60
    MINUTES_IN_YEAR = 525949

    if self.wage_yearly and self.wage_hourly:
      raise Exception('Both yearly and hourly wage defined!')
    if self.wage_hourly:
      self.wage_per_minute = self.wage_hourly / MINUTES_IN_HOUR
    elif self.wage_yearly:
      self.wage_per_minute = self.wage_yearly / MINUTES_IN_YEAR

    g = geocoders.GoogleV3()
    full_address = (self.address_street_1 + ' ' 
                    + self.address_street_2 + ' ' 
                    + self.address_city + ' ' 
                    + self.address_zip + ' ' 
                    + self.address_country)
    place, (lat, lon) = g.geocode(full_address)
    self.geolocation = ndb.GeoPt(lat, lon)

    return super(UserInformation, self).put()
>>>>>>> e060dbf8c99e52cae07e4e7a6c5da50309dee6a8
