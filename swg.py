import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

def get_target_username():
    target_username = args.username
    if target_username is "None":
        target_username = input("\nType the username of the target: ")
    return target_username

def get_target_socials(target_username):
    os.system("sudo sherlock " + target_username + " --timeout 3")

def menu():
    print("\n\n")
    print("1- Get target socials. Powered by Sherlock.")

def welcome():
    print("\n\n")
    print("SOSINT Wordlist Generator by [INSERT_CLEVER_NAME_HERE].")

def bye():
    print("\n\n")
    print("Bye Bye.")

def main():
    print(os.__version__, argparse.__version__, subprocess.__version__)
    action = ""
    welcome()
    while "q" not in action:
        menu()
        action = input("\nChoose action (write 'q' or 'exit' to exit): ")

        if "1" in action:
            get_target_socials(get_target_username())
        elif "q" in action:
            bye()
        else:
            print("\n\nInvalid option.")

main()