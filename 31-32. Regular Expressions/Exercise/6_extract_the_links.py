import re

regex = r'(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)'
valid_urls = []

line = input()
while line:
    matches = re.search(regex, line)
    if matches:
        valid_urls.append(matches.group(1))
    line = input()

for valid_url in valid_urls:
    print(valid_url)
