""" Functions commonly used gathered here for reusability.
"""
import sys
sys.path.insert(0, 'libs')
from geopy import *


def calculateWagePerMinute(wage_hourly=None, wage_yearly=None):
  """calculate the wage per minute."""
  MINUTES_IN_HOUR = 60
  MINUTES_IN_YEAR = 525949

  if wage_yearly and wage_hourly:
    raise Exception('Both yearly and hourly wage defined!')
  if wage_hourly:
    wage_per_minute = wage_hourly / MINUTES_IN_HOUR
  elif wage_yearly:
    wage_per_minute = wage_yearly / MINUTES_IN_YEAR

  return wage_per_minute

def calculateGeoLocation(address_street_1, address_street_2, address_city, 
                         address_zip, address_country):
  """Calculate the geographic location in a geopoint."""
  g = geocoders.GoogleV3()
  full_address = (address_street_1 + ' ' 
                  + address_street_2 + ' ' 
                  + address_city + ' ' 
                  + address_zip + ' ' 
                  + address_country)
  place, (lat, lon) = g.geocode(full_address)
  geolocation = ndb.GeoPt(lat, lon)

  return geolocation