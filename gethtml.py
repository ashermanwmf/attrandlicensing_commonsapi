import os
import sys
import urllib
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup

cc_0 = 'freely licensed under <a href=" '
cc_1_0 = 'freely licensed under <a href=" '
cc_2_0 = 'freely licensed under <a href=" '
cc_3_0 = 'freely licensed under <a href=" '
cc_4_0 = 'freely licensed under <a href=" '
cc_3_0_SA = 'freely licensed under <a href=" '
cc_4_0_SA = 'freely licensed under <a href=" '
pd = '<a href=" '


for arg in sys.argv[1:]:
    filename = arg

    requestURL = 'https://tools.wmflabs.org/magnus-toolserver/commonsapi.php?image=' + filename

    root = ET.parse(urllib.urlopen(requestURL)).getroot()

    licensehtml= ''
    authorhtml = ''

    for author in root.iter('author'):
        authorhtml = author.text

    for licenses in root.findall('licenses'):
        licensehtml = licenses.find('license').find('name').text

    licensehtml = '<a href="https://creativecommons.org/">' + licensehtml + '</a>'    
    
    print '<a href="https://commons.wikimedia.org/wiki/File:' + filename + '">Photo</a> by ' + authorhtml + licensehtml
    print '\n'    
    