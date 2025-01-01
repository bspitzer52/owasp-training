import requests
from bs4 import BeautifulSoup
from termcolor import colored
from time import time

# Other functions (how_many_forms, links_to_page, get_inputs, etc.) remain unchanged.

def find_xss(url, payload):
    xss_flag = False
    try:
        if ("https://" not in url and "http://" not in url):
            url = "http://{}".format(url)
    except Exception as e:
        print(e)
        pass

    print(colored("Request Sent to Site {}".format(url), "green"))

    inputs = get_inputs(url)  # Get input boxes
    if len(inputs) == 0:
        return -1
    print(colored("Finding input box in the page..", "green"))
    start = time()
    for pyld in payload:
        try:
            for i in inputs:
                name = str(i.get("name"))
                r = requests.get(url + "?" + name + "=" + pyld)
                if pyld in str(r.content, "utf-8"):
                    xss_flag = True

                    print()
                    print(colored("#FOUND -> Payload:{}".format(pyld), "green"))
                    end = time()
                    ctime = end - start
                    print(colored("Vulnerable URL -> {}".format(url), "red"))
                    print(colored("Vulnerable Input Box-> {}".format(i), "red"))
                    if xss_flag:
                        print()
                        print(colored("Time:{} Seconds".format(ctime), "white"))
                        return 1
                else:
                    print(colored("#NOT FOUND -> Payload:{}".format(pyld), "red"))
        except Exception as e:
            print(e)
            pass


def payloads(file):
    with open(file, "rb") as f:
        payloads = f.read().splitlines()
    return payloads


if __name__ == '__main__':
    intro = '''
        #################################################################
        #                                                               #
        #                       XSS Scraper                             #
        #               Developed by Brandon Spitzer                    #
        #                                                               #
        #################################################################
    '''
    print(colored(intro, "green"))
    print()

    choices = '''
    1)XSS URL Scan
    2)Total Scan
    3)Fetch all Links
    4)Fetch Form Count
    5)Fetch Input Box
    '''
    try:
        print(choices)
        choice = input("Make a Choice -->")

        # Define the payload file directly
        payload_file = "payload.txt"  # File is in the same directory
        payload = payloads(payload_file)  # Read payloads from payload.txt

        if choice == "1":
            url = input("Please input the url -> ")
            result = find_xss(url, payload)
            if result == -1:
                print("No input box found to attack.")
            else:
                print(colored(40 * "-", "red"))
        elif choice == "2":
            url = input("Please input the url -> ")
            links = links_to_page(url)
            for link in links:
                try:
                    result = find_xss(link, payload)
                    if result == -1:
                        print("No input box found to attack.")
                    elif result == 1:
                        test = input("Do you want to test other links in the page:(1->Continue or 0->Stop) (Default:1)") or "1"
                        if test == "0":
                            exit(0)
                        print(colored(40 * "-", "red"))
                    else:
                        print(colored(40 * "-", "red"))
                except Exception as e:
                    print(e)
                    pass
        elif choice == "3":
            url = input("URL Please -> ")
            links = links_to_page(url)
            for i in links:
                print(i)
        elif choice == "4":
            url = input("URL Please -> ")
            forms = how_many_forms(url)
            for i, j in forms.items():
                print(i, "->", j, "form(s)")
        elif choice == "5":
            url = input("URL Please -> ")
            inputs = get_inputs(url)
            for i in inputs:
                print(i)
        else:
            print("Bad Choice,Try Your Luck Next time")
            exit(1)
    except KeyboardInterrupt:
        print("Bye Bye..Exiting")
