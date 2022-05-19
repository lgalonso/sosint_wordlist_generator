import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

def menu():
    print("\n\n")
    print("1- Test")

def welcome():
    print("\n\n")
    print("SOSINT Wordlist Generator by [INSERT_CLEVER_NAME_HERE].")

def bye():
    print("\n\n")
    print("Bye Bye.")

def main():
    print(args)
    action = ""
    welcome()
    while "quit" not in action:
        menu()
        action = input("Choose action (write 'quit' to exit): ")

        if "1" in action:
            print("This is a test")
        elif "quit" in action:
            bye()
        else:
            print("\n\nInvalid option.")

main()