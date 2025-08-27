import time

input("Press Enter to start timing...") 
before = time.time()
input("Press Enter to end...")
after = time.time()

print(f"Elapsed time: {after - before} seconds")
