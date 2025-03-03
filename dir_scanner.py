import os

def scan_directories(domain):
    print(f"🔍 Đang dò tìm thư mục trên {domain}")
    os.system(f"gobuster dir -u {domain} -w /usr/share/wordlists/dirb/common.txt -o directories.txt")
    print("✅ Kết quả lưu vào directories.txt")

if __name__ == "__main__":
    domain = input("Nhập domain: ")
    scan_directories(domain)
