from Setup import session, User

# 1. Crear un registro -  CREATE - INSERT
new_user = User(name="Raquel ", age=23)
# # Agregamos el registro
session.add(new_user)
session.commit()

# Verificar que el usuario (registro) a sido registrado
# Consulta de peticion READ
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age  FROM users
# WHERE users.name = %(name_1)s
#created_user =session.query(User).filter_by(name="Samuel").first()
print(f"Usuario creado: {new_user.name}, Edad: {new_user.age}")

# Agregar multiples usuarios
users_to_create = [
    User(name="Bob", age="30"),
    User(name="Maria", age="20"),
    User(name="Carlos", age="35"),
    User(name="Marcelo", age="12"),
]

session.add_all(users_to_create)
session.commit()

# Verificar los registros creados
all_users = session.query(User).all()
for user in all_users:
    print(f"Usuario: {user.name}, Edad: {user.age}")