from selenium.webdriver.remote.webdriver import By
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys

class gptParser:
    def __init__(self,
                 driver,
                 gpt_url: str = 'https://chat.openai.com/'):
        """ ChatGPT parser
        Args:
            driver_path (str, optional): The path of the chromedriver.
            gpt_url (str, optional): The url of ChatGPT.
        """
        # Start a webdriver instance and open ChatGPT
        self.driver = driver
        self.driver.get(gpt_url)

    @staticmethod
    def get_driver(driver_path: str = None,):
        return uc.Chrome() if driver_path is None else uc.Chrome(driver_path)

    def __call__(self, query: str):
        # Find the input field and send a question
        input_field = self.driver.find_element(
            By.TAG_NAME, 'textarea')
        input_field.send_keys(query)
        input_field.send_keys(Keys.RETURN)

    def read_respond(self):
        try:
            response = self.driver.find_elements(By.TAG_NAME, 'p')[-2].text
            return response
        except:
            return None

    def new_chat(self):
        """Open a new chat"""
        self.driver.find_element(By.XPATH, '//a[text()="New chat"]').click()

    def close(self):
        self.driver.quit()