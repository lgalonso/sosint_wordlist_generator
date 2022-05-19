import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

target = "None"
urls = []

def get_target_username():
    target_username = args.username
    if target_username == "None":
        target_username = input("\nType the username of the target: ")
    target = target_username
    return target_username

def search_target_socials(target_username):
    os.system("sudo sherlock " + target_username + " --timeout 3")

def set_target_file_urls(target_file):
    os.system("sudo sed -i '$ d' " + target_file)
    with open(target_file, 'r') as file:
        urls = file.readlines()

def menu():
    print("\n\n")
    print("1- Get target socials. Powered by Sherlock.")
    print("2- Create target dictionary. Powered by CEWL.")
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
                set_target_file_urls(target + ".txt")

        if "3" in action:
            print("3.")
            
        elif "q" in action:
            bye()
        else:
            print("\n\nInvalid option.")

main()