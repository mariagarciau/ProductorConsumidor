from queue import Queue
from threading import Thread
import time
from random import randint

# Crear cola
q = Queue(10)

def producer(name,lleno):

    """Productor"""

    count = 1 #mostrador

    while True:

        q.join() # Espera a task_done () para enviar una señal

        q.put(count)

        print(f"{name} está produciendo el bollo {count}")

        count+=1
        if count > lleno:
          break

def customer(name):

    """consumidor"""

    count = 1

    while True:

        baozi = q.get()

        print(f"El consumidor- {name} está comiendo el bollo {count}")

        count+=1

        q.task_done() # Envía una señal después de comer

        time.sleep(1)



if __name__ == '__main__':
    lleno=randint(1,10)
    t1 = Thread(target=producer,args=("Maestro Zhang",lleno))

    t2 = Thread(target=customer,args=("Xiaoming",))

    t1.start()

    t2.start()

   

