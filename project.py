#Created by Kaan M.
import urllib.request
import os.path

if !(os.path.isfile('awslog.log')):  
    print('You do not have the file, beginning file download with urllib2...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'awslog.log')
    print('File downloaded, resuming program.')
    
# Opening a file
file = open("awslog.log","r")
  
# Reading from file
Content = file.read() 
# Splitting list by new lines
CoList = Content.split("\n")
    
Counter = 0
for i in Colist
    Counter += 1
    if '30/Apr/1995:23:57:25' in i:
        print("This is the number of lines from the 24th of October to the 30th of April (6 months): " + Counter)
Counter = 0
for i in CoList:
    Counter += 1
          
print("This is the number of lines in the file: " + Counter)
