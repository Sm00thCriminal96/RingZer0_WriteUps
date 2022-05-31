import requests, re, hashlib
response = requests.get('http://challenges.ringzer0team.com:10013/', cookies = {'PHPSESSID' : 'xxxxxxxxxxxxxxx'})

#Getting the message and return URL from HTTP response
string = re.search('BEGIN MESSAGE(.*)END MESSAGE', str(response.content))
string = re.sub('[^A-Za-z0-9]+', '', string.group(1))
string = re.search('brn(.*)brn', string)
#print('The message to hash is: ', string.group(1))
url = re.search('answer back using (.*)\[your_response\]', str(response.content))
#print('The URL to send Hash is: ', url.group(1))

#Generate Hash and then send response
hasher = hashlib.sha512(string.group(1).encode())
#print('The Hash is: ', hasher.hexdigest())
request_str = url.group(1) + hasher.hexdigest()
response = requests.get(request_str, cookies = {'PHPSESSID' : 'xxxxxxxxxxxxxxx'})

#Extract the Flag from the response
Flag = re.search('alert alert-info">(.*)</div> ', str(response.content))
print(Flag.group(1))
