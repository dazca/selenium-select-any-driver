# Select any Driver for Selenium ![Selenium](https://github.com/dazca/selenium-select-any-driver/tree/main/img/selenium.png =50x50)
Automatically selects any driver for selenium that is on the system and can be installed.
Compatible devices are: Firefox, Chrome, Edge, IE, Opera


![firefox](https://github.com/dazca/selenium-select-any-driver/tree/main/img/firefox.svg =100x100)![chrome](https://github.com/dazca/selenium-select-any-driver/tree/main/img/chrome.png =100x100)![edge](https://github.com/dazca/selenium-select-any-driver/tree/main/https://github.com/dazca/selenium-select-any-driver/tree/mainimg/edge.png =100x100)![IE](https://github.com/dazca/selenium-select-any-driver/tree/main/https://github.com/dazca/selenium-select-any-driver/tree/mainimg/ie.png =100x100)![Opera](https://github.com/dazca/selenium-select-any-driver/tree/main/https://github.com/dazca/selenium-select-any-driver/tree/mainimg/opera.png =100x100)

## Installation
Clone the repo, move inside the directory and type:
`pip install -e .`
Press enter.

## Usage
In your selenium project, use:
```
from any_driver_selenium import obtain_selenium_driver

driver = obtain_selenium_driver()
```

Then you can start using the automatically selected driver.

## Example

```
from any_driver_selenium import obtain_selenium_driver
url = input('Enter the url : ')
driver = obtain_selenium_driver()
driver.get(url)
```