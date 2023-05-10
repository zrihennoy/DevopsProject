import pymysql


def get_username(user_id):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    len= cursor.execute("select user_name from public.users where user_id=%s;", user_id)
    user = (cursor.fetchall())
    cursor.close()
    conn.close()
    print(user)
    if len == 0 :
        return "The is no such user"
    else:
        return user[0][0]

def create_user(user_id, user_name):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    cursor.execute("insert into public.users (user_id, user_name) VALUES (%s,%s);", (user_id, user_name))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    cursor.execute("delete from public.users where user_id = %s;", user_id)
    conn.commit()
    cursor.close()
    conn.close()

def update_user(user_id, user_name):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwe123!!', db='public')
    cursor = conn.cursor()
    cursor.execute("update public.users set user_name = %s WHERE (user_id = %s);", (user_name, user_id))
    conn.commit()
    cursor.close()
    conn.close()