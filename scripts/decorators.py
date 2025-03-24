import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"{func.__name__} took {t2} seconds to execute.")
    return wrapper

@tictoc
def short_timer():
    time.sleep(1.65)
    print("Short timer finished.")

@tictoc
def long_timer():
    time.sleep(7)
    print("Long timer finished.")

short_timer()
long_timer()