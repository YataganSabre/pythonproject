#Created by Kaan M.
#This project, per instructions is intended to count the number of requests (lines) for the first 6 months, then the number of lines for the entire log.
import urllib.request
import os.path
#checks to see if the file exists, if it does NOT exist, download it and countine running.
if not(os.path.isfile('awslog.log')):  
    print('You do not have the file, beginning file download with urllib2...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'awslog.log')
    print('File downloaded, resuming program.')
    
# Opening a file
file = open("awslog.log","r")
  
# Reading from file
Content = file.read() 
# Splitting list by new lines (each line is a different request)
CoList = Content.split("\n")

#Intialize different stuff i'll use in a bit
CounterM = 0
Counter = 0
monthcheck = True
for i in CoList:
    if monthcheck == True: #counts until the 6 month period ends, which the next if statement checks
        CounterM += 1
    Counter += 1 #counts total requests
    if '24/Apr/1995:23:58:32' in i: #when 6 month period ends, change monthcheck to false so it stops counting for that 6 months
           monthcheck = False
#print outputs
print("This is the number of requests (lines) from the first 6 months, starting on October 24th and ending on April 24th: ", CounterM)         
print("This is the number of requests (lines) in the log: ", Counter)
