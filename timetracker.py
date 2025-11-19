import time

input("Press Enter to start timing...") 
before = time.time()

input("Press Enter to end timing...")
after = time.time()

print(f"Elapsed time: {round(after - before, 2)} seconds")