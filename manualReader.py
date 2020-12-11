#!/bin/bash
import os

def manualreder(manual_ref, word):
    manual_ref = 'man ' + manual_ref + '> manual.txt'
    os.system(manual_ref)
    file_manual = open("manual.txt")
    y = False
    for lines in file_manual.readlines():
        
        if lines.strip() == word and (len(lines.split())) == 1:
            print (lines.lstrip())
            y = True
            continue
        elif lines.lstrip().startswith(word+"  "):
            y = True
            print (lines.lstrip())
            continue
        else:
            lines.strip()
            pass
        if y == True:
            if (lines[0:6]) == " "*6:
                print(lines.lstrip())
            else:
                y = False

    file_manual.close()
