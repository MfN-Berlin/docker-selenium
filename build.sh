#! /bin/bash

# Create a docker container for testing with Selenium
#
# @author Alvaro Ortiz for Museum fuer Naturkunde, 2017
# contact: alvaro.OrtizTroncoso@mfn-berlin.de

echo "Please choose:"
echo "1. Build new Selenium image"
echo "13: Remove Selenium image and container"
echo "0. Usage"
read -p "? " opt

# Read configuration options
source config.ini

usage() {
    # Show usage information
    echo "See README."
}

###########################################
#
# Build the Selenium image.
#
###########################################
build() {
    docker build -f Dockerfile -t $SLNM_CONTAINER .
    docker images 
}

#############################################
#
# Remove the Selenium image and container.
#
#############################################
remove() {
    docker stop $SLNM_CONTAINER
    docker rm $SLNM_CONTAINER
    docker rmi $SLNM_CONTAINER
}

#############################################
#
# Run all tests.
#
#############################################
runtests() {
    docker exec -ti $SLNM_CONTAINER /bin/bash ./runtests.sh
}

case $opt in 
    0)
        usage
        ;;
    1)
        build
        ;;
    13)
        remove
        ;;
    *)
        echo "Unknown option"
	usage
        ;;
esac
