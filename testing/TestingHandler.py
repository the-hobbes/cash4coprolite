import logging

from handlers.Datastore import *
from handlers.base_handler import BaseHandler
from google.appengine.api import users


class DummyData():
  """Create a set of fake user information."""
  def __init__(self):
    self.wage_hourly = 18.0
    self.wage_yearly = 60000.0
    self.address_street_1 = '91 South Meadow Drive'
    self.address_street_2 = ''
    self.address_city = 'Burlington'
    self.address_zip = '94040'
    self.address_country = 'United States of America'
    
    self.poop_length_1 = 0.0
    self.poop_length_2 = 15.0
    self.poop_length_3 = 120000.0 
    self.poop_length_4 = -1.1

class TestDatastoreWrite():
  """Test writes to the datastore."""
  def runTest(self, user_object):
    ndb.delete(ndb.Query(keys_only=True))
    d = DummyData()
    test_user = user_object
    dummy_write  = UserInformation(user = test_user,
                                   wage_hourly = d.wage_hourly,
                                   wage_yearly = d.wage_yearly,
                                   address_street_1 = d.address_street_1,
                                   address_street_2 = d.address_street_2,
                                   address_city = d.address_city,
                                   address_country = d.address_country,
                                   poops = [Poop(poop_length = d.poop_length_1,
                                                 ),
                                            Poop(poop_length = d.poop_length_2,
                                                ),
                                            Poop(poop_length = d.poop_length_3,
                                                ),
                                            Poop(poop_length = d.poop_length_4,
                                                )])
    try:
      dummy_write.put()
    except Exception as e:
      logging.error('Failed write. Exception: %s' %e)
      return False

    logging.info('Write succeeded')
    return True
 

class TestDatastoreRead(BaseHandler):
  pass

# TODO(pheven): it would be better to test each calculation separately here.


class TestingHandler(BaseHandler):
  """Root handler for tests."""
  def get(self):
    self.render('testing_index.html')

  def post(self):
    test_choices = self.request.get_all('test_choice')
    user_object = users.get_current_user()

    if 'test_datastore' in test_choices:
      logging.info('Datastore test chosen.')
      datastore_write_success = TestDatastoreWrite().runTest(user_object)
      assert datastore_write_success is True
    if 'test_something' in test_choices:
      logging.info('Test test chosen. That\'s not confusing at all.')
