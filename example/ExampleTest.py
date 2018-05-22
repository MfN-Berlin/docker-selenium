"""A simple test class example."""
from dockerSelenium.Base import Base


class ExampleTest(Base):
    """
    A simple test class example.

    The test class should extend Base.py.
    Base.py provides:
    * loadURL
    * getElementById
    """

    def test1(self):
        """Test that Google can be loaded."""
        self.loadURL("http://www.google.com")
        element = self.getElementById("searchform")
        self.assertTrue(element, "Problem loading page.")
