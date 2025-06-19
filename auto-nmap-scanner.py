import os
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "\nWelcome to the Nmap Automated Scanner!\n")

ip = input(Fore.YELLOW + "Enter the Target IP Address: ")

def SYN_scan():
    print(Fore.GREEN + "[+] Starting SYN Scan...\n")
    os.system(f"nmap -sS -sV -v {ip}")
    print(Fore.GREEN + "[+] SYN Scan Completed.")

def aggressive_scan():
    print(Fore.GREEN + "[+] Starting Aggressive Scan...\n")
    os.system(f"nmap -A -v {ip}")
    print(Fore.GREEN + "[+] Aggressive Scan Completed.")

def no_ping_scan():
    print(Fore.GREEN + "[+] Starting No Ping Scan...\n")
    os.system(f"nmap -sV -Pn -v {ip}")
    print(Fore.GREEN + "[+] No Ping Scan Completed.")

def TCP_scan():
    print(Fore.GREEN + "[+] Starting TCP Scan...\n")
    os.system(f"nmap -sT -T1 -sV -v {ip}")
    print(Fore.GREEN + "[+] TCP Scan Completed.")

def UDP_scan():
    print(Fore.GREEN + "[+] Starting UDP Scan...\n")
    os.system(f"nmap -sU -sV -v {ip}")
    print(Fore.GREEN + "[+] UDP Scan Completed.")

def script_scan():
    print(Fore.GREEN + "[+] Starting Script Scan...\n")
    os.system(f"nmap -sV -sC -v {ip}")
    print(Fore.GREEN + "[+] Script Scan Completed.")

def custom_command():
    cmd = input(Fore.YELLOW + "Enter your custom Nmap command (without 'nmap'): ")
    print(Fore.GREEN + "[+] Running Custom Command...\n")
    os.system(f"nmap {ip} {cmd}")
    print(Fore.GREEN + "[+] Custom Scan Completed.")

# Show menu
print(Fore.CYAN + "\n---- Nmap Automated Script ----")
print("1. SYN scan")
print("2. Aggressive scan")
print("3. No ping Scan")
print("4. TCP scan")
print("5. UDP Scan")
print("6. Script Scan")
print("7. Custom Command")
print("8. Exit")

try:
    menu = int(input(Fore.YELLOW + "Select option: "))

    if menu == 1:
        SYN_scan()
    elif menu == 2:
        aggressive_scan()
    elif menu == 3:
        no_ping_scan()
    elif menu == 4:
        TCP_scan()
    elif menu == 5:
        UDP_scan()
    elif menu == 6:
        script_scan()
    elif menu == 7:
        custom_command()
    elif menu == 8:
        print(Fore.RED + "Exiting...")
    else:
        print(Fore.RED + "Invalid option! Please choose between 1-8.")
except ValueError:
    print(Fore.RED + "Please enter a valid number.")
