def generate_report():
    with open("pentest_report.txt", "w") as report:
        report.write("🛡️ BÁO CÁO PENTEST 🛡️\n")
        report.write("\n🔍 Subdomains Found:\n")
        with open("subdomains.txt", "r") as f:
            report.write(f.read())

        report.write("\n🔍 Hidden Directories:\n")
        with open("directories.txt", "r") as f:
            report.write(f.read())

        report.write("\n🔍 SQL Injection Results:\n")
        with open("sql_results.txt", "r") as f:
            report.write(f.read())

        report.write("\n🔍 XSS Results:\n")
        with open("xss_results.txt", "r") as f:
            report.write(f.read())

    print("✅ Báo cáo được lưu vào pentest_report.txt")

if __name__ == "__main__":
    generate_report()
