import os
import sys
import requests
import subprocess

GET_KEY_SCRIPT = "get_key.py"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/tsanduongvi123/key-generator/main/get_key.py"

def download_get_key():
    print("[•] Kiểm tra file get_key.py ...")
    if not os.path.exists(GET_KEY_SCRIPT):
        try:
            print("[•] Tải get_key.py từ GitHub ...")
            r = requests.get(GITHUB_RAW_URL, timeout=10)
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

def main():
    download_get_key()
    run_get_key()
    print("\n[•] Đã xác thực key, bạn có thể chạy các tool khác hoặc code chính tiếp theo.\n")

if __name__ == "__main__":
    main()
