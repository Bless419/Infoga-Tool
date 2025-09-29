#!/usr/bin/env python3
import os
import sys
import json
import requests
from time import sleep

# Color codes
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear():
    os.system('clear')

def banner():
    print(f"""{C}{BOLD}
    ╔═══════════════════════════════════════╗
    ║ 🐙 {G}Created by: {W}Agent Security{C}       ║
    ║                                       ║
    ║        {M}INFO{C}GATHER {W}v1.0{C}              ║
    ║   {Y}Information Gathering Tool{C}          ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    {RESET}""")

def menu():
    print(f"{G}{BOLD}[1]{RESET} {W}Phone Number Lookup{RESET}")
    print(f"{G}{BOLD}[2]{RESET} {W}Social Media Username Search{RESET}")
    print(f"{G}{BOLD}[3]{RESET} {W}Geo-IP Location Lookup{RESET}")
    print(f"{G}{BOLD}[0]{RESET} {R}Exit{RESET}\n")

def phone_lookup():
    clear()
    banner()
    print(f"{Y}{BOLD}[*] Phone Number Lookup{RESET}\n")
    
    phone = input(f"{C}Enter phone number (with country code, e.g., +1234567890): {RESET}").strip()
    
    if not phone:
        print(f"{R}[!] Invalid input{RESET}")
        sleep(2)
        return
    
    print(f"\n{Y}[*] Searching for information...{RESET}\n")
    sleep(1)
    
    try:
        # Using numverify API
        api_key = "0174359e644a8ddb97c5869f7ddf0173"
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('valid'):
            print(f"{G}[✓] Valid Phone Number{RESET}\n")
            print(f"{C}[+] Phone Number:{RESET} {data.get('number', 'N/A')}")
            print(f"{C}[+] Local Format:{RESET} {data.get('local_format', 'N/A')}")
            print(f"{C}[+] International Format:{RESET} {data.get('international_format', 'N/A')}")
            print(f"{C}[+] Country:{RESET} {data.get('country_name', 'N/A')}")
            print(f"{C}[+] Country Code:{RESET} {data.get('country_code', 'N/A')}")
            print(f"{C}[+] Country Prefix:{RESET} {data.get('country_prefix', 'N/A')}")
            print(f"{C}[+] Location:{RESET} {data.get('location', 'N/A')}")
            print(f"{C}[+] Carrier:{RESET} {data.get('carrier', 'N/A')}")
            print(f"{C}[+] Line Type:{RESET} {data.get('line_type', 'N/A')}")
            
            # Generate map link if location available
            location = data.get('location', '')
            country = data.get('country_name', '')
            if location and country:
                map_query = f"{location}, {country}".replace(' ', '+')
                map_link = f"https://www.google.com/maps/search/{map_query}"
                print(f"{C}[+] Map Link:{RESET} {B}{map_link}{RESET}")
            elif country:
                map_query = country.replace(' ', '+')
                map_link = f"https://www.google.com/maps/search/{map_query}"
                print(f"{C}[+] Map Link:{RESET} {B}{map_link}{RESET}")
        else:
            print(f"{R}[✗] Invalid Phone Number{RESET}")
            if 'error' in data:
                print(f"{Y}[!] Error: {data['error'].get('info', 'Unknown error')}{RESET}")
        
    except Exception as e:
        print(f"{R}[!] Error: {str(e)}{RESET}")
    
    input(f"\n{G}Press Enter to continue...{RESET}")

def username_search():
    clear()
    banner()
    print(f"{Y}{BOLD}[*] Social Media Username Search{RESET}\n")
    
    username = input(f"{C}Enter username to search: {RESET}").strip()
    
    if not username:
        print(f"{R}[!] Invalid input{RESET}")
        sleep(2)
        return
    
    print(f"\n{Y}[*] Searching across platforms...{RESET}\n")
    
    platforms = {
        'Instagram': f'https://www.instagram.com/{username}/',
        'Twitter/X': f'https://twitter.com/{username}',
        'GitHub': f'https://github.com/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'YouTube': f'https://www.youtube.com/@{username}',
        'Facebook': f'https://www.facebook.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'Pinterest': f'https://www.pinterest.com/{username}',
        'Snapchat': f'https://www.snapchat.com/add/{username}'
    }
    
    found = []
    not_found = []
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                status = f"{G}[✓] Found{RESET}"
                found.append((platform, url))
            else:
                status = f"{R}[✗] Not Found{RESET}"
                not_found.append(platform)
            
            print(f"{C}{platform:15}{RESET} {status}")
            sleep(0.3)
            
        except:
            print(f"{C}{platform:15}{RESET} {Y}[?] Could not check{RESET}")
            sleep(0.3)
    
    if found:
        print(f"\n{G}{BOLD}Found on {len(found)} platform(s):{RESET}")
        for platform, url in found:
            print(f"  {M}•{RESET} {platform}: {B}{url}{RESET}")
    
    input(f"\n{G}Press Enter to continue...{RESET}")

def geoip_lookup():
    clear()
    banner()
    print(f"{Y}{BOLD}[*] Geo-IP Location Lookup{RESET}\n")
    
    ip = input(f"{C}Enter IP address (or press Enter for your IP): {RESET}").strip()
    
    print(f"\n{Y}[*] Fetching location data...{RESET}\n")
    sleep(1)
    
    try:
        if ip:
            url = f"http://ip-api.com/json/{ip}"
        else:
            url = "http://ip-api.com/json/"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"{C}[+] IP Address:{RESET} {data.get('query', 'N/A')}")
            print(f"{C}[+] Country:{RESET} {data.get('country', 'N/A')}")
            print(f"{C}[+] Country Code:{RESET} {data.get('countryCode', 'N/A')}")
            print(f"{C}[+] Region:{RESET} {data.get('regionName', 'N/A')}")
            print(f"{C}[+] City:{RESET} {data.get('city', 'N/A')}")
            print(f"{C}[+] ZIP Code:{RESET} {data.get('zip', 'N/A')}")
            print(f"{C}[+] Latitude:{RESET} {data.get('lat', 'N/A')}")
            print(f"{C}[+] Longitude:{RESET} {data.get('lon', 'N/A')}")
            print(f"{C}[+] Timezone:{RESET} {data.get('timezone', 'N/A')}")
            print(f"{C}[+] ISP:{RESET} {data.get('isp', 'N/A')}")
            print(f"{C}[+] Organization:{RESET} {data.get('org', 'N/A')}")
            print(f"{C}[+] AS:{RESET} {data.get('as', 'N/A')}")
        else:
            print(f"{R}[!] Failed to retrieve location data{RESET}")
            
    except Exception as e:
        print(f"{R}[!] Error: {str(e)}{RESET}")
    
    input(f"\n{G}Press Enter to continue...{RESET}")

def main():
    while True:
        clear()
        banner()
        menu()
        
        choice = input(f"{C}Select an option: {RESET}").strip()
        
        if choice == '1':
            phone_lookup()
        elif choice == '2':
            username_search()
        elif choice == '3':
            geoip_lookup()
        elif choice == '0':
            clear()
            print(f"{G}Thank you for using InfoGather!{RESET}")
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid choice{RESET}")
            sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrupted by user{RESET}")
        sys.exit(0)
