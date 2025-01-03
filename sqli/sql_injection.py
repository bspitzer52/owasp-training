import requests

# The provided URL is set as a variable called URL
URL = "http://testphp.vulnweb.com/listproducts.php?cat=1"
f = open("sqlpayload.txt", "r")

# Contains payload and saved as a list
lines = f.readlines()

print("All Payloads Used:")
print(lines)
print()

# Open a file to log results
with open("results.log", "w") as log_file:
    for x in lines:
        # The iteration will test newURLs (URL and payload text file) for vulnerability
        newURL = URL + x.strip()  # Strip any extra whitespace from payloads

        # Use the request module's GET method to obtain data from a resource
        try:
            response = requests.get(newURL)
            response.raise_for_status()  # Ensure we get a successful HTTP response

            # Check the content for common signs of SQL injection vulnerability
            responseString = str(response.content)

            if "error in your SQL" in responseString.lower():  # Case insensitive
                result = f"Vulnerable Payload! : {x.strip()}"
                print(result)
                log_file.write(result + "\n")
            else:
                result = f"Not Vulnerable Payload! : {x.strip()}"
                print(result)
                log_file.write(result + "\n")
        
        except requests.exceptions.RequestException as e:
            # Handle network errors or other exceptions
            print(f"Request failed for payload: {x.strip()} with error: {e}")
            log_file.write(f"Failed request for payload: {x.strip()} with error: {e}\n")

print("\nFinished testing. Results logged in 'results.log'.")
