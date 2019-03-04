FROM python:3.7-alpine

LABEL Description="This image is used to run Selenium tests" Vendor="Museum für Naturkunde Berlin"
WORKDIR /usr/src/app

######################################
#
# Install utilities
#
######################################
RUN set -x && apk add --no-cache \
  bash nano curl supervisor

######################################
#
# Install Java to run Selenium server
#
######################################
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
# corresponds to alpine version
ENV JAVA_ALPINE_VERSION 8.191.12-r0

RUN set -x && apk add --no-cache \
  bash nano curl \
  supervisor \
  openjdk8-jre="$JAVA_ALPINE_VERSION"

######################################
#
# Install Firefox
#
######################################
RUN set -x && apk add --no-cache \
  dbus-x11 ttf-freefont firefox-esr xvfb

######################################
#
# Download Selenium server
#
######################################
ENV Selenium_DOWNLOAD_URL="http://selenium-release.storage.googleapis.com/3.0/selenium-server-standalone-3.0.1.jar"
RUN curl -fSL $Selenium_DOWNLOAD_URL -o selenium-server-standalone.jar

############################################
#
# Download Firefox driver (geckodriver)
#
############################################
ENV geckodriver_DOWNLOAD_URL="https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz"
RUN curl -fSL $geckodriver_DOWNLOAD_URL -o geckodriver.tar.gz \
	&& tar -xf geckodriver.tar.gz -C . \
	&& mv geckodriver /usr/bin \
	&& chmod a+x /usr/bin/geckodriver \
	&& rm geckodriver.tar.gz

######################################
#
# Install Python packages and test runner script
# from requirements.txt
#
######################################
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY start_test_runner.sh ./
RUN chmod +x ./start_test_runner.sh

######################################
#
# Copy base Python class for tests.
# See issue: https://github.com/moby/moby/issues/15858
#
######################################
RUN mkdir ./dockerSelenium
COPY dockerSelenium ./dockerSelenium

######################################
#
# Link test directory from /usr/src/app/test
#
######################################
RUN ln -s /usr/src/app/test /test

#######################
#
# Start
#
#######################
COPY version.py ./
# Starting processes
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# run supervisor daemon to start apps
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]