"""A base class for Selenium Tests using Python bindings."""
import unittest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base(unittest.TestCase):
    """A base class for Selenium Tests using Python bindings."""

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
        elementId -- URL of the web page to be loaded.
        """
        self.driver.get(URL)

    def getElementById(self, elementId):
        """
        Get a HTML element.

        This method is set to a 30 seconds timeout.
        Keyword arguments:
        elementId -- ID of the HTML element sought
        return --
        """
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, elementId)))
        return element

    def tearDown(self):
        """
        Teardown the test.

        Will be executed after each test. Close the driver and the display.
        """
        self.driver.close()
        self.driver.quit()
        self.display.stop()
