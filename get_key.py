import os
import time
import json
import random
import string
from datetime import datetime, timedelta
import urllib.parse
import requests

# ========== MÀU SẮC ==========
colors = [
    "\033[91m", "\033[93m", "\033[92m",
    "\033[96m", "\033[94m", "\033[95m", "\033[90m"
]
reset = "\033[0m"

# ========== BANNER ==========
banner_lines = [
    "╔" + "═" * 90 + "╗",
    "║{:^90}║".format("CREDIT: Đường Vĩ"),
    "║{:^90}║".format("____    ____ __     __ ___         _  __    _     _  __    _"),
    "║{:^90}║".format("|  _ \\  / ___|\\ \\   / /|_ _|       | |/ /   / \\   | |/ /   / \\"),
    "║{:^90}║".format("| | | || |  _  \\ \\ / /  | |  _____ | ' /   / _ \\  | ' /   / _ \\"),
    "║{:^90}║".format("| |_| || |_| |  \\ V /   | | |_____|| . \\  / ___ \\ | . \\  / ___ \\"),
    "║{:^90}║".format("|____/  \\____|   \\_/   |___|       |_|\\_\\/_/   \\\\|_|\\_\\/_/   \\\\"),
    "╠" + "═" * 90 + "╣",
]

ascii_art = [
    "⠀⠀⢠⡶⠛⠛⠢⣄⠀⠀⣀⣀⣀⣤⣀⣀⣀⢀⡤⠖⠛⠓⣆",
    "⠀⠀⣾⠁⢠⡆⠀⣌⠿⠿⠛⣻⣿⣯⠙⣛⠻⠏⠀⣠⣤⡀⢸",
    "⠀⠀⢹⣤⣻⠏⠚⢉⣠⣾⡵⠭⢻⠂⠠⣭⣓⠦⣀⠙⢻⣷⠟",
    "⠀⠀⠈⢯⠤⡤⢞⡧⠈⡵⠃⡞⢻⡈⠳⡙⢦⡘⢧⡓⢄⢾",
    "⠀⠀⢰⠃⡾⢡⡏⡧⢾⢄⠸⠡⠛⠋⠒⠛⡠⣽⢆⢳⡘⡎⢢",
    "⠀⢠⡇⢸⡇⣿⢰⢻⣶⣾⡷⡄⠀⠀⠀⣾⣟⣿⡹⠋⡇⣧⠀⢇",
    "⠀⢸⠀⢸⡇⢻⡸⢦⣙⡊⣿⠁⠀⠀⠀⢻⡉⠉⠀⠀⡇⣿⠀⢸⣷⣄",
    "⠀⡾⠀⢸⣧⠘⡟⠂⠲⣤⡿⠀⠀⠀⠀⠈⠓⣜⣶⢶⠁⣿⠁⢸⣿⡏",
    "⢀⣿⡀⠈⢻⣄⢸⡌⢷⡎⠀⠀⠀⠀⠀⠀⠆⠈⣯⣄⣤⡿⠀⢸⠁⢀",
    "⠈⠘⣷⡀⠀⢿⣷⣿⣟⣻⡤⡷⣶⡒⡶⠞⣠⣾⣿⡶⠿⠋⢐⠆⠀⣼",
    "⠀⠀⠹⣿⡇⠀⡎⡏⡿⣯⢽⡟⠈⣻⡁⠠⢿⣿⠟⠁⢀⢀⡾⠀⢰⡟",
    "⠀⠀⠀⣿⣧⣀⢀⣿⢠⠈⡻⠓⠉⠉⠉⠒⢾⠙⡄⢱⣤⡿⠄⣠⡿⠃",
    "⠀⠀⢀⡸⡛⠿⣧⣉⡋⠛⠧⢄⣀⣀⡀⣠⠾⢯⠴⠿⠏⣠⣾⣿⠃",
    "⠀⠀⠈⢳⡕⣄⠀⠙⠻⢶⣤⡀⠉⠙⠻⡁⠀⠀⠀⢀⡼⣻⣿⠃",
    "⠀⠀⠀⠀⠙⣮⠑⠦⣀⠀⠉⠻⢶⣄⠀⠈⠦⡀⠖⠉⢰⣿⠋",
    "⠀⠀⠀⠀⠀⠈⠳⣤⣀⠉⠓⠄⠀⠙⢿⣤⡀⠀⠀⣠⡿⠁",
    "⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣶⣤⡀⠀⠈⠻⡛⠂⠀⣉",
]

for art in ascii_art:
    banner_lines.append("║{:^90}║".format(art))

banner_lines += [
    "╠" + "═" * 90 + "╣",
    "║ {:<88} ║".format("ZALO: 0785308626"),
    "║ {:<88} ║".format("FACEBOOK: https://www.facebook.com/share/19db7bX5Jr/"),
    "╚" + "═" * 90 + "╝"
]

def print_banner():
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        print(color + line + reset)
        time.sleep(0.01)

# ========== HỖ TRỢ ==========
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

TOKEN = "28eb61f0b99302a47b7da55f3170c73934e6613c9d5c1dc99a9c123a548e3776"

def create_youmoney_link(url):
    try:
        encoded = urllib.parse.quote_plus(url)
        api = f"https://yeumoney.com/QL_api.php?token={TOKEN}&url={encoded}&format=json"
        response = requests.get(api, timeout=10)
        data = response.json()
        if data.get("status") == "success":
            return data.get("shortenedUrl")
        else:
            print("[X] Không thể tạo link:", data.get("message", "Lỗi không xác định"))
            return None
    except Exception as e:
        print("[X] Lỗi khi tạo link:", e)
        return None

def get_or_create_key():
    print_banner()
    ip = get_ip()
    keys = read_json("vuotlink.json")
    if ip in keys:
        info = keys[ip]
        if datetime.now() < datetime.strptime(info["expired"], "%Y-%m-%d %H:%M:%S"):
            print("[✓] Bạn đã có key còn hạn, không cần vượt link nữa.")
            print(f"[!] Link vượt: {info['link']}")
            return info["key"], info["link"]
        else:
            del keys[ip]

    key = generate_key()
    base_url = "https://tsanduongvi123.github.io/key-generator/?key=" + key

    print("[•] Tạo link vượt...")
    link1 = create_youmoney_link(base_url)
    if not link1:
        print("[X] Lỗi tạo link lần 1.")
        exit()
    print("[✓] Link rút gọn lần 1:", link1)

    link2 = create_youmoney_link(link1)
    if not link2:
        print("[X] Lỗi tạo link lần 2.")
        exit()
    print("[✓] Link rút gọn lần 2 (dùng để vượt):", link2)

    print("\n[!] Bạn hãy truy cập link trên để vượt link lấy key (bấm hoặc copy rồi mở trình duyệt).")
    print("[!] Sau khi vượt link thành công, quay lại đây nhập key để dùng tool.\n")

    keys[ip] = {
        "key": key,
        "link": link2,
        "expired": (datetime.now() + timedelta(hours=48)).strftime("%Y-%m-%d %H:%M:%S")
    }
    save_keys(keys)
    return key, link2

def is_valid_vip(key):
    keys = read_json("key.json")
    return key in keys.get("vip_keys", [])

def check_key_valid(key_input):
    keys = read_json("vuotlink.json")
    for info in keys.values():
        if info.get("key") == key_input:
            return datetime.now() < datetime.strptime(info["expired"], "%Y-%m-%d %H:%M:%S")
    return False

def main_menu():
    while True:
        print("\n[1] Lấy key 48h (nếu chưa có hoặc hết hạn)")
        print("[2] Nhập key đã có")
        print("[3] Nhập key VIP")
        print("[0] Thoát")
        ch = input("[?] Chọn: ").strip()
        if ch == "1":
            key, link = get_or_create_key()
            print(f"[!] Link vượt (chồng): {link}")
        elif ch in ["2", "3"]:
            user_key = input("[!] Nhập key: ").strip()
            if ch == "3" and is_valid_vip(user_key):
                break
            elif ch == "2" and check_key_valid(user_key):
                break
            else:
                print("[X] Key không hợp lệ hoặc đã hết hạn!")
                exit()
        elif ch == "0":
            exit()
        else:
            print("[X] Lựa chọn sai!")

    print("\n[!] Đã xác thực key. Bắt đầu sử dụng tool...\n")
    # Nơi bạn thêm code tool chính

if __name__ == "__main__":
    main_menu()
