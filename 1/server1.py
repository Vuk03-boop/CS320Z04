##1. Server2 šalje Serveru1 vreme poslednje izmene svog data.txt.
# Server1 proverava da li je njegov fajl noviji.
# Ako jeste, ispisuje poruku: „Server1 ima noviju verziju“.
# Ako nije, ispisuje „Server2 ima noviju verziju“ ili „Fajlovi su sinhronizovani“ ako je vreme isto.
import os
from socket import socket, AF_INET, SOCK_STREAM

host="127.0.0.1"
port=6543
fajl="data.txt"
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        last_edited_date=float(conn.recv(1024).decode("utf-8"))
        personal_last_file_edited_date=os.path.getmtime(fajl)
        print(personal_last_file_edited_date)
        if personal_last_file_edited_date > last_edited_date:
            print("Server1 ima noviju verziju\n")
        elif personal_last_file_edited_date < last_edited_date:
            print("Server2 ima noviju verziju\n")
        else:
            print("Serveri su sinhronizovani\n")