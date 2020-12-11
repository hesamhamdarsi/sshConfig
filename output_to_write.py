#!/bin/bash

import validityCheck
from colorama import Fore , Style

def return_output(my_input_file, mydict, item_to_change):
    list1 = []
    oldtext = ""
    text = ""
    print("")
    print(f"your selection is: {Fore.MAGENTA}{item_to_change}{Style.RESET_ALL}")
    print("")
    myfile = open(my_input_file, 'r+')
    result = False
    for lines in myfile.readlines():
        if lines.strip() == "":
            continue
        list1.append(lines.split())
        #print (list1[0])
        #print (mydict[item_to_change]['configs'])
        #print (lines)
        if list1[0] == mydict[item_to_change]['configs']:
            tick = True
            text = lines.lstrip()
            oldtext = lines
            #print (text)
            if text.startswith("#"):
                print(f"This feature is disabled/default value, do you want to enable it?{Fore.RED}(YES,NO or q to quit){Style.RESET_ALL}: ", end="")
                #check_answer_correctness
                while result == False:
                    user_input = input()
                    check_user_input = validityCheck.check_user_input(user_input)
                    result, answer = check_user_input.check_user_input_yes_or_no(3)
                if result==True and answer == "yes":
                    #remove # from text and save it
                    text = text.replace("#", "", 1)
                    result = False
                else:
                    print("you didn't enable this feature")
                    result = False
                    break
            else:
                print(f"This feature is enabled, do you want to disable it?{Fore.RED}(YES,NO or q to quit){Style.RESET_ALL}: ", end="")
                #check answer correctness
                while result == False:
                    user_input = input()
                    check_user_input = validityCheck.check_user_input(user_input)
                    result, answer = check_user_input.check_user_input_yes_or_no(3)
                #add # to the text and save it
                if result==True and answer == "yes":
                    text = "# "+text
                    result = False
                    break
                else:
                    result = False
                    print("you didn't disable this feature")
        
            ###############################################################################
            if text.rstrip().endswith("yes"):
                print(f"do you want to unset this? {Fore.RED}(YES,NO or q to quit){Style.RESET_ALL}: ", end="")
                while result == False:
                    user_input = input()
                    check_user_input = validityCheck.check_user_input(user_input)
                    result, answer = check_user_input.check_user_input_yes_or_no(3)
                if result==True and answer == "yes":
                #replace yes with no and save it
                    text = text.rsplit(' ', 1)[0]
                    text = text + " no"
                    result = False
                    tick = False
                    break
                else:
                    print("you didn't change this value")
                    result = False
                    break

            elif text.rstrip().endswith("no"):
                if tick:
                    print(f"do you want to set this?{Fore.RED}(YES,NO or q to quit){Style.RESET_ALL}: ", end="")
                    while result == False:
                        user_input = input()
                        check_user_input = validityCheck.check_user_input(user_input)
                        result, answer = check_user_input.check_user_input_yes_or_no(3)
                    if result==True and answer == "yes":
                        #replace no with yes and save it
                        text = text.rsplit(' ', 1)[0]
                        text = text + " yes"
                        result = False
                        break
                    else:
                        print("you didn't change this value")
                        result = False
                        break
                else:
                    continue
            else:
                #replace the value with use input
                if text.lstrip().startswith("#"):
                    print("this text starts with #")
                    continue
            ###########################################################
                else:
                    print (f"do you want to assign a new value to {item_to_change} ?{Fore.RED}(YES,NO or q to quit){Style.RESET_ALL}: ", end="")
                    while result == False:
                        user_input = input()
                        check_user_input = validityCheck.check_user_input(user_input)
                        result, answer = check_user_input.check_user_input_yes_or_no(3)
                    if result==True and answer == "yes":
                        print("enter the new value: ", end="")
                        user_input = input()
                        text = text.lstrip().split(' ',1)[0]
                        text = text + " " + user_input
                        result = False
                    else:
                        print("nothing to change!")
                        result = False
                    break
            list1 = []
        
        else:
            list1 = []
            pass

    myfile.close()
    return oldtext, text