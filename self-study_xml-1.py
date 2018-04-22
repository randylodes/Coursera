
# Studying ElementTree for reading/writing XML

# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://www.w3schools.com/xml/xml_syntax.asp

# XML is an inherently hierarchical data format, and the most natural way to represent it is with a tree.
# ET has two classes for this purpose -
# 'ElementTree' represents the whole XML document as a tree, and 'Element' represents a single node

# common convention for import
import xml.etree.cElementTree as ET

# open an XML file
tree = ET.parse('country_data.xml')

# XML documents must contain one root element that is the parent of all other elements
root = tree.getroot()

# finding certain Elements
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

lst = tree.findall('country')

print('Country count: ', len(lst))
print(type(lst))
for item in lst:
    print('Name', item.get('name'))
    print('Rank', item.find('rank').text)
    print('Year', item.find('year').text)







