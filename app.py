from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    domain = request.form["domain"]
    os.system(f"python3 subdomain_scanner.py {domain}")
    os.system(f"python3 dir_scanner.py {domain}")
    os.system("python3 generate_report.py")
    return "✅ Quá trình pentest hoàn tất. Kiểm tra pentest_report.txt"

if __name__ == "__main__":
    app.run(debug=True)
