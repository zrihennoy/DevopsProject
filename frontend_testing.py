import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
try:-
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5001/users/get_user_data/1")
    elem = driver.find_element(By.TAG_NAME,"H1")
    print(elem.text)
except Exception as e:
    print("test failed")

