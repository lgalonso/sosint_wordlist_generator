import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

def get_target_username():
    target_username = args.username
    if target_username == "None":
        target_username = input("\nType the username of the target: ")
    return target_username

def get_target_socials(target_username):
    os.system("sudo sherlock " + target_username + " --timeout 3")

def get_target_file_urls(target_file):
    urls = []
    ##os.system("sudo sed -i '$ d' " + target_file)
    with open(target_file, 'r') as file:
        lines = len(file.readlines())
        print('Total lines:', lines)
        for line in file:
            urls.append(line.strip().split())
        print(urls)

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
    action = ""
    welcome()
    while "q" not in action:
        menu()
        action = input("\nChoose action (write 'q' or 'exit' to exit): ")

        if "1" in action:
            get_target_socials(get_target_username())
            
        elif "q" in action:
            get_target_file_urls("IbaiLlanos.txt")
            bye()
        else:
            print("\n\nInvalid option.")

main()