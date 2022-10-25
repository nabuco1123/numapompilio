import time
from datetime import datetime as dt

hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
hosts_dir = "hosts"

website_list = [

    "www.facebook.com",
    "facebook.com",
    "mail.google.com"
]

from_hour = 10
to_hour = 18

while True:
    
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() <dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("working...")
        with open(hosts_dir, 'r+') as file:
            content = file.read()
            print(content)
    else:
        print("fun...")
    time.sleep(1)