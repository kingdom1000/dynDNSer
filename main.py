from settings import *
from getHostStatus import *

# Open log to find last IP address
openLog = open('ipAddress.log', 'r')
lastIP = openLog.read()
openLog.close()

externalIP = externalIP()

# Compare last IP address and New IP address
if lastIP == externalIP:
    # Do nothing
    print 'no change'
else:
    # Update dyndns and write to log file
    dynDnsUrl = 'http://' + dynDnsUsername + ':' + dynDnsPassword + '@members.dyndns.org/nic/update?hostname=' + dynDnsHostname + '&myip=' + externalIP
    r = requests.get(dynDnsUrl)
    openLog = open('ipAddress.log', 'w')
    openLog.write(externalIP)
    openLog.close()
    print 'change and updated'
