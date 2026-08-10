# config files store settings
# log files store activity records

# program 1
# writing a simple config file

config = open("config.txt", "w")

config.write("username=admin\n")
config.write("password=1234\n")
config.write("theme=dark\n")

config.close()

print("Config file created")


# program 2
# reading config file

config = open("config.txt", "r")

print("\nReading Config File:\n")

for line in config:
    print(line.strip())

config.close()


# program 3
# writing logs (like real applications)

log = open("app_log.txt", "a")

import datetime

time = datetime.datetime.now()

log.write(f"{time} - User logged in\n")
log.write(f"{time} - Performed action: File opened\n")

log.close()

print("\nLog file updated successfully")