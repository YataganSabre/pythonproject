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

#Counter for however amount of months from start (6 in this case)
CounterM = 0
Counter = 0
monthcheck = true
for i in CoList:
    if monthcheck == true:
        CounterM += 1
    Counter += 1
    if '24/Apr/1995:23:58:32' in i: #When april ends, so the end of the 6th month from October
           monthcheck = false
        
print("This is the number of requests (lines) from the first 6 months, starting on October 24th: ", CounterM)         
print("This is the number of requests (lines) in the log: ", Counter)
