# Select any Driver for Selenium ![Selenium](/img/selenium.png =50x50)
Automatically selects any driver for selenium that is on the system and can be installed.
Compatible devices are: Firefox, Chrome, Edge, IE, Opera

<img src="/img/firefox.png =100x100" width="100" height="100">
<img src="/img/chrome.png =100x100" width="100" height="100">
<img src="/img/edge.png =100x100" width="100" height="100">
<img src="/img/ie.png =100x100" width="100" height="100">
<img src="/img/opera.png =100x100" width="100" height="100">
![Opera](/img/opera.png =100x100)

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