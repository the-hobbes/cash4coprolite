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
    # clear the datastore before each write
    ndb.delete_multi(ndb.Query(default_options=ndb.QueryOptions(
                                                     keys_only=True)))
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
      logging.error('Write FAILING. Exception: %s' %e)
      return 'failing'

    logging.info('Write PASSING')
    return 'passing'
 

class TestDatastoreCalculations():
  # TODO(pheven): we want to test the acutal logic that performs these calculations,
  # so we need to write that and then import it to be used here.
  def __init__(self):
    pass
  def testDatastoreCalculateWagePerMinute(self):
    pass
  def testDatastoreCalculateTotalValue(self):
    pass

  def testDatastoreCalculateGeolocation(self):
    pass

  def testDatastoreCalculatePoopValue(self):
    pass


class TestingHandler(BaseHandler):
  """Root handler for tests."""
  def get(self):
    self.render('testing_index.html', test_results=None)

  def post(self):
    test_choices = self.request.get_all('test_choice')
    test_results = {}
    user_object = users.get_current_user()

    # write test(s)
    if 'test_datastore_write' in test_choices:
      logging.info('Datastore write test chosen.')
      result = TestDatastoreWrite().runTest(user_object)
      test_results['result_datastore_write'] = result

    # calculation test(s)
    if 'test_datastore_calculate_wage_per_minute' in test_choices:
      logging.info('Datastore wage per minute calculation chosen')
      result = TestDatastoreCalculations().testDatastoreCalculateWagePerMinute()
      test_results['result_datastore_calculate_wage_per_minute'] = result

    if 'test_datastore_calculate_total_value' in test_choices:
      logging.info('Datastore total value calculation chosen')
      result = TestDatastoreCalculations().testDatastoreCalculateTotalValue()
      test_results['result_datastore_calculate_total_value'] = result

    if 'test_datastore_calculate_geolocation' in test_choices:
      logging.info('Datastore calculate geolocation chosen')
      result = TestDatastoreCalculations().testDatastoreCalculateGeolocation()
      test_results['result_datastore_calculate_geolocation'] = result

    if 'test_datastore_calculate_poop_value' in test_choices:
      logging.info('Datastore calculate poop value chosen')
      result = TestDatastoreCalculations().testDatastoreCalculatePoopValue()
      test_results['result_datastore_calculate_poop_value'] = result

    # fake test(s)
    if 'test_fake' in test_choices:
      logging.info('Fake test chosen. That\'s not confusing at all.')
      test_results['result_fake'] = 'passing'

    self.render('testing_index.html', test_results=test_results)
