
# good tutorial on XML, ElementTree, and XPath
# https://www.datacamp.com/community/tutorials/python-xml-elementtree

import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

# the top (root) level of the tree starts with a tag called 'collection'
print(root.tag)

# this element has no attributes
print(root.attrib)

# this loop will iterate over the immediate children of an element
for child in root:
    print(child.tag, child.attrib)

# this will show all the elements in a tree [as a list]
print([elem.tag for elem in root.iter()])

# ..same idea as a loop
for elem in root.iter():
    print(elem.tag)

# very useful way to visualize the whole tree
print(ET.tostring(root, encoding='utf8').decode('utf8'))

# to look for specific elements in the tree
for movie in root.iter('movie'):
    print(movie.attrib, movie.tag)

# to print out the text content of an element
for description in root.iter('description'):
    print(description.text)

# using .findall() and XPath expressions to traverse the immediate children
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)
print('\n')

# searching for movies with attribute 'favorite' = 'True'
for movie in root.findall("./genre/decade/movie/[@favorite='True']"):
    print(movie.attrib)

# use '...' inside of XPath to return the parent element of the current element.
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.attrib)

# get the 'Back 2 the Future' element; we need to fix the title
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)

# correct the title attribute
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

# write the changes out to the XML file
tree.write("movies.xml")

