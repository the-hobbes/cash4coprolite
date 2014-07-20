from handlers.base_handler import BaseHandler
from handlers.Datastore import *


class DummyData():
  """Create a set of fake user information."""
  def __init__(self):
    wage_hourly = 18.0
    wage_yearly = 60000.0
    address_street_1 = '91 South Meadow Drive'
    address_street_2 = ''
    address_city = 'Burlington'
    address_zip = '94040'
    address_country = 'United States of America'
    
    poop_length_1 = 10.0
    poop_length_2 = 15.0
    poop_length_3 = 120.0 

class TestDatastoreWrite(BaseHandler):
  """Test writes to the datastore."""
  def get(self):
    self.write('Got to the datastore write handler. Populating data.'
    d = DummyData()
    test_user = users.get_current_user()
    dummy_write  = UserInformation(user = test_user,
                                   wage_hourly = d.wage_hourly,
                                   wage_yearly = d.wage_yearly,
                                   address_street_1 = d.address_street_1,
                                   address_street_2 = d.address_street_2,
                                   address_city = d.address_city,
                                   address_country = d.address_country
                                   poops = [Poop(poop_length = d.poop_length_1,
                                                 ),
                                            Poop(poop_length = d.poop_length_2,
                                                ),
                                            Poop(poop_length = d.poop_length_3,
                                                )])
    try:
      dummy_write.put()
    except Exception as e:
      logging.error('Failed write. Exception: %s' %e)
      return 'Failing'

    logging.info('Write succeeded')
    return 'Passing'
 

class TestDatastoreRead(BaseHandler):
  pass

# TODO(pheven): it would be better to test each calculation separately here.


class TestingHandler(BaseHandler):
  """Root handler for tests."""
  def get(self):
    self.render('testing_index.html')

  def post(self):
    test_choice = self.request.get('test_choice')
    if test_choice == 'datastore_test':
      datastore_test = # TODO initialize the testing classes here, based on what the user clicks
