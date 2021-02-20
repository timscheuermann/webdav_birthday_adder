from getpass import getpass
from webdav3.client import Client

option = {
    'webdav_hostname': "https://timscheuermann.ddns.net/remote.php/dav/calendars/admin/geburtstage/",
    'webdav_login': "admin",
    'webdav_password': "NULL"
}

if(option["webdav_password"]=="NULL"):
    option["webdav_password"] = getpass("Please enter WebDav password: ")

client = Client(option)
client.verify=True
print(client.list())