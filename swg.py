import os
import argparse
from alive_progress import alive_bar
import time
import subprocess

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

target = "None"
urls = []

def get_target_username():
    global target
    target_username = args.username
    if target_username == "None":
        target_username = input("\nType the username of the target: ")
    target = target_username
    return target_username

def search_target_socials(target_username):
    os.system("sudo sherlock " + target_username + " --timeout 3")

def set_target_file_urls(target_file):
    global urls
    os.system("sudo sed -i '$ d' " + target_file)
    with open(target_file, 'r') as file:
        urls = file.read().splitlines()
    
def get_words_from_url(url, n):
    os.system("printf '\n\n")
    os.system("sudo cewl -d 2 -m 8 -w " + n + "_" + target + "_temp.txt " + url)
    os.system("printf '\n\n\n'")

def create_temp_files():
    for index, url in enumerate(urls):
        print("Visiting: " + url)
        get_words_from_url(url, str(index))
        yield

def create_wordlist():
    os.system("sudo bash -c 'cat *_temp.txt >> " + target + "_wordlist.txt'")
    clean_wordlist()

def clean_wordlist():
    command = "sort " + target + "_wordlist.txt | uniq -u | tee " + target + "_wordlist.txt"
    os.system("sudo rm *temp*")
    os.system("sudo bash -c '" + command + "'")

def menu():
    print("\n\n")
    print("1- Get target socials. Powered by Sherlock.")
    print("2- Create target wordlist. Powered by CEWL.")
    print("3- Apply dictionary rules. Powered by crunch/hashcat.")

def clear_screen():
    os.system("clear")

def welcome():
    print("\n\n")
    print("SOSINT Wordlist Generator by [INSERT_CLEVER_NAME_HERE].")

def bye():
    print("\n\n")
    print("Bye Bye.")

def main():
    action = ""
    clear_screen()
    welcome()
    while "q" not in action:
        menu()
        action = input("\nChoose action (write 'q' or 'exit' to exit): ")

        if "1" in action:
            search_target_socials(get_target_username())
            args.username = "None"

        if "2" in action:
            print("\n\n2.")
            if target == "None":
                print("No target specified. Complete action 1.")
            else:
                set_target_file_urls(target + ".txt")
                with alive_bar(len(urls)) as bar:
                    for i in create_temp_files():
                        time.sleep(1)
                        bar()
                create_wordlist()

        if "3" in action:
            print("\n\n3.")
            
        elif "q" in action:
            bye()
        else:
            print(action)
            print("\n\nInvalid option.")

main()