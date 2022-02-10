#Created by Kaan M.
import urllib.request
import os.path

print('Beginning file download with urllib2...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, 'awslog.log')

if os.path.isfile('awslog.log'):
    print ("File exist")
else:
    print ("File not exist")
