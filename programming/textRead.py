import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3

def textRead(file_url):
    data=urlopen(file_url).read().decode('utf-8')
    print("Capital Letters: ", sum(1 for c in data if c.isupper()))
    
file_url="https://cs.indstate.edu/info/files/text/shakespeare_random_26.txt"
textRead(file_url)
