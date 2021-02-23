import socket
import sqlite3

"""
from user_operations import *

user = User_Operations()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

control_query = "SELECT * FROM Blocked_Ip_Addresses WHERE Ip_Address = ?"
user.cursor.execute(control_query, (ip_address,))
informations = user.cursor.fetchall()

date_and_time_str = informations[0][1]
ns = []

for i in date_and_time_str:

    if (i.isnumeric()):
        ns += [i]

date = [ns[0] + ns[1], ns[2] + ns[3], ns[4] + ns[5] + ns[6] + ns[7]]
time = [ns[-6] + ns[-5], ns[-4] + ns[-3], ns[-2] + ns[-1]]

date_and_time = [date, time]
print(date_and_time)
"""

while True:
    while True:
        username = input("Kullanıcı adı: ")

        print(username.split())
        if not (username.strip()):
            print("\nKullanıcı adı boş bırakılamaz!")
        else:
            break
    
    while True:
        password = input("Şifre: ")

        print(password.split())
        if not (password.strip()):
            print("\nŞifre boş bırakılamaz!")
            print(password.split())
        else:
            break

password = input("Şifre: ")

        

# [(x, "[['22', '11', '2019'], ['17', '06', '33']]")]