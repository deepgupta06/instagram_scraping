from instascrape import Reel
from json import dumps, loads

reel_ = Reel("https://www.instagram.com/reel/Coo1srptylw/")
SESSION_ID = "3686566848%3AjL3vAb8CbLYsii%3A17%3AAYeD3oQrc9LZpRFgaB209V76ZRaswXbIiyhGfP-2bw"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "cookie": f"sessionid={SESSION_ID}" 
}
header_json = dumps(header)
header_dict = loads(header_json)
print(header_json)
reel_.scrape(headers=header, inplace=False)

