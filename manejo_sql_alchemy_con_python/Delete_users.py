from Setup import session, User

# 4. ELIMINAR REGISTRO
user_to_delete = session.query(User).filter_by(name="Bob").first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"Usuario eliminado : {user_to_delete.name}")

# Eliminar registros con un criterio MAYOR A 25 age
users_to_delete = session.query(User).filter(User.age > 25).all()
for user in users_to_delete:
    session.delete(user)
session.commit()

# Verificar los cambios y los Usuarios Restantes
not_deleted_users = session.query(User).all()


for user in not_deleted_users:
    print(f"User: {user.name}, {user.age}")

not_deleted_users_count = session.query(User).count()
print(f"Usuarios restantes: {not_deleted_users_count}")