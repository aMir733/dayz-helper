from xml.etree import ElementTree

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
                'category': item.find('category').get('name'),
                'usages': usages,
                'values': values
                }
        result.append(item_info)
    return result

with open("types.json",'w') as types_json:
    print(xmlToJson("types.xml"), file=types_json)        
