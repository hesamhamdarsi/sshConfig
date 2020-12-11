from io import UnsupportedOperation
"""
grab a file, read that and return string
"""
class fileGraber():
    def __init__(self, anyfile):
        self.anyfile = anyfile
    
    def freader(self):
        try:
            mylist = []
            myfile = open(self.anyfile,"r")
            for lines in myfile.readlines():
                if lines.strip() != "":
                    mylist.append(lines.strip())
            return mylist
        except UnsupportedOperation:
            print("you don't have permission to read the file")
        finally:
            myfile.close()
    """
    fweiter(str, operation[write|append|edit])
    """
    def fwriter(self, mydic, operation):
        op = 'r+'
        if operation == "append": 
            op = 'a+'
        else: 
            pass
        if operation == "edit":
            try:
                for _,v in mydic.items():
                    with open(self.anyfile, op) as myfile:
                        temp = myfile.readlines()
                        myfile.seek(0)             
                        for i in temp: 
                            if i != v[0]:
                                myfile.write(i)
                            else:
                                myfile.write(v[1]+"\n")
                        myfile.truncate()
                    myfile.close()
            except UnsupportedOperation:
                print("you don't have permission to write/chage the file")
            except ValueError:
                print("Only write and append is accepted!")
            finally:
                myfile.close()

"""
        try:
            myfile = open(self.anyfile, op)
            myfile.write('xxxxxxx')
            myfile.close()
        except UnsupportedOperation:
            print("you don't have permission to write/chage the file")
        except ValueError:
            print("Only write and append is accepted!")
        finally:
            myfile.close()
"""

    
