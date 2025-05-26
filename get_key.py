import os
import time
import json
import random
import string
import urllib.parse
import requests
from datetime import datetime, timedelta

TOKEN = "28eb61f0b99302a47b7da55f3170c73934e6613c9d5c1dc99a9c123a548e3776"

def create_youmoney_link(url):
    try:
        encoded = urllib.parse.quote_plus(url)
        api = f"https://yeumoney.com/QL_api.php?token={TOKEN}&url={encoded}&format=json"
        response = requests.get(api, timeout=10)
        data = response.json()
        if data.get("status") == "success":
            return data.get("shortenedUrl")
    except:
        pass
    return None

def generate_key():
    return "Dgvikaka" + ''.join(random.choices(string.digits + string.ascii_letters, k=5))

def get_ip():
    try:
        return os.popen("curl -s https://api.ipify.org").read().strip()
    except:
        return "unknown"

def read_json(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def save_keys(data):
    with open("vuotlink.json", "w") as f:
        json.dump(data, f, indent=2)

def main():
    ip = get_ip()
    keys = read_json("vuotlink.json")

    if ip in keys and datetime.now() < datetime.strptime(keys[ip]["expired"], "%Y-%m-%d %H:%M:%S"):
        return

    key = generate_key()
    base = "https://tsanduongvi123.github.io/key-generator/?key=" + key
    link1 = create_youmoney_link(base)
    if not link1:
        print("[X] Lỗi tạo link lần 1.")
        return
    link2 = create_youmoney_link(link1)
    if not link2:
        print("[X] Lỗi tạo link lần 2.")
        return

    keys[ip] = {
        "key": key,
        "link": link2,
        "expired": (datetime.now() + timedelta(hours=48)).strftime("%Y-%m-%d %H:%M:%S")
    }
    save_keys(keys)

    print(f"\n[!] Vui lòng truy cập link sau để lấy key (hạn dùng 48h):\n{link2}")
    print("[!] Sau khi hoàn thành, hãy chạy lại tool và nhập key!")

if __name__ == "__main__":
    main()