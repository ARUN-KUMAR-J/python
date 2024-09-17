tasks=[]
while(True):
    print("1.Add Task")
    print("2.Remove Task")
    print("3.List Tasks")
    print("4.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter task you want to add:")
        tasks.append(task)
    elif choice==2:
        task=input("Enter task you want to delete:")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")
    elif choice==3:
        for i in tasks:
            print(i)
    elif choice==4:
        break
    else:
        print("Invalid choice")