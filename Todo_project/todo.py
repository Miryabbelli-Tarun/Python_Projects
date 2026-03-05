def add_task():
    task=input('Enter your task:')
    due_date=input('Enter due date(YY-MM-DD):')
    priority=input('Enter priority(High/Midium/low):')
    with open('tasks.txt',mode='a',newline='') as f:
        f.write(f"{task}   | {due_date} | {priority } |  pending.. \n")
    print('task added sucesfully')

def view_tasks():
    try:
        with open('tasks.txt',mode='r') as f:
            tasks=f.readlines()
            if not tasks:
                print('No tasks found\n')
                return
            print("\n---All Tasks-----\n")
            for i,task in enumerate(tasks,start=1):
                print(f'{i}.{task.strip()}')
            print()
                
    except FileNotFoundError :
        print('file not found')

def delete_task():
    try:
        with open('tasks.txt','r') as f:
            tasks=f.readlines()
        if not tasks:
            print('no tasks found')
            return
        view_tasks()
        num=int(input('Enter number to delete task:'))
        if num<0 or num>len(tasks):
            print('invalid number')
            return
        tasks.pop(num-1)
        with open('tasks.txt','w') as f:
            f.writelines(tasks)
        print('task delete succesfully')
    except FileNotFoundError:
        print('file not found')

def mark_complete():
    with open('tasks.txt',mode='r') as f:
        tasks=f.readlines()
    if not tasks:
        print('no tasks found')
        return
    view_tasks()
    num=int(input('Enter task number to mark as complete:'))
    if num<0 or num>len(tasks):
        print('Invalid choice')
        return
    task=tasks[num-1].strip().split('|')
    task[3]='completed'
    tasks[num-1]='|'.join(task)+'\n'
    with open('tasks.txt','w') as f:
        f.writelines(tasks)
    print('task is mark as completed')
    
def search_task():
    with open('tasks.txt',mode='r') as f:
        tasks=f.readlines()
    keyword=input('Enter keyword to serch task:').lower()
    found=False
    if not tasks:
        print('No tasks Found')
        return
    for task in tasks:
        if keyword in task.lower():
            print(task)
            found=True
    if not found:
        print('No task found')
            
def pending_tasks():
    pending_task=[]
    with open('tasks.txt','r') as f:
        tasks=f.readlines()
    if not tasks:
        print('no tasks found')
        return
    for task in tasks:
        if 'pending' in task:
            pending_task.append(task.strip())
    if not pending_task:
        print('No pending tasks')
        return
    for i in pending_task:
        print(i)
def completed_tasks():
    complted_task=[]
    with open('tasks.txt','r') as f:
        tasks=f.readlines()
    if not tasks:
        print('no tasks found')
        return
    for task in tasks:
        if 'completed' in task.lower():
            complted_task.append(task.strip())
    if not complted_task:
        print('No completed tasks')
        return
    for i in complted_task:
        print(i)

def main():
    while True:
        print('==================ToDo List============')
        print('1.add Task')
        print('2.view task')
        print('3.delete task')
        print('4.mark task as complete')
        print('5.search task')
        print('6.view pending tasks')
        print('7.view completed tasks')
        print('10.Exit')

        choice=input('Enter your choice:')
        match choice:
            case '1':
                add_task()
            case '2':
                view_tasks()
            case '3':
                delete_task()
            case '4':
                mark_complete()
            case '5':
                search_task()
            case '6':
                pending_tasks()
            case '7':
                completed_tasks()
            case '10':
                print('Good bye...')
                break
            case _:
                print('\n please enter valid choice')
if __name__=='__main__':
    main()