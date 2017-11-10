import xml.etree.ElementTree as ET

data = ''' <person>

  <name>Sam</name>
  <phone>
    0757239423
  </phone>

  <last_name hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print("The name:", tree.find('name').text)
print('Last name is a hidden attribute:', tree.find('last_name').get('hide'))
