import sys
import re
import urllib.request
import json

def xstr(s):
   return s or "None"

p = re.compile(r"\s*(\d+)\s+(.+)")

i = 0
countlimit = 100

for line in sys.stdin:
    i += 1
    line = line.rstrip()
    # print(line)
    m = p.match(line)
    count = m.group(1)

    if int(count) < countlimit:
        print('{} {}'.format((count), str(countlimit)))
        continue

    ipaddress = m.group(2)
    # print(count + '-' + ipaddress)

    with urllib.request.urlopen("https://geoip-db.com/json/" + ipaddress) as url:
        pass
        data = json.loads(url.read().decode())
        # print(data)
        print('{} {} {} {} \'{}\' \'{}\' \'{}\''.format(
         str(i), count, 
         xstr(data.get("IPv4")),
         xstr(data.get("country_code")),
         xstr(data.get("country_name")),
         xstr(data.get("city")),
         xstr(data.get("state"))
        ))

#**************************************************************************************

# 37.188.81.143
# cat /home/gemesif/tmp/logs.*.txt | grep 'attack' | cut -d',' -f5 | cut -d'-' -f1 | cut -d':' -f1 | sort | uniq --count --repeated | sort -n | python geoloc.py

# 21474  185.176.27.174
# 26779  81.22.45.28
# 41650  46.161.27.81

# 2441 80.99.183.254
#{'country_code': 'HU', 'country_name': 'Hungary', 'city': 'Budapest', 'postal': '1083', 'latitude': 47.5, 'longitude': 19.0833, 'IPv4': '80.99.183.254', 'state': 'Budapest'}

