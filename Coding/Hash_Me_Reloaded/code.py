import requests, re, hashlib
#Function to convert binary 0s and 1s to text
def binary_to_string(binary):
    return "".join(chr(int(binary[i:i+8],2)) for i in range(0,len(binary),8))



response = requests.get('http://challenges.ringzer0team.com:10014/', cookies = {'PHPSESSID' : 'xxxxxxxxxxxxxxxxxx'})

#Getting the message and convert the binary data to text.
string = re.search('BEGIN MESSAGE(.*)END MESSAGE', str(response.content))
string = re.sub('[^A-Za-z0-9]+', '', string.group(1))
string = re.search('brn(.*)brn', string)
string = binary_to_string(string.group(1))
#print('The message to hash is: ', string)

#Extract URL from HTTP response
url = re.search('answer back using (.*)\[your_response\]', str(response.content))
#print('The URL to send Hash is: ', url.group(1))

#Generate Hash and then send response
hasher = hashlib.sha512(string.encode())
#print('The Hash is: ', hasher.hexdigest())
request_str = url.group(1) + hasher.hexdigest()
response = requests.get(request_str, cookies = {'PHPSESSID' : 'xxxxxxxxxxxxxxxxxxxx'})

#Extract the Flag from the response
Flag = re.search('alert alert-info">(.*)</div>   ', str(response.content))
print(Flag.group(1))
