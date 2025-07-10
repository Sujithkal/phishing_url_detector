import re

# Load URLs from file
def load_urls(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# Define phishing detection rules
def is_phishing(url):
    suspicious_keywords = ["login", "verify", "secure", "update", "bank", "account"]
    ip_pattern = r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    misspelled_domains = ["g00gle", "faceb00k", "paypa1", "amaz0n"]

    if re.search(ip_pattern, url):
        return True
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    if any(domain in url.lower() for domain in misspelled_domains):
        return True
    if len(url) > 75:
        return True
    return False

# Analyze URLs
def analyze_urls(urls):
    print("Phishing URL Report:")
    print("---------------------")
    for url in urls:
        if is_phishing(url):
            print(f"[⚠️] Suspicious: {url}")
        else:
            print(f"[✅] Safe: {url}")

# Main execution
if __name__ == "__main__":
    urls = load_urls("sample_urls.txt")
    analyze_urls(urls)
