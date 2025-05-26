import os
import sys
import requests
import subprocess
import json

GET_KEY_SCRIPT = "get_key.py"
GITHUB_RAW_KEY = "https://raw.githubusercontent.com/tsanduongvi123/Gopcode/main/key.json"
GITHUB_RAW_GETKEY = "https://raw.githubusercontent.com/tsanduongvi123/key-generator/main/get_key.py"

def download_get_key():
    print("[•] Kiểm tra file get_key.py ...")
    if not os.path.exists(GET_KEY_SCRIPT):
        try:
            print("[•] Tải get_key.py từ GitHub ...")
            r = requests.get(GITHUB_RAW_GETKEY, timeout=10)
            r.raise_for_status()
            with open(GET_KEY_SCRIPT, "w", encoding="utf-8") as f:
                f.write(r.text)
            print("[✓] Tải xong get_key.py.")
        except Exception as e:
            print("[X] Lỗi tải get_key.py:", e)
            sys.exit(1)

def run_get_key():
    ret = subprocess.call([sys.executable, GET_KEY_SCRIPT])
    if ret != 0:
        print("[X] Lỗi khi chạy get_key.py.")
        sys.exit(1)

def get_vip_keys_from_github():
    try:
        print("[•] Đang kiểm tra VIP key từ GitHub ...")
        response = requests.get(GITHUB_RAW_KEY, timeout=10)
        response.raise_for_status()
        data = json.loads(response.text)
        return data.get("vip_keys", [])
    except Exception as e:
        print("[X] Lỗi tải key:", e)
        return []

def is_valid_vip(user_key):
    vip_keys = get_vip_keys_from_github()
    return user_key in vip_keys

def main_menu():
    user_key = input("Nhập key của bạn: ").strip()
    print("\n[1] Chạy tool thường")
    print("[2] Chạy tool khác")
    print("[3] Chạy tool VIP")
    ch = input("\nChọn chức năng: ").strip()

    if ch == "3":
        if is_valid_vip(user_key):
            print("[✓] Key VIP hợp lệ. Đang chạy tool VIP...")
            # Gọi script hoặc tool VIP tại đây
        else:
            print("[X] Key không hợp lệ hoặc không phải VIP.")
            sys.exit(1)
    else:
        print("[•] Đang chạy tool thường ...")
        # Gọi tool thường ở đây

def main():
    download_get_key()
    run_get_key()
    print("\n[•] Đã xác thực key. Vào menu chính.\n")
    main_menu()

if __name__ == "__main__":
    main()
