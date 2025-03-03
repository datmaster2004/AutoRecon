import os

def check_xss(url):
    print(f"🔍 Kiểm tra XSS trên {url}")
    os.system(f"xsser -u '{url}' > xss_results.txt")
    print("✅ Kết quả lưu vào xss_results.txt")

if __name__ == "__main__":
    url = input("Nhập URL cần kiểm tra: ")
    check_xss(url)
