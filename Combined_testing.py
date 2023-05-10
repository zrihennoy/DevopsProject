import requests
import  pymysql
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


try:
    username=input("please enter username: ")
    userid=input("please enter user id: ")
    res = requests.post(f'http://127.0.0.1:5000/users/{userid}',json={"user_name": username})
    print(res.content)
    res = requests.get(f'http://127.0.0.1:5000/users/{userid}')
    respose = res.json()
    if res.ok and respose['user_name'] == username:
        print("user exist")
    else:
        print(res.content)
        print("user doesnt exist in the spesified id")

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    cursor.execute("select user_name from public.users where user_id=%s;",userid)
    usernamesql=cursor.fetchall()
    print(usernamesql[0][0])
    if usernamesql[0][0] == username:
        print("The user is stored in the DB")
    else:
        print("The user  is not stored in db")
except Exception as e:
    print("test failed")
try:
    driver = webdriver.Chrome()
    driver.get(f"http://127.0.0.1:5001/users/get_user_data/{userid}")
    elem = driver.find_element(By.TAG_NAME,"H1")
    print(elem.text)
    if elem.text == username:
        print("correct name")
    else:
        print("incorrect name")
except Exception as e:
    print("test failed")
