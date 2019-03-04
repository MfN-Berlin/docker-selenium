#! /bin/bash

# Run a docker container for testing with Selenium.
#
# Create the container first, using build.sh
# Pass the full path of the directory where the tests are on the host as parameter.
# Example:
#   ./run.sh /home/my-name/workspace/my-project/tests/
#
# The test runner expects to find a script called load_test_data.sh in the directory where the tests are.
# This script will be called before the tests are executed.
#
# The test runner will print test success and coverage info.
#
# Debug mode:
#   ./run.sh /home/my-name/workspace/my-project/tests/ debug
# If you add the word debug as last parameter, then the container will not be stopped,
# so you can connect to it doing:
#   docker exec -ti selenium /bin/bash
#
# @author Alvaro Ortiz for Museum fuer Naturkunde Berlin, 2017
# contact: alvaro.OrtizTroncoso@mfn-berlin.de

# Read configuration options
source ./config.ini

#############################################
#
# Start the Selenium container.
#
#############################################
start() {
    docker rm selenium
    docker run \
       --restart no \
       --name selenium \
       --volumes-from ikon-smw \
       -d \
       $SLNM_CONTAINER
    echo "You can now run tests."
    docker ps
}

#############################################
#
# Run all tests.
#
#############################################
runtests() {
    docker exec -ti selenium /bin/bash ./start_test_runner.sh
}

#############################################
#
# Stop and remove the container
# after the test run is completed
#
#############################################
stop() {
    docker stop selenium
    docker rm selenium
}

PATH_ON_HOST=$1
if [ $2 ];
  then IS_DEBUG=$2;
  else IS_DEBUG="no"
fi

start
runtests
if [ $IS_DEBUG == "debug" ]; then
  echo "Debug mode. Container will not be stopped."
else
  stop
fi
