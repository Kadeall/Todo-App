
import function
           
while True:
   user_action = input("add,show,edit,complete or exit:")
   user_action = user_action.strip()
   
   if user_action.startswith('add'):
      todo = user_action[4:]

      ''' file = open('kadil.txt','r')
      todos = file.readlines()
      file.close()
      '''
      todos = function.opening_files()

      todos.append(todo + "\n")
      '''
      file = open('shakur.txt', 'w')
      file.writelines(todos)
      file.close()
      '''
      function.write_todos(todos)

   elif user_action.startswith('show'):
      ''' file = open('shakur.txt','r')
      todos = file.readlines()
      file.close() '''
      todos = function.opening_files()
      for index, items in enumerate(todos):
         items = items.strip('\n')
         rows = f"{index + 1 }.{items.title()}"
         print(rows) 

   elif user_action.startswith('edit'):
      try:
         number = int(user_action[5:])
         number = number - 1
         todos = function.opening_files()
         new_todo = input("Enter a new todo:")
         todos[number] = new_todo + "\n"
         function.write_todos(todos)
      except ValueError:
         print("Enter th rght command: ")   
         continue

   elif user_action.startswith('complete'):
      try:   
         number =int(user_action[9:])
         todos = function.opening_files()
         index = number - 1
         todo_to_be_removed = todos[index].strip('\n')
         todos.pop(number - 1)
         function.write_todos(todos)
         message = f"the todo {todo_to_be_removed} is completed and removed" 
         print(message)
      except IndexError:
         print("There is no item with that number:")
         continue 
      

   elif user_action.startswith('exit'):  
         break