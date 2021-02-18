import requests 
import json

url = "Put the api key, link to the website you want to send the message from, and your message by generating the url."

# make a post request 
response = requests.request("POST", 
                            url) 

returned_msg = json.loads(response.text) 
  
# print the send message 
print(returned_msg)
