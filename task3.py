u = "Lora"
users = {
    "u1":"Aleksey",
    "u2":"Kim",
    "u3":"Egor"
    "Lora"
}
users1 = {
    "u5":"Aleksey",
    "u6":"Kim",
    "u7":"Egor",
    "u8":"Denis"
}
print("Я ввожу 2 юзера, чтоб проверить, правильно ли выводит.")
print(users.get(u, "Всем привет"))
for k, s in users1.items():
    print(users1.get(u, f"Привет, {k}\n"))