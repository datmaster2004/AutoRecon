import os

def scan_subdomains(domain):
    print(f"🔍 Đang quét subdomains cho {domain}")
    os.system(f"subfinder -d {domain} -o subdomains.txt")
    print("✅ Kết quả lưu vào subdomains.txt")

if __name__ == "__main__":
    domain = input("Nhập domain: ")
    scan_subdomains(domain)
