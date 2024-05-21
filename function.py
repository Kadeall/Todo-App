def opening_files(filepath = 'shakur.txt'):
   with open(filepath,'r') as file_local:
            todos_local = file_local.readlines()
   return todos_local  


def write_todos(todos_arg, filepath = 'shakur.txt'):
     with  open(filepath, 'w') as file:
         file.writelines(todos_arg)



if __name__ == '__main__' :
       print("Hello there")
       print(opening_files())