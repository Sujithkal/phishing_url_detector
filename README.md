# 🛡️ Phishing URL Detector

## 📄 Project Overview
This Python script analyzes a list of URLs and flags potentially malicious or phishing links using simple pattern matching and keyword detection.

## 🚀 Features
- Detects phishing URLs based on:
  - Use of IP addresses
  - Suspicious keywords (e.g., login, verify)
  - Misspelled brand names (e.g., g00gle, paypa1)
  - Excessively long URLs
- Prints a clear report of safe vs suspicious URLs

## 🧪 Sample URL Format
https://www.google.com
http://192.168.0.1/login
https://secure-login.paypa1.com
## 🛠️ How to Use

1. Clone or download the repository.
2. Ensure `sample_urls.txt` is in the same directory.
3. Run the script:
   ```bash
   python phishing_detector.py
