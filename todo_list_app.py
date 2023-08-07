def add(todo):
    with open('todo.txt', 'a') as f:
        f.write(todo + '\n')

def show():
    with open('todo.txt', 'r') as f:
        print(f.read())

def delete(todo):
    with open('todo.txt', 'r') as f:
        lines = f.readlines()
    with open('todo.txt', 'w') as f:
        for line in lines:
            if line.strip('\n') != todo:
                f.write(line)

def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: python todo_list_app.py [add|show|delete] [task]")
        return

    keyword = sys.argv[1]
    task = sys.argv[2]

    if keyword == 'add':
        add(task)
    elif keyword == 'show':
        show()
    elif keyword == 'delete':
        delete(task)
    else:
        print('Invalid command')

if __name__ == "__main__":
    main()