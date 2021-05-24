username = ["Ayyoob", "Abdul", "Nathan", "Matthew", "Zipho"]

password = ["0000", "5555", "7700", "1234", "9621"]

name = input("Enter Username: ")
pword = input("Enter Password: ")
find = False

for x in range(len(username)):
    if name == username[x] and pword == password[x]:
        find = True

if find == True:
    print("Access Granted!")

else:
    print("x Access Denied! x")
