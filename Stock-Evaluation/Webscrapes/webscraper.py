"""
Description: Selenium Webscraping tool to 
             identify key elements found in 
             a page

Author: Zoren Dela Cruz
Created: 06-06-2023
"""

import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Webscraping:
    """ Webscraping Class """

    def __init__(self) -> None:
        """ 
        Instatniate the webscraping tool
        """
        ## Setup chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")

        # Set path to chromedriver as per your configuration
        homedir = os.getcwd()
        webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

        # Choose Chrome Browser
        self.browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    def __del__(self) -> None:
        """
        Destorys the Webscraping class
        """
        self.browser.quit()

    def extract_values(self, url:str, css_element:str) -> list:
        """
        Extracts the value from the given HTML element found 
        in the url

        Args:
            url (str): Website of interest
            css_element (str): Html Element to be dissected

        Returns:
            list: List of values found in the element
        """
        # Gets page
        self.browser.get(url)
        
        # Extract the value from element and store into a list
        result = []
        values = self.browser.find_elements(By.CSS_SELECTOR, css_element)
        for value in values:
            result.append(value.text)

        return result
