__author__ = 'Fladdie'


import sys
import urllib2
import time
'''
sys.argv[0] # this is the file name
sys.argv[1] # this is the state
sys.argv[2] # this is the time
sys.argv[3] # this is the dip from the first device
sys.argv[n] # this is the dip from "n" device
'''


php_state=sys.argv[1]

if php_state == "on":
    state = 1
elif php_state == "off":
    state = 0


php_dip=sys.argv[1]
#dip=[int(php_dip[0]),int(php_dip[1]),int(php_dip[2]),int(php_dip[3]),int(php_dip[4]),int(php_dip[5]),int(php_dip[6]),int(php_dip[7]),int(php_dip[8]),int(php_dip[9])]
dip=[int(x) for x in php_dip]

php_state=sys.argv[2]

if php_state == "on":
    state = 1
elif php_state == "off":
    state = 0

#state = 0

v1=(dip[3] << 0) + (dip[2] << 2) + (dip[1] << 4) + (dip[0] << 6)
v2=(dip[7] << 0) + (dip[6] << 2) + (dip[5] << 4) + (dip[4] << 6)
v3=(state << 0) + (state << 2) + (dip[9] << 4) + (dip[8] << 6)


page = urllib2.urlopen("http://192.168.1.90/ecmd?rfm12%202272+" + str(v1) + "," + str(v2) + "," + str(v3) + "+76+10")
result = page.read()
state = 0
v3=(state << 0) + (state << 2) + (dip[9] << 4) + (dip[8] << 6)
page = urllib2.urlopen("http://192.168.1.90/ecmd?rfm12%202272+" + str(v1) + "," + str(v2) + "," + str(v3) + "+76+10")
result = page.read()
state = 1
v3=(state << 0) + (state << 2) + (dip[9] << 4) + (dip[8] << 6)
page = urllib2.urlopen("http://192.168.1.90/ecmd?rfm12%202272+" + str(v1) + "," + str(v2) + "," + str(v3) + "+76+10")
result = page.read()
state = 0
v3=(state << 0) + (state << 2) + (dip[9] << 4) + (dip[8] << 6)
page = urllib2.urlopen("http://192.168.1.90/ecmd?rfm12%202272+" + str(v1) + "," + str(v2) + "," + str(v3) + "+76+10")
result = page.read()