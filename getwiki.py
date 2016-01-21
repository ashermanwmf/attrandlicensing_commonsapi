import os
import sys
import urllib
import xml.etree.ElementTree as ET


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
    
    print '[[File:' + filename + '|Photo]] by ' + authorhtml + licensehtml
    print '\n'