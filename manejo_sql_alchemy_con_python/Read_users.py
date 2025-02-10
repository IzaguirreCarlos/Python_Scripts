from Setup import session, User

# 3. LEER REGISTROS
# Operacion de filtrado
filtered_users = session.query(User).filter(User.age > 25).all()
print(" ! Usuarios mayores a 25....!")
for user in filtered_users:
    print(f"{user.name}, {user.age}")

# Operacion de filtrado por varios criterios
filtered_users2 = session.query(User).filter(User.age >= 20, User.age <= 30).all()
print("Usuarios entre 20 y 30......!")
for user in filtered_users2:
    print(f"{user.name}, {user.age}")

# Contar los registros
total_filtered_users = (
    session.query(User).filter(User.age >= 20, User.age <= 25).count()
)
print(f" ! Total de usuarios en la base de datos ..... :{total_filtered_users}")