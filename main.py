# main.py
import requests

def main():
    response = requests.get("https://httpbin.org/get")
    print("Status:", response.status_code)
    print("Data:", response.json())

if __name__ == "__main__":
    main()