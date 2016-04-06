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
    authorhtml = ''
    soup = ''

    for author in root.iter('author'):
        authorhtml = author.text
        soup = BeautifulSoup(authorhtml)
        soup.a['style'] = 'color:white;text-decoration:underline;'

    for licenses in root.findall('licenses'):
        licensehtml = licenses.find('license').find('name').text

    licensehtml = '<a style="color:white;text-decoration:underline;" href="https://creativecommons.org/">' + licensehtml + '</a>'    

    print '<a style="color:white;text-decoration:underline;" href="https://commons.wikimedia.org/wiki/' + filename + '">Photo</a> by ' + str(soup) + ', ' + licensehtml
    print '\n'    
