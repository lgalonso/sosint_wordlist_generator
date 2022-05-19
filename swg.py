from operator import index
import os
import argparse
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
    os.system("sudo cewl -d 2 -m 8 -w " + n + "_" + + target + "_temp.txt " + url)

def create_temp_files():
    for index, url in enumerate(urls):
        get_words_from_url(url, index)

def create_wordlist():
    os.system("sudo bash -c 'cat *_" + target * "_temp.txt >> " + target + "_wordlist.txt'")
    os.system("sudo rm *temp*")

def menu():
    print("\n\n")
    print("1- Get target socials. Powered by Sherlock.")
    print("2- Create target wordlist. Powered by CEWL.")
    print("3- Apply dictionary rules. Powered by crunh/hashcat.")

def welcome():
    print("\n\n")
    print("SOSINT Wordlist Generator by [INSERT_CLEVER_NAME_HERE].")

def bye():
    print("\n\n")
    print("Bye Bye.")

def main():
    action = ""
    welcome()
    while "q" not in action:
        menu()
        action = input("\nChoose action (write 'q' or 'exit' to exit): ")

        if "1" in action:
            search_target_socials(get_target_username())
            args.username = "None"

        if "2" in action:
            print("2.")
            if target == "None":
                print("No target specified. Complete action 1.")
            else:
                print(target)
                set_target_file_urls(target + ".txt")
                create_temp_files()

        if "3" in action:
            print("3.")
            
        elif "q" in action:
            bye()
        else:
            print(action)
            print("\n\nInvalid option.")

main()