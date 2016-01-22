import os
import sys
import urllib
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
from html5lib.sanitizer import HTMLSanitizerMixin

class TestHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)

        self.elements = set()

    def handle_starttag(self, tag, attrs):
        self.elements.add(tag)

    def handle_endtag(self, tag):
        self.elements.add(tag)


def is_html(text):
    elements = set(HTMLSanitizerMixin.acceptable_elements)

    parser = TestHTMLParser()
    parser.feed(text)

    return True if parser.elements.intersection(elements) else False

#licensing links (not always in the xml)
cc0_1 = ', freely licesned under [https://creativecommons.org/publicdomain/zero/1.0/ '
cc_1_0 = ', freely licensed under [http://creativecommons.org/licenses/by/1.0/ '
cc_2_0 = ', freely licensed under [http://creativecommons.org/licenses/by/2.0/ '
cc_2_5 = ', freely licensed under [http://creativecommons.org/licenses/by/2.5/ '
cc_3_0 = ', freely licensed under [http://creativecommons.org/licenses/by/3.0/ '
cc_4_0 = ', freely licensed under [http://creativecommons.org/licenses/by/4.0/ '
cc_1_0_SA = ', freely licensed under [http://creativecommons.org/licenses/by-sa/1.0/ '
cc_2_0_SA = ', freely licensed under [http://creativecommons.org/licenses/by-sa/2.0/ '
cc_2_5_SA = ', freely licensed under [http://creativecommons.org/licenses/by-sa/2.5/ '
cc_3_0_SA = ', freely licensed under [http://creativecommons.org/licenses/by-sa/3.0/ '
cc_4_0_SA = ', freely licensed under [http://creativecommons.org/licenses/by-sa/4.0/ '

for arg in sys.argv[1:]:
    filename = arg

    requestURL = 'https://tools.wmflabs.org/magnus-toolserver/commonsapi.php?image=' + filename

    root = ET.parse(urllib.urlopen(requestURL)).getroot()

    licensehtml= ''
    authorhtml = ''

    print authorhtml
    
    if is_html(authorhtml) is 'True':
        soup = BeautifulSoup(authorhtml)
        for author in root.iter('author'):
            authorhtml = author.text
            authorhtml = '[[' + soup.a['title'] + '|' + soup.a.text + ']]'
    else:
        for author in root.iter('author'):
            authorhtml = author.text
        
    for licenses in root.findall('licenses'):
        licensehtml = licenses.find('license').find('name').text
    
#    if licensehtml == 'CC-Zero':
#        licensehtml = cc0_1 + licensehtml + ']'
#    elif licensehtml == 'CC-PD-Mark':
#        licensehtml = ' ' + licensehtml
#    elif licensehtml == 'CC-BY-1.0':
#        licensehtml = cc_1_0 + licensehtml + ']'    
#    elif licensehtml == 'CC-BY-2.0':
#        licensehtml = cc_2_0 + licensehtml + ']'
#    elif licensehtml == 'CC-BY-2.5':
#        licensehtml = cc_2_5 + licensehtml + ']'
#    elif licensehtml is 'CC-BY-SA-1.0-migrated' or 'CC-BY-SA-1.0':
#        licensehtml = cc_1_0_SA + licensehtml + ']'
#    elif licensehtml is 'CC-BY-SA-2.0-migrated' or 'CC-BY-SA-2.0':
#        licensehtml = cc_2_0_SA + licensehtml + ']'
#    elif licensehtml is 'CC-BY-SA-2.5-migrated' or 'CC-BY-SA-2.5':
#        licensehtml = cc_2_5_SA + licensehtml + ']'
#    elif licensehtml is 'CC-BY-SA-3.0-migrated' or 'CC-BY-SA-3.0':
#        licensehtml = cc_3_0_SA + licensehtml + ']'
#    elif licensehtml is 'CC-BY-SA-4.0-migrated' or 'CC-BY-SA-4.0':
#        licensehtml = cc_4_0_SA + licensehtml + ']'

    
    print '[[File:' + filename + '|Photo]] by ' + authorhtml + ' ' + licensehtml
    print '\n'