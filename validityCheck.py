
from colorama import Fore , Style
class check_user_input():

    def __init__(self, value):
        self.value = value

    def check_user_input_number(self, bottom, top):

        type_check = False
        range_check = False

        if self.value == "q":
            exit(0)

        try:
            self.value = int(self.value)
            type_check = True
        except ValueError:
            print (f"{Fore.RED}type{Style.RESET_ALL} is not correct!")

        try: 
            if bottom <= self.value and self.value <= top:
                range_check = True
            else:
                print(f"Not in {Fore.RED}Range!{Style.RESET_ALL}")
        except TypeError:
            pass

        if type_check and range_check:
            return True
        else:
            print(f"Please try again or {Fore.RED}q to exit!{Style.RESET_ALL}-> ", end="")
            return False

    def check_user_input_string(self, max_len):

        type_check = False
        range_check = False

        if self.value == "q":
            exit(0)
        
        try:
            self.value = float(self.value)
            print (f"{Fore.RED}type{Style.RESET_ALL} is not correct!")
        except ValueError:
            type_check = True

        try: 
            if max_len >= len(self.value):
                range_check = True
            else:
                print("String is too long!")
        except TypeError:
            pass

        if type_check and range_check:
            return True
        else:
            print(f"Please try again or {Fore.RED}q to exit!{Style.RESET_ALL}-> ", end="")
            return False
    
    def check_user_input_yes_or_no(self, max_len):

        type_check = False
        range_check = False
        content_check = False
        val_to_return = "null"

        if self.value == "q":
            exit(0)
        
        try:
            self.value = float(self.value)
            print (f"do not enter {Fore.RED}digit!{Style.RESET_ALL}")
        except ValueError:
            type_check = True

        try: 
            if max_len >= len(self.value):
                range_check = True
            else:
                print("string is too long!")
        except TypeError:
            pass

        try:
            if self.value.lower() == "yes" or self.value.lower() == "y":
                content_check = True
                val_to_return = "yes"
            elif self.value.lower() == "no" or self.value.lower() == "n":
                content_check = True
                val_to_return = "no"
            else:
                content_check = False
                print(f"only {Fore.RED}yes, no, y and n{Style.RESET_ALL} is accepted!")
        except AttributeError:
            pass

        if type_check and range_check and content_check:
            return True, val_to_return
        else:
            print(f"Please try again or {Fore.RED}q to exit!{Style.RESET_ALL}-> ", end="")
            return False, val_to_return


