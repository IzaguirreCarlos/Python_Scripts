from Setup import session, User

# 3. ACTUALIZAR REGISTROS
user_to_update = session.query(User).filter_by(name="Carlos_1").first()
if user_to_update:
    user_to_update.age = 19  # actualizacion de edad (sobreescritura)
    session.commit()
    print(
        f"Usuario actualizado :{user_to_update.name}, Nueva edad :{user_to_update.age}"
    )

# Actualizacion de multiples registros - incrementar la edad para todos los usuarios en 1
users_to_update = session.query(User).all()
for user in users_to_update:
    user.age += 1
session.commit()

# Verificar los cambios
updated_users = session.query(User).all()
print("Usuarios actualizados:")
for user in updated_users:
    print(f"{user.name}, {user.age}")

# Manejar casos inexistentes - Intentar actualizar un usuario que NO EXISTA
#user_to_update = session.query(User).filter_by(name="NombreNoExista").first()

#if not user_to_update:
   # print("El usuario que intentas actualizar no existe ")