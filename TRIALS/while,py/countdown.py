# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")

logs = [
"INFO: Starting process",
"WARNING: Low memory",
"ERROR: Unable to connect to server",
"CRITICAL: System failure",
"INFO: Process completed"
] 
for log in logs:
   if "CRITICAL" in log:
          print(f"Critical log found: {log}")
# Exit the loop after finding the critical error
   elif "WARNING" in log:
    continue # Skip warnings
   elif "INFO" in log:
    pass # Do nothing for info logs
else:
    print(f"Log entry: {log}")