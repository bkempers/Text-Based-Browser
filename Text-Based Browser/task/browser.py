# Text-Based Browser
# Author: Ben Kempers
# Version: December 30, 2021
#
# Simple course designed by JetBrains to better get an understanding of
# how Python works as a language and to develop a simple text-based browser
# based on key aspects of the Python language
#
import sys
import argparse
import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from colorama import Fore

parser = argparse.ArgumentParser(description="Input directory name to store website tabs.")
parser.add_argument("dir_name")
arg = parser.parse_args()

class TextBrowser():
    website_tabs = []
    last_website = ""
    website_num = 0

    # Creates new directory
    if not os.access(arg.dir_name, os.F_OK):
        os.mkdir(arg.dir_name)

    def __init__(self, omitted, url):
        self.omitted = omitted
        self.url = url

    # Function to check if the user input was a valid website, then writes and saves that
    # website to the given folder directory
    def website_input(self, input, domain):
        changed_input = input.split(".")
        changed_file_path = os.path.join(arg.dir_name, changed_input[0])

        if os.path.exists(changed_file_path):
            self.tab_input(path=changed_file_path)
        else:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)"
            }
            request = requests.get(input, headers=headers)
            if request.status_code == 200:
                url_soup = BeautifulSoup(request.content, "html.parser")

                for link in url_soup.find_all("a"):
                    link.string = "".join([Fore.BLUE, link.get_text(), Fore.RESET])

                with open(domain, 'w', encoding='utf-8') as file:
                    file.write(url_soup.get_text())
                    file.flush()

                with open(domain, 'r') as file:
                    print(file.read())

            else:
                print("error: input URL wasn't able to be requested from server.")

    # Function to check if the given website already has been saved to the given folder directory
    def tab_input(self, path):
        with open(path, 'r') as file:
            print(file.read())

    # Function to determine if the given website can be put into 'back' stack
    def check_back(self):
        if self.last_website != "":
            self.website_tabs.append(self.last_website)

    # Function to return last website (if there was one)
    def back_input(self):
        if len(self.website_tabs) != 0:
            print(self.website_tabs.pop())

    # 'Main' loop statement that will continuously allow users to input a valid website
    def start(self):
        while True:
            user_input = input()

            if user_input == "exit":
                sys.exit()
            elif user_input == "back":
                self.back_input()
            elif "." in user_input:
                self.website_num = self.website_num + 1

                if self.website_num >= 2:
                    self.check_back()

                if "https://" not in user_input:
                    user_input = "https://{website}".format(website=user_input)

                website_name = urlparse(user_input).netloc
                self.website_input(input=user_input, domain=website_name)
                self.last_website = website_name
            else:
                print("Incorrect URL")


while True:
    text_browser = TextBrowser("https://www.", '')
    text_browser.start()
