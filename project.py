#Created by Kaan M.
import urllib.request

print('Beginning file download with urllib2...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, root)
