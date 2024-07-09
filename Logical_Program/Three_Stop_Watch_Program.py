import time

def start():
    return time.time()

def stop():
    return time.time()

def elapsed_time(start_time, stop_time):
    return stop_time - start_time

if __name__ == '__main__':
    start_time = start()
    input("Press Enter to stop the stopwatch")
    stop_time = stop()
    print(f"Elapsed time: {elapsed_time(start_time, stop_time):.2f} seconds")

