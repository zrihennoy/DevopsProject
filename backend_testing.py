import requests
import  pymysql
try:
    res = requests.post('http://127.0.0.1:5000/users/1',json={"user_name": "john"})
    print(res.content)
    res = requests.get('http://127.0.0.1:5000/users/1')
    if res.ok:
        respose= res.json()
        print(respose)
        print("user exist")
    else:
        print(res.content)
        print("user doesnt exist")

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    cursor.execute("select user_name from public.users where user_id=1;")
    username=cursor.fetchall()
    print(username[0][0])
    if username == "john":
        print("The user john is stored under id 1")
    else:
        print("The user john is not stored under id 1")
except Exception as e:
    print("test failed")
