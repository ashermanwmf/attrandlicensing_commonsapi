#########################################################################
#   How this works                              
# 1. This script allows for multiple arguments to print mulitple files
#    attributions and licensing. There is NO added link for creative commons licensing.
# ex: $ python gethtml.py File:Dog.png
# 2. The above example returns (still needs appropriate licensing with link):
#       <a style="color:white;text-decoration:underline;" href="https://commons.wikimedia.org/wiki/File:Dog.png">Photo</a> 
#       by <a href="http://commons.wikimedia.org/wiki/User:Loupeznik" title="User:Loupeznik" style="color:white;text-decoration:underline;">Loupeznik</a>, 
#       <a style="color:white;text-decoration:underline;" href="https://creativecommons.org/">CC-BY-SA-3.0,2.5,2.0,1.0</a> 
# 3. othe possible example:
#   ex: $ python gethtml.py File:Dog.png File:Cat.jpg
# (choose getwiki.py to print the file info in wiki format)
# (one packages: BeautifulSoup)
# recently updated to add in licensing url
#########################################################################

import os
import sys
import re
import urllib
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup

#([\w\s,!*?]*\.\w{3}) regex to use for sys.argv solution (works for anything ending in ".png, .svg, .jpg" etc...

for arg in sys.argv[1:]:
    filename = arg

    requestURL = 'https://tools.wmflabs.org/magnus-toolserver/commonsapi.php?image=' + str(filename) + '&forcehtml'

    root = ET.parse(urllib.urlopen(requestURL)).getroot()

    licensehtml= ''
    licenseurlopen = ''
    licenseurlclose = ''
    authorhtml = ''
    soup = ''

    for author in root.iter('author'):
        authorhtml = author.text
        soup = BeautifulSoup(authorhtml)
        # check soup for a link to add styling or just use the text
        if "</a>" in soup:
            soup.a['style'] = 'color:white;text-decoration:underline;'
        else:
            soup = soup

    for licenses in root.findall('licenses'):
        licensehtml = licenses.find('license').find('name').text
        # find the license url, if it exists then add it to the licenseurl variable
        if licenses.find('license').find('license_info_url') is None:
            licenseurlopen = ''
            licenseurlclose = ''
        else:
            licenseurlopen = '<a style="color:white;text-decoration:underline;" href="'+ licenses.find('license').find('license_info_url').text + '">'
            licenseurlclose = '</a>'

    licensehtml = licenseurlopen + licensehtml + licenseurlclose    

    print '<a style="color:white;text-decoration:underline;" href="https://commons.wikimedia.org/wiki/' + filename + '">Photo</a> by ' + str(soup) + ', ' + licensehtml
    print '\n'    
