#!/usr/bin/python
# -*- coding: utf_8 -*-

import mechanize, sys, re
from BeautifulSoup import BeautifulSoup

if (len(sys.argv) == 1): quit("please input ip address or hostname")

print "=============================="
print "target:" + " ".join(sys.argv[1:])
print "=============================="

keyword = "+".join(sys.argv[1:])
BASE_URL = "http://www.ip-adress.com/ip_tracer/" + keyword
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent',
                                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36')]

soup = BeautifulSoup(br.open(BASE_URL).get_data())
table = soup.find(id="ipinfo").find("table")

lat = ""
lng = ""
if (not table): quit("not found")
for tr in table.findAll("tr"): 
  if 'latitude' in re.compile(r'<.*?>').sub('', unicode(tr.find("th"))):
    lat = re.compile(r'<.*?>').sub('', re.compile(r'<(a|script) .*').sub('', unicode(tr.find("td")))).strip()
  if 'longitude' in re.compile(r'<.*?>').sub('', unicode(tr.find("th"))):
    lng = re.compile(r'<.*?>').sub('', re.compile(r'<(a|script) .*').sub('', unicode(tr.find("td")))).strip()
  print re.compile(r'<.*?>').sub('', unicode(tr.find("th"))) + "" + re.compile(r'<.*?>').sub('', re.compile(r'<(a|script) .*').sub('', unicode(tr.find("td")))).strip()

print ""
print "https://www.google.co.jp/maps/place//@"+unicode(lat)+","+unicode(lng)+",15z"
print ""
