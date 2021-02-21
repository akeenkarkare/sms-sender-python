import requests 
import json

text = ("This is a test")

url = "Upload url generated from previous code uploaded, and close the quotation marks and add +text+ in between and continue the url and the quotation marks"
# make a post request 
response = requests.request("POST", 
                            url) 

returned_msg = json.loads(response.text) 
  
# print the send message 
print(returned_msg)
