#Created by Kaan M.
import urllib.request
import os.path

print('Beginning file download with urllib2...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, 'awslog.log')

if os.path.isfile('awslog.log'):
    # Opening a file
    file = open("awslog.log","r")
    Counter = 0
  
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1
          
    print("This is the number of lines in the file")
    print(Counter)
else:
    print ("File not exist")
