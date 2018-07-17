"""A base class for Selenium Tests using Python bindings."""
import unittest
import urllib.request
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base(unittest.TestCase):
    """A base class for Selenium Tests using Python bindings."""

    MAX_WAIT = 60
    """Seconds before timeout"""

    def setUp(self):
        """
        Set the test up.

        Each test forks its own process, so needs its own driver.
        Otherwise they get in the way of each other and cause random errors.
        Todo: Some stuff can go in setUpClass (but not the driver)
        """
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()

        self.driver = webdriver.Firefox()

    def loadURL(self, URL):
        """
        Load a web page.

        Following method calls (e.g. getElementById) will be applied to the page loaded.
        Keyword arguments:
        URL -- URL of the web page to be loaded.
        """
        self.driver.get(URL)

    def getElementById(self, elementId):
        """
        Get a HTML element.

        This method is set to a MAX_WAIT seconds timeout.
        Keyword arguments:
        elementId -- ID of the HTML element sought
        return -- webElement
        """
        element = WebDriverWait(self.driver, Base.MAX_WAIT).until(EC.presence_of_element_located((By.ID, elementId)))
        
        return element

    def getElementByName(self, elementId):
        """
        Get a HTML element.

        This method is set to a MAX_WAIT seconds timeout.
        Keyword arguments:
        elementId -- ID of the HTML element sought
        return -- webElement
        """
        element = WebDriverWait(self.driver, Base.MAX_WAIT).until(EC.presence_of_element_located((By.NAME, elementId)))
        return element

    def getElementByXPath(self, path):
        """
        Get a HTML/XML element.

        This method is set to a MAX_WAIT seconds timeout.
        Keyword arguments:
        path -- XPATH to the element sought
        return -- webElement
        """
        element = WebDriverWait(self.driver, Base.MAX_WAIT).until(EC.presence_of_element_located((By.XPATH, path)))
        return element

    def getInnerHTMLById(self, elementId):
        """
        Get the HTML contained in an element.

        Keyword arguments:
        elementId -- ID of the HTML element sought
        return -- string HTML
        """
        element = self.getElementById(elementId)
        return element.get_attribute("innerHTML")

    def getUrlStatusCode(self, URL):
        """
        Get the HTTP response code for this URL.

        Keyword arguments:
        URL -- URL of the web page to be loaded.
        return -- int http code
        """
        try:
            with urllib.request.urlopen(URL) as r:
                return r.getcode()
        except urllib.error.HTTPError as e:
            return e.code

    def tearDown(self):
        """
        Teardown the test.

        Will be executed after each test. Close the driver and the display.
        """
        self.driver.close()
        self.driver.quit()
        self.display.stop()
