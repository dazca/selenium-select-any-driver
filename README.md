# Select any Driver for Selenium <img src="/img/selenium.png" width="60" height="60">

Automatically selects any driver for selenium that is on the system and can be installed.
Compatible devices are: Firefox, Chrome, Edge, IE, Opera

<p float="left">
    <img src="/img/firefox.png" width="100" height="100">
    <img src="/img/chrome.png" width="100" height="100">
    <img src="/img/edge.png" width="100" height="100">
    <img src="/img/ie.png" width="100" height="100">
    <img src="/img/opera.png" width="100" height="100">
</p>

## Installation
Clone the repo, move inside the directory and install through pip:
```
pip install .
```

## Update
Move to the download folder and do:
```bash
git pull
pip install .
```

## Usage
In your selenium project, use:
```python
from any_driver_selenium import obtain_selenium_driver

driver = obtain_selenium_driver()
```

Then you can start using the automatically selected driver.

## Example
```python
from any_driver_selenium import obtain_selenium_driver
url = input('Enter the url : ')
driver = obtain_selenium_driver()
driver.get(url)
```