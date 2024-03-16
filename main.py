#!/usr/bin/python
# coding=utf-8
# Author github.com/Eltotiz

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import os
import fade

init()
naranja = "\x1b[38;2;255;165;0m" 
violeta = "\x1b[38;2;138;43;226m" 

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

banner = """
       *****************************************************************************
	████████  ██████  ██████  ███████ ███████  █████  ██████   ██████ ██   ██ 
	   ██    ██    ██ ██   ██ ██      ██      ██   ██ ██   ██ ██      ██   ██ 
	   ██    ██    ██ ██████  ███████ █████   ███████ ██████  ██      ███████ 
	   ██    ██    ██ ██   ██      ██ ██      ██   ██ ██   ██ ██      ██   ██ 
	   ██     ██████  ██   ██ ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ 
                              Created by github.com/eltotiz

	****************************************************************************"""


while True:
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    clear()
    print("Starting TORSEARCH...")
    api_url = "https://api.ipify.org?format=json"

    responseIP = session.get(api_url)
    clear()
    faded_text = fade.purplepink(banner)
    print(faded_text)
    print(Fore.LIGHTRED_EX + "   [!] SECRET IP >", responseIP.json()['ip'] + Fore.RESET)
    search = input(violeta + "   [TORSEARCH] > ")
    print("")
    url = f"http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P={search}"


    response = session.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    td_elements = soup.find_all('td')

    for td in td_elements:
        for small_tag in td.find_all('small'):
            if 'matching' in small_tag.text:
                small_tag.extract()

        url_element = td.find('a')
        if url_element:
            url = url_element.get('href')
            description = td.text.strip()
            print(Fore.GREEN + "[URL]", f"{url}" + Style.RESET_ALL)
            print(naranja + "[DESCRIPTION]", f"{description}" + Style.RESET_ALL)
            print()

    print()
    print(violeta + " [?] Press enter to start a new search. ")
    input()  
