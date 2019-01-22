# 4.Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login=(input("Enter your login: "))
while login == "First":
    print("Greetings, " + login)
    break
else:
    print("Login incorrect. Please, try again.")
