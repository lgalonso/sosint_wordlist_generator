import os
import argparse
from alive_progress import alive_bar
import time

parser = argparse.ArgumentParser(description='SOSINT Wordlist Generator is a project to creating social media user based dictionaries.')
parser.add_argument('-u','--username', help='This is help but not very helpful right now',required=False)
args = parser.parse_args()

target = "None"
urls = []
rules = []
selected_rules = []

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
    os.system("printf '\n\nUsing: '")
    os.system("sudo cewl -d 2 -m 8 -w " + n + "_" + target + "_temp.txt " + url)
    os.system("printf '\n\n\n'")

def create_temp_files():
    for index, url in enumerate(urls):
        print("\n\n")
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

def rules_menu():
    print("\n\n")
    print("1- Show hashcat rules.")
    print("2- Select rules.")
    print("3- Apply dictionary rules.")

def set_rules():
    global rules
    for file in os.listdir("/usr/share/hashcat/rules/"):
        if ".rule" in file:
            rules.append(file)

def show_rules():
    for index, rule in enumerate(rules):
        print(str(index) + ". " + rule + "\n")

def select_rules():
    global selected_rules
    input_rules = input("\nInput rule number or rules number separated by a comma ex: [1,1,1]: ")
    selected_rules = input_rules.split(',')
    print(selected_rules)

def apply_rules_to_wordlist():
    command = "hashcat --force " + target + "_wordlist.txt"
    rules_to_apply = ""
    for index, rule in enumerate(rules):
        if selected_rules.count(str(index)) > 0:
            rules_to_apply += " -r /usr/share/hashcat/rules/" + rule
    print("sudo bash -c '" + command + rules_to_apply + " --stdout > " + target + "_wordlist_with_rules.txt'")
    yield
    ##os.system("sudo bash -c '" + command + rules_to_apply + " --stdout > " + target + "_wordlist_with_rules.txt'")
    
def menu():
    print("\n\n")
    print("1- Get target socials. Powered by Sherlock.")
    print("2- Create target wordlist. Powered by CEWL.")
    print("3- Apply wordlist rules. Powered by hashcat.")

def clear_screen():
    os.system("clear")

def welcome():
    print("\n\n")
    print("SOSINT Wordlist Generator by [INSERT_CLEVER_NAME_HERE].")

def bye():
    print("\n\n")
    print("Bye Bye.")
    time.sleep(1)

def main():
    action = ""
    set_rules()
    clear_screen()
    welcome()
    while "q" not in action:
        menu()
        action = input("\nChoose action (write 'q' to exit): ")

        if "1" in action:
            search_target_socials(get_target_username())
            args.username = "None"

        elif "2" in action:
            print("\n\n2.")
            if target == "None":
                print("No target specified. Complete action 1.")
            else:
                set_target_file_urls(target + ".txt")
                with alive_bar(len(urls)) as bar:
                    for i in create_temp_files():
                        time.sleep(0.5)
                        bar()
                create_wordlist()

        elif "3" in action:
            rule_action = ""
            while "q" not in rule_action:
                rules_menu()
                rule_action = input("\nChoose action (write 'q' to go back): ")
                if "1" in rule_action:
                    show_rules()

                elif "2" in rule_action:
                    select_rules()

                elif "3" in rule_action:
                    with alive_bar(1) as bar:
                        for i in apply_rules_to_wordlist():
                            bar()
                
                elif 'q' in rule_action:
                    break
                          
        elif "q" in action:
            bye()
            break
        else:
            print(action)
            print("\n\nInvalid option.")

main()