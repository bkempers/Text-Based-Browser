# Text-Based Browser
# Author: Ben Kempers
# Version: December 21, 2021
#
# Simple course designed by JetBrains to better get an understanding of
# how Python works as a language and to develop a simple text-based browser
# based on key aspects of the Python language
#
import sys
import argparse
import os
import shutil

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

parser = argparse.ArgumentParser(description="Input directory name to store website tabs.")
parser.add_argument("dir_name")
arg = parser.parse_args()

class TextBrowser():
    # List of possible valid websites
    websites = {
        "bloomberg.com": bloomberg_com,
        "nytimes.com": nytimes_com
    }

    website_tabs = []
    last_website = ""
    website_num = 0

    def __init__(self, omitted, url):
        self.omitted = omitted
        self.url = url

    # Function to check if the user input was a valid website, then writes and saves that
    # website to the given folder directory
    def website_input(self, input):
        if input in self.websites:
            changed_input = input.split(".")
            file_path = os.path.join(arg.dir_name, changed_input[0])

            if os.path.exists(file_path):
                self.tab_input(input=changed_input[0])
            else:
                if input == "bloomberg.com":
                    print(bloomberg_com)
                elif input == "nytimes.com":
                    print(nytimes_com)

                with open(file_path, 'w') as file:
                    file.write(self.websites[input])
                file_path = changed_input[0]
                shutil.copy(file_path, arg.dir_name)
        else:
            print("error: website URL not Bloomberg.com or NYTimes.com")

    # Function to check if the given website already has been saved to the given folder directory
    def tab_input(self, input):
        file_path = os.path.join(arg.dir_name, input)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                print(file.read())

    # Function to determine if the given website can be put into 'back' stack
    def check_back(self, input):
        if self.last_website != "":
            self.website_tabs.append(self.last_website)

    # Function to return last website (if there was one)
    def back_input(self):
        if len(self.website_tabs) != 0:
            print(self.website_tabs.pop())

    # Creates new directory
    if not os.access(arg.dir_name, os.F_OK):
        os.mkdir(arg.dir_name)

    # 'Main' loop statement that will continuously allow users to input a valid website
    def start(self):
        while True:
            user_input = input()
            short_input = (user_input == "bloomberg") or (user_input == "nytimes")

            if user_input == "exit":
                sys.exit()
            elif user_input == "back":
                self.back_input()
            elif short_input or (user_input in self.websites):
                self.website_num = self.website_num + 1

                if self.website_num >= 2:
                    self.check_back(self.last_website)

                if short_input:
                    self.tab_input(input=user_input)
                    added_com = "{website}.com".format(website=user_input)
                    self.last_website = self.websites[added_com]
                else:
                    self.website_input(input=user_input)
                    self.last_website = self.websites[user_input]
            else:
                print("error: input isn't a valid URL or isn't a proper command")

while True:
    text_browser = TextBrowser("https://www.", '')
    text_browser.start()