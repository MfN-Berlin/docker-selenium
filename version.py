"""Print version of software installed."""
import sys
import subprocess

linuxVersion = subprocess.check_output(["cat", "/etc/alpine-release"]).decode('utf8')
print("Alpine Linux version: %s" % linuxVersion)
pythonVersion = sys.version
print("Python version: %s" % pythonVersion)
javaVersion = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode('utf8')
print("Java version: %s" % javaVersion)
seleniumPipVersion = subprocess.check_output(["pip", "show", "selenium"]).decode('utf8')
print("Selenium Python binding version: %s" % seleniumPipVersion)
