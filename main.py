#!/bin/bash

import os
import modfile
import manualReader
import validityCheck
import output_to_write
from colorama import Fore , Style

mydict = {}

def get_dict_key(mydict, index_number):
    for key, _ in mydict.items():
        if str(index_number) == str(mydict[key]["index"]):
            return key

fgraber = modfile.fileGraber("/etc/ssh/ssh_config")
mylist = fgraber.freader()


def config_check():

    #print(mylist)
    i = 1
    indicator = False
    try:
        for item in mylist:
            val = item
            if val.strip() == "Host *":
                indicator = True
            if val[0] == "#" and indicator == True:
                temp = val.split()[1]
                if (temp) in mydict:
                    temp = (val.split()[1])+"(ExtraConfig-"+str(i)+")"
                mydict[temp] = {"configs" : val.split(), "index" : i}
                i += 1
            else:
                temp = val.split()[0]
                if indicator == True:
                    if (temp) in mydict:
                        temp = (val.split()[0])+"(ExtraConfig-"+str(i)+")"
                    mydict[temp] = {"configs" : val.split(), "index" : i} 
                    i += 1       
    except:
        print("finished")

    def show_configs():
        mystr = ""
        print('{0:3}|{1:30}|{2:61}|{3}'.format('index','Feature','value','Status'))
        print("--"*60)
        i = 1
        for key, value in mydict.items():
            index = mydict[key]['index']
            print('{0:<5}|'.format(index), end="")
            print("{0:<30}| ".format(key), end="")
            for items in value['configs']: 
                if items != "#" and items != key and (items+"(ExtraConfig-"+str(i)+")") != key:
                    mystr = mystr+" "+items
            print("{0:<60}| ".format(mystr), end="")
            mystr = ""
            if value['configs'][0] == "#":
                print("Not activated/Default")
            else:
                print("Activated")
            print("--"*60)
            i += 1
    show_configs()
    #print (mydict)


def user_manual():
    result = False
    config_check()
    user_input = ""
    print(f"press {Fore.RED}q to quit{Style.RESET_ALL} or enter {Fore.YELLOW}index number{Style.RESET_ALL} to see the manual of selected item{Fore.YELLOW}(e.g. 12){Style.RESET_ALL}: ", end="")
    while True:
        if result:
            os.system('clear')
            item_selected = get_dict_key(mydict, user_input)
            manualReader.manualreder("ssh_config",item_selected)
            result = False
            print(f"{Fore.GREEN}press any key to continue!{Style.RESET_ALL}", end="")
            input()
            config_check()
            print(f"press {Fore.RED}q to quit{Style.RESET_ALL} or enter index number to see the manual of selected item{Fore.YELLOW}(e.g. 12){Style.RESET_ALL}: ", end="")
        else:
            while result == False:
                user_input = input()
                isvalidate = validityCheck.check_user_input(user_input)
                result = isvalidate.check_user_input_number(1,len(mydict))
        

os.system("clear")
print('What kind of Operations do you need?:')
print("")
print(f'1-{Fore.RED}Checking{Style.RESET_ALL} a Config File')
print(f'2-{Fore.RED}Editing{Style.RESET_ALL} a Config File')
print("")
print("Answer: ", end="")
x = input()
if x == "1":
    #part1 -> show configs
    
    os.system("clear")
    print(f"Select the configuration file {Fore.RED}(default is ssh){Style.RESET_ALL}: ", end="")
    selected = input()
    os.system("clear")
    print(f"{Fore.RED}Notice!{Style.RESET_ALL}\nyou can select the index number of any config to see the related manual!")
    print("")
    print(f"{Fore.GREEN}press any key to continue!{Style.RESET_ALL}", end="")
    y = input()
    os.system("clear")
    print(f"{selected} config file......")
    print(f"{Fore.RED}Notice!{Style.RESET_ALL}\nyou can select the index number of any config to see the related manual!\n\n")
    user_manual()
    

elif x == "2":
    dic_chages = {}
    more_change = True
    i = 0
    os.system('sudo cp /etc/ssh/ssh_config ./ssh-config-file.txt')
    os.system('sudo chown $USER:$USER ssh-config-file.txt')
    os.system('chmod +x ssh-config-file.txt')
    print(f"you are about to change a config, please specify the config you want to chanage{Fore.RED}(default is ssh_config){Style.RESET_ALL}: ",end="")
    user_input = input()
    config_check()
    while more_change:
        print(f"Select the item that you want to edit {Fore.RED}(use the index number)!{Style.RESET_ALL} : ",end="")
        #user_input = input()
        result = False
        while result == False:
            user_input = input()
            isvalidate = validityCheck.check_user_input(user_input)
            result = isvalidate.check_user_input_number(1,len(mydict))
        item_to_change = get_dict_key(mydict,user_input)
 
        my_input_file = "ssh-config-file.txt"
        oldtext , newtext = output_to_write.return_output(my_input_file, mydict, item_to_change)
        res_old = oldtext.strip()
        res_new = newtext.strip()
        
        print("")
        print(f"the old config {Fore.GREEN}'{res_old}'{Style.RESET_ALL} will be converted to the new one {Fore.RED}'{res_new}'{Style.RESET_ALL}")
        
        dic_key = str(i)
        dic_chages[dic_key] = [oldtext , newtext]
        i += 1

        print("")
        print(f"More Change ????{Fore.RED}(yes/no){Style.RESET_ALL} : ",end="")
        result = False
        while result == False:
            user_input = input()
            check_user_input = validityCheck.check_user_input(user_input)
            result, answer = check_user_input.check_user_input_yes_or_no(3)
        if result==True and answer == "yes":
            continue
        else:
            result = False
            more_change = False
    
    os.system('clear')
    print ("changes are: ")
    print ("")
    for k,v in dic_chages.items():
        print (f"from '{Fore.GREEN}{v[0].strip()}{Style.RESET_ALL}'   to   '{Fore.MAGENTA}{v[1].strip()}{Style.RESET_ALL}'")
    
    print("")
    print(f"is it {Fore.GREEN}confirmed?{Style.RESET_ALL}{Fore.GREEN}(YES/NO or q to quit!) {Style.RESET_ALL}", end="")
    result = False
    while result == False:
        user_input = input()
        check_user_input = validityCheck.check_user_input(user_input)
        result, answer = check_user_input.check_user_input_yes_or_no(3)
    if result==True and answer == "yes":
        print("confirmed")
        write_changes = modfile.fileGraber(my_input_file)
        write_changes.fwriter(dic_chages , "edit")
    

