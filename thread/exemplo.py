import threading
import time
import random

def func_thread(name, sleep):
    while True:
        print(f'Executando a thread {name}')
        time.sleep(sleep)

class MyThread(threading.Thread):
    def __init__(self, name, sleep):
        super().__init__()
        self.name  = name
        self.sleep = sleep

    def run(self):
        while True:
            print(f'Executando a thread {self.name}')
            time.sleep(self.sleep)

if __name__ == '__main__':
    sleeps = [1,2,3,4,5]
    names  = ['A','B','C','D']
    ts = []
    for _ in range(4):
        tmp = threading.Thread(target=func_thread,args=(names[_],random.choice(sleeps)),daemon=True)
        tmp.start()
        ts.append(tmp)
    
    my_t = MyThread('JACA',0.5)
    my_t.start()
    ts.append(my_t)


    #for t in ts:
    #    t.join()

    while True:
        i = 1






