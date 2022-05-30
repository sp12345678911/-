tasks = {}
task = lambda f: tasks.setdefault(f.__name__, f)

@task
def p1():
    print("p1")

@task
def p2():
    print("p2")

def my_main(key):
    tasks[key]()
    
if __name__ == '__main__':
    my_main()