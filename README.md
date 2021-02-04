# Select any Driver for Selenium ![Selenium](/img/selenium.png =50x50)
Automatically selects any driver for selenium that is on the system and can be installed.
Compatible devices are: Firefox, Chrome, Edge, IE, Opera

<img src="/img/firefox.svg =100x100" width="100" height="100">
![firefox](/img/firefox.svg =100x100)![chrome](/img/chrome.png =100x100)![edge](/img/edge.png =100x100)![IE](/img/ie.png =100x100)![Opera](/img/opera.png =100x100)

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