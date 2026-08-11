# simple CLI TO_DO mini project

tasks=[]

def add_task():
   task=input("Enter Task: ")
   tasks.append(task)
   save_tasks()
   print("Task added! ")

def view_tasks():
   if len(tasks) == 0:
      print("There is no task! ")

   else:
      for i in range(len(tasks)):
         print(str(i + 1) + "." + tasks[i])

def delete_task():
   view_tasks()
   if len(tasks) == 0:
      return
   num=int(input("which task to delete....!"))
   tasks.pop(num-1)
   save_tasks()
   print("task deleted!")

def save_tasks():
   with open("todo.txt", "w") as file:
      for task in tasks:
         file.write(task + "\n")
def load_tasks():
   try:
      with open("todo.txt", "r") as file:
         for line in file:
            tasks.append(line.strip())   # strip() removes the "\n" at the end
   except FileNotFoundError:
      pass   # if file doesn't exist yet, just start with an empty list       


load_tasks()
while True:
   print("\n1. Add Task")
   print("2. View Task")
   print("3. Delete Task")
   print("4 Exit")

   choice = input("Choose an option:  ")

   if choice == "1":
      add_task()
   elif choice == "2":
      view_tasks()
   elif choice == "3":
      delete_task()
   elif choice == "4":
      print("Task over............!")
      break
   else:
      print("Wrong Option...")
      
    
    
  