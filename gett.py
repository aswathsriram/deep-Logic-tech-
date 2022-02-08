import requests
import re
import json


url = "https://time.com"
response = requests.get(url)
pattern = "<li class=\"latest-stories__item\">\s*.*<a href=\"(.*)\">\s*<h3 class=\"latest-stories__item-headline\">(.*)</h3>"
data = re.findall(pattern,response.text)
output_list=[]
for i in range(0,len(data)):
    temp = {'title':data[i][1], 'link':"https://time.com"+data[i][0]}
    output_list.append(temp)
print (json.dumps(output_list))