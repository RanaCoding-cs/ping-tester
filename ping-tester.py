import os
import sys

# টার্মিনাল কালার কোড
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear')

def show_banner():
    clear_screen()
    print(f"{CYAN}==================================================")
    print(f"     ____ ___ _   _  ____   _____ _____ ____ _____ ")
    print(f"    |  _ \_ _| \ | |/ ___| |_   _| ____/ ___|_   _|")
    print(f"    | |_) | ||  \| | |  _    | | |  _| \___ \ | |  ")
    print(f"    |  __/ | || |\  | |_| |   | | | |___ ___) || |  ")
    print(f"    |_|   |___|_| \_|\____|   |_| |_____|____/ |_|  ")
    print(f"            Tier-2: Live Network Ping Tester")
    print(f"=================================================={RESET}")

def execute_ping(target_host):
    print(f"\n{YELLOW}[*] Sending ICMP Echo Request packets to '{target_host}'...{RESET}\n")

    # [!-- বাংলা কমেন্ট: লিনাক্স বা টারমাক্সের মেইন সিস্টেমে ৩টি পিং প্যাকেট পাঠানোর কাস্টম কমান্ড তৈরি --]
    # -c 3 মানে ৩টি প্যাকেট পাঠানো হবে যাতে টুলটি আটকে না থেকে দ্রুত রেজাল্ট দেয়
    command = f"ping -c 3 {target_host}"

    # [!-- বাংলা কমেন্ট: ওএস ডট সিস্টেম ব্যবহার করে টার্মিনালে সরাসরি পিং প্রসেস রান করা হচ্ছে --]
    response = os.system(command)

    print(f"\n{CYAN}--------------------------------------------------{RESET}")
    # [!-- বাংলা কমেন্ট: রেসপন্স যদি ০ আসে তার মানে পিং সফল হয়েছে এবং হোস্টটি লাইভ আছে --]
    if response == 0:
        print(f"{GREEN}[✓] Target Host '{target_host}' is ALIVE and responding!{RESET}")
    else:
        print(f"{RED}[!] Target Host '{target_host}' is DOWN or Unreachable!{RESET}")
    print(f"{CYAN}--------------------------------------------------{RESET}")

if __name__ == "__main__":
    while True:
        show_banner()
        print(f"{YELLOW}[+] Enter Website Domain or IP to Ping (e.g., google.com)")
        host_input = input(f"[+] Type 'exit' to close the tool: {RESET}").strip()

        if host_input.lower() == 'exit':
            print(f"\n{YELLOW}[*] Thank you for using Ping Tester! Goodbye.{RESET}\n")
            break

        if host_input:
            # [!-- বাংলা কমেন্ট: ইনপুট থেকে প্রোটোকল হেডার (http/https) থাকলে তা ট্রিম বা ক্লিন করা --]
            clean_host = host_input.replace("http://", "").replace("https://", "").replace("www.", "")
            execute_ping(clean_host)
        else:
            print(f"{RED}[!] Host input address cannot be empty!{RESET}")

        input(f"\n{CYAN}[Press Enter to test next host...]{RESET}")
