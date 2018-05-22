Builds a Docker Container for testing web applications with Selenium.

There are several Selenium-ready Docker containers available. This one is optimized for small image size (based on Alpine Linux), comes with a headless Firefox and Python bindings. 

To **build the image** from the Dockerfile, call ```./build.sh```.

## Writing tests
Tests are written in Python. See ```example/ExampleTest.py```. Your tests should expand ```dockerSelenium.Base```.

Put the tests in the repository of the project that needs to be tested, then start a container and **run the tests**: call ```./run.sh full-path-to-the-test-directory```.

## Documentation
* Selenium with Python: http://selenium-python.readthedocs.io/
* Green (test runner): https://github.com/CleanCut/green
* Coverage: http://coverage.readthedocs.io/en/coverage-4.5.1/