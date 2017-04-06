import ConfigParser
import requests
from requests.auth import HTTPBasicAuth

def update_ip():
  cp = ConfigParser.ConfigParser()
  cp.read('config.ini')

  try:
    label = cp.get('Main', 'label')
    username = cp.get('Main', 'username')
    password = cp.get('Main', 'password')
  except ConfigParser.NoSectionError as e:
    print "Please make sure you have a config.ini file in this directory, with label, username, and password defined."
    return

  response = requests.get('https://updates.opendns.com/nic/update?hostname=%s' % label, auth=HTTPBasicAuth(username, password))
  if response.status_code == requests.codes.ok:
    print "Successfully updated IP:", response.text
  else:
    print "Failed to update IP:", response
    print "Make sure your password doesn't have any special characters in it, other than underscore. Try using underscore for the special character."

if __name__ == '__main__':
  update_ip()
