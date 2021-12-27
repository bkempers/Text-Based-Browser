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
import stat

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


def check_website_input(input):
    if input in websites:
        changed_input = input.split(".")
        file_path = os.path.join(arg.dir_name, changed_input[0])

        if os.path.exists(file_path):
            check_tab_input(input=changed_input[0])
        else:
            if input == "bloomberg.com":
                print(bloomberg_com)
            elif input == "nytimes.com":
                print(nytimes_com)

            with open(file_path, 'w') as file:
                file.write(websites[input])
            file_path = changed_input[0]
            shutil.copy(file_path, arg.dir_name)
    else:
        print("error: website URL not Bloomberg.com or NYTimes.com")


def check_tab_input(input):
    file_path = os.path.join(arg.dir_name, input)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print(file.read())


parser = argparse.ArgumentParser(description="Input directory name to store website tabs.")
parser.add_argument("dir_name")
arg = parser.parse_args()

# Creates new directory
if not os.access(arg.dir_name, os.F_OK):
    os.mkdir(arg.dir_name)

websites = {
    "bloomberg.com": bloomberg_com,
    "nytimes.com": nytimes_com
}

while True:
    user_input = input()

    if user_input == "exit":
        sys.exit()

    if user_input in websites:
        check_website_input(input=user_input)
    if input == "bloomberg" or input == "nytimes":
        check_tab_input(input=user_input)
    else:
        print("error: input isn't a proper URL or website tab.")
