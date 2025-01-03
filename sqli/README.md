# SQL-Injection
This tool is built using the python programming language.
<br>
<br>

# Code Description
Using the requests module to make requests to the web page.
```
import requests
```
Save the given URL as a variable.
```
URL = "http://testphp.vulnweb.com/listproducts.php?cat=1"
```

Open the given payload text file "sqlpayload.txt" in read mode
Then read the lines to save the content in a list.
```
f = open("sqlpayload.txt","r")
lines = f.readlines()
```

Iterate through each index in the list from the previous step then combine the URL with the payload text file to check whether a URL is Vulnerable or not.

Then by using get method to retrieve data from a specified resource and content method to see the response’s content (this method access the raw bytes of the response payload, so convert them into a string).

If the returned response value has "Error in your SQL" It will be considered a **Vulnerable Payload**. Else it will be considered a **Not Vulnerable Payload**.

```
for x in lines:
newURL = URL + x
response = requests.get(newURL)
responseString = str(response.content)
if "error in your SQL" in responseString:
print("Vulnerable Payload! : " + x)
else:
print("Not Vulnerable Payload! : " + x)
```

## The Output
![sql1](https://user-images.githubusercontent.com/126514202/222053150-174785d6-d46e-43b1-aa79-cc4b0466e3d1.png)

## Check Output
![sql2](https://user-images.githubusercontent.com/126514202/222053148-a2a57a99-0a27-4725-a354-f335e952a991.png)

<br>
<br>

![sql3](https://user-images.githubusercontent.com/126514202/222053139-5c97bea3-8943-4688-8047-1de046baf900.png)
