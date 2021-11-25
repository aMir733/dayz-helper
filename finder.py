import sys,requests
from xml.dom import minidom

#types_url = 'https://raw.githubusercontent.com/BohemiaInteractive/DayZ-Central-Economy/master/dayzOffline.chernarusplus/db/types.xml'

types_xml = minidom.parse("types.xml")
items = types_xml.getElementsByTagName("type")

# return value: [{'name': 'AK101', 'nominal': '2', ... , 'usages': ['Military','Police'] , ... },{'name': 'AK101_Black', ... }]
def xmlToJson(xml):
    items = xml.getElementsByTagName("types")
    for item in items:


