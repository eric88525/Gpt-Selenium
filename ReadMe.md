# GPT + Selenium
Selenium can directly control the browser to manipulate elements on the screen, and is commonly used for dynamic web scraping. If you have spent a lot of money buying GPT-Plus, but find that you still need to pay extra for using the API (that's me), you can try this method.

**Pros**
Unlimited usage with a monthly fee of 20 USD.

**Cons**
Usage is limited to small amounts as there is a restriction of 45 minutes if too much data is requested within an hour.

## How to use?
Download [ChromeDriver](https://chromedriver.chromium.org/downloads). I strongly recommend that you update to the latest version of Chrome.

**Linux setup**
```
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/
chmod +x /usr/bin/chromedriver
```
**Windows**
Either click the exe file or specify driver_path when getting the driver.

Install requirements [Selenium](https://github.com/SeleniumHQ/selenium) and [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
```
pip install -r requirements.txt
```
## Example
A window will pop up after execution. Please log in manually.
```python
from gpt_parser import gptParser
import time

dirver = gptParser.get_driver(driver_path="driver path")
gpt = gptParser(driver=dirver)
```
Send and read the message.
```python
gpt('1+1=?') # Send a question
time.sleep(1) # Wait for the response
print(gpt.read_respond()) # Read the response
```
![](/imgs/result.png)
![](/imgs/gpt-1.png)
![](/imgs/gpt-2.png)
Open a new chat
```python
gpt.new_chat()
```

Close the driver
```python
gpt.close() # Close the driver
```