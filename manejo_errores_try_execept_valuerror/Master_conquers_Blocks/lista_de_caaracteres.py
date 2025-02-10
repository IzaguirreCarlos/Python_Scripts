frutas = (["mango","cereza","frambueza"])

print("___________")

for fruta in frutas:
    print(f"fruta {fruta}. longitud {len(fruta)}")

frutas.remove("mango")
print(frutas)

frutas.clear()
print(frutas)