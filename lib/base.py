# The BasePage object will act as a parent object for all the page object that we
# will create in our test suite.
# The base page provides common code that the page object can use.

from abc import abstractmethod
class BasePage(object):
    ''' All page objects inherit from this '''

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
         return

    ''' Regions define functionality available through
        all page objects '''
    @property
    def topnavigation(self):
        from topnavigation import TopNavigationRegion
        return TopNavigationRegion(self.driver)

class InvalidPageException(Exception):
    ''' Throw this exception when you don't find the correct page '''
    pass
