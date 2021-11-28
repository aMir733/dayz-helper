from xml.etree import ElementTree
import sys, json

def xmlToJson(xml):
    xml_parsed = ElementTree.parse(xml)
    root = xml_parsed.getroot()
    result = []
    for item in root.findall("type"):
        usages = []
        for usage in item.findall('usage'):
            usages.append(usage.get('name'))
        values = []
        for value in item.findall('value'):
            values.append(value.get('name'))
        categories = []
        for category in item.findall('category'):
            categories.append(category.get('name'))
        item_info = {
                'name': item.get('name'),
                'nominal': item.find('nominal').text,
                'lifetime': item.find('lifetime').text,
                'restock': item.find('restock').text,
                'min': item.find('min').text,
                'quantmin': item.find('quantmin').text,
                'quantmax': item.find('quantmax').text,
                'cost': item.find('cost').text,
                'flags': item.find('flags').attrib,
                'categories': categories,
                'usages': usages,
                'values': values
                }
        result.append(item_info)
    return result

try:
    with open("types.json") as types_json:
        items = json.load(types_json)
except:
    with open("types.json",'w') as types_json:
        json.dump(xmlToJson("types.xml"), types_json, indent=4)

query = sys.argv[1].lower()
for item in items:
    if query in item['name'].lower():
        print(json.dumps(item, indent=2))
