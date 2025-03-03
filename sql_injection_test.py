import os

def check_sqli(url):
    print(f"🔍 Kiểm tra SQL Injection trên {url}")
    os.system(f"sqlmap -u '{url}' --batch --dbs > sql_results.txt")
    print("✅ Kết quả lưu vào sql_results.txt")

if __name__ == "__main__":
    url = input("Nhập URL cần kiểm tra: ")
    check_sqli(url)
