import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

info = json.loads(data)

sum_count = 0

for person in info["comments"]:
    sum_count += int(person["count"])

print(sum_count)