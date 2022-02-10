#Created by Kaan M.
#This project, per instructions is intended to count the number of requests (lines) for the first 6 months, then the number of lines for the entire log.
import urllib.request
import os.path

if not(os.path.isfile('awslog.log')):  
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
for i in CoList:
    Counter += 1
    if '30/Apr/1995:23:57:25' in i:
        print("This is the number of requests (lines) from the first 6 months, starting on October 24th: ", Counter)
        break
Counter = 0
for i in CoList:
    Counter += 1
          
print("This is the number of requests (lines) in the log: ", Counter)
