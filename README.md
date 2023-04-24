# XSS List Automate

This is a Python script for automating the testing of XSS payloads on a target website using Selenium and a list of XSS payloads. The script reads a list of XSS payloads from a file and opens the target website with each payload in the list. It also waits for the page to fully load and waits an additional 3 seconds before opening the website with the next payload in the list.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver (or any other WebDriver for the browser of your choice)

## Installation

1. Install Python 3.x on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Install the required packages using pip:

```sh
 pip install -r requirements.txt 
```


3. Download ChromeDriver (or any other WebDriver for the browser of your choice) from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Extract the downloaded file and move the executable to a directory in your system PATH.

## Usage

1. Open the `xss-payload-list.txt` file and add the XSS payloads you want to test, one per line.

2. Run the script:

```sh 
python main.py 
```


This will open the target website with each payload in the list.

Note: You may need to modify the `url_prefix` variable in the script to match the URL of your target website.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
