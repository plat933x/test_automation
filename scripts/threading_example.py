''' threading training'''

import threading, time

def walk_dog_out(dog_name):
    time.sleep(4)
    print(f"Func 1): Walk the {dog_name} dog outside.")

def thrash_out():
    time.sleep(3)
    print("Func 2): Take out the trash!")

def get_email():
    time.sleep(1)
    print("Func 3): Read your new e-mail.")

''' In this way of running functions, 3 functions are being executed on the same thread
They have to be executed one by one in an order.'''

walk_dog_out("Azor")
thrash_out()
get_email()

print("Break between running functions...")
for i in range(5,0,-1):
    time.sleep(1)
    print(f"...{i}...")
    i-=1

'''try threading module to run it in a different order'''

chore1 = threading.Thread(target=get_email())
chore1.start()

chore2 = threading.Thread(target=thrash_out())
chore2.start()

chore3 = threading.Thread(target=walk_dog_out("Azor"))
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores completed")