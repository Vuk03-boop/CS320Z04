##1. Server2 šalje Serveru1 vreme poslednje izmene svog data.txt.
# Server1 proverava da li je njegov fajl noviji.
# Ako jeste, ispisuje poruku: „Server1 ima noviju verziju“.
# Ako nije, ispisuje „Server2 ima noviju verziju“ ili „Fajlovi su sinhronizovani“ ako je vreme isto.
import os
from socket import socket, SOCK_STREAM, AF_INET

fajl="data.txt"
host="127.0.0.1"
port=6543
with socket(AF_INET, SOCK_STREAM) as s_client:
    s_client.connect((host, port))
    personal_last_file_edited_date = (str)(os.path.getmtime(fajl)).encode("utf-8")
    print(personal_last_file_edited_date)
    s_client.send(personal_last_file_edited_date)

