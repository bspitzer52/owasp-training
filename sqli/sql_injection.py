#This module allows you to send HTTP requests
import requests

#The provided URL is set as a variable called URL
URL = "http://testphp.vulnweb.com/listproducts.php?cat=1"
f = open("sqlpayload.txt","r")

#Contains payload and saved as a list
lines = f.readlines()

print("All Payload Used:")
print(lines)
print()


for x in lines:
    #The iteration will test newURL's (URL and payload text file) for vulnerability
    newURL = URL + x
    #Use the request module's GET method to obtain data from a resource
    response = requests.get(newURL)
    #See the response's content using the content method
    responseString = str(response.content)
    #If the answer response has "Error in your SQL". It's vulnerable. Otherwise, it's not vulnerable.
    if "error in your SQL" in responseString:
      print("Vulnerable Payload! : " + x)
    else:
      print("Not Vulnerable Payload! : " + x)