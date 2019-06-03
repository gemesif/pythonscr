import sys
import re

#***************************************************************************************************************

def month_string_to_number_string(string):
    m = {
        'jan': '1',
        'feb': '2',
        'mar': '3',
        'apr': '4',
        'may': '5',
        'jun': '6',
        'jul': '7',
        'aug': '8',
        'sep': '9',
        'oct': '10',
        'nov': '11',
        'dec': '12'
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        # raise ValueError('Not a month')
        print('Not a month')

#***************************************************************************************************************

# firewall,info attack
catchLine = re.compile(r"firewall,info attack")

# Apr/19/2019 20:43:48 firewall,info attack input: in:ether1 out:(unknown 0), src-mac 00:01:5c:7a:26:45, proto TCP (SYN), 156.201.187.205:48036->37.188.81.143:23, len 40
# May/05/2019 07:11:45

# jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec
# https://stackoverflow.com/questions/3418050/month-name-to-month-number-and-vice-versa-in-python
# https://stackoverflow.com/questions/16670601/how-to-perform-arithmetic-operation-on-a-date-in-python
# https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python

date = re.compile(r"([a-zA-Z]{3})/(\d{2})/(\d{4})\s(\d{2}):(\d{2}):(\d{2})")

for line in sys.stdin:
    if not catchLine.search(line):
        continue
    # print(line)
    m = date.match(line)
    print(month_string_to_number_string(m.group(1)) +  m.group(2) + m.group(3) + m.group(4) + m.group(5) + m.group(6))
    month = month_string_to_number_string(m.group(1));  day =  m.group(2); year = m.group(3); hour = m.group(4); min = m.group(5); sec = m.group(6)
    

#***************************************************************************************************************

# cat /home/gemesif/tmp/logs.*.txt | python logregexp.py
