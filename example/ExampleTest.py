"""A simple test class example."""
from dockerSelenium.Base import Base


class ExampleTest(Base):
    """
    A simple test class example.

    The test class should extend Base.py.
    Base.py provides:
    * loadURL
    * getElementById
    * getUrlStatusCode
    """

    def test1(self):
        """Test that Google can be loaded."""
        status = self.getUrlStatusCode("http://www.google.com")
        self.assertEquals(200, status, "Problem loading page.")

    def test2(self):
        """Test that Google page has a search input field."""
        self.loadURL("http://www.google.com")
        element = self.getElementById("searchform")
        self.assertTrue(element, "Problem loading page.")
