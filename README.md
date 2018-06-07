Builds a Docker Container for testing web applications with Selenium.

There are several Selenium-ready Docker containers available. This one is optimized for small image size (based on Alpine Linux), comes with a headless Firefox and Python bindings. 

To **build the image** from the Dockerfile, call ```./build.sh```.

## Writing tests
Tests are written in Python and should expand ```dockerSelenium.Base``` (see ```example/ExampleTest.py```).

Put the tests in the project that needs to be tested. When you start the container, make sure the directory containing the tests is mounted as a volume called "test".

Then **run the tests**:
```
cd docker-selenium
./run.sh docker-container-to-test
```

## Debug mode
If you need to debug tests, you can run the container in debug mode by calling:
```
cd docker-selenium
./run.sh docker-container-to-test debug
```
The container will not be removed after it the tests have run. You can then connect to it using
```
docker exec -ti selenium /bin/bash
```
and edit the test runner script, which is in ```/start_test_runner.sh```.

## Documentation
* Selenium with Python: http://selenium-python.readthedocs.io/
* Green (test runner): https://github.com/CleanCut/green
* Coverage: http://coverage.readthedocs.io/en/coverage-4.5.1/