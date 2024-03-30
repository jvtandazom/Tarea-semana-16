# Escritura de Archivo de Texto:

with open("my_notes.txt", "w") as file:
    file.write("Mis notas personales:\n")
    file.write("- Mi nombre es Jonathan Tandazo.\n")
    file.write("- Tengo 25 años de edad.\n")
    file.write("- Estudio en la mejor universidad del Ecuador.\n")

# Lectura de Archivo de Texto:

with open("my_notes.txt", "r") as file:
    print("Contenido del archivo my_notes.txt:")
    for line in file.readlines():
        print(line.strip())

