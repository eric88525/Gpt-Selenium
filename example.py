from gpt_parser import gptParser
import time

dirver = gptParser.get_driver()
gpt = gptParser(driver=dirver)

input('After you login, press enter to continue.')


gpt('1+1=?') # Send a question
time.sleep(1) # Wait for the response
print(gpt.read_respond()) # Read the response


gpt.new_chat() # Open a new chat
gpt('2+2=?') # Send a question
time.sleep(1) # Wait for the response
print(gpt.read_respond()) # Read the response


gpt.close() # Close the driver
