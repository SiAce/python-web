import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(xml)

counts = tree(".//count")

sum = 0
for count in counts:
    sum += int(count.text)

print(sum)