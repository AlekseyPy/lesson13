print("We have programmists like: Ada Lavleys, Mark Cukerberg, Gvido Van Rosum, Margaret Hifild")
n = input("Name of programmist: ")
programists = {
    "Ada Lavleys":"10/12/1895",
    "Mark Cukerberg":"14/05/1984",
    "Gvido Van Rosum":"31/01/1956",
    "Margaret Hifild":"17/08/1946"
} 
print(programists.get(n, "Not found"))
