 ### **Ejercicio Integrado: Sistema de Gestión de Usuarios**
# El objetivo de este ejercicio es implementar un sistema básico de gestión de usuarios
# que permita realizar todas las operaciones CRUD.

# 1. **Crear usuarios**: Permitir agregar uno o más usuarios con validaciones básicas.
# 2. **Listar usuarios**: Mostrar todos los usuarios o filtrar por criterios específicos (por ejemplo, edad).
# 3. **Actualizar usuarios**: Modificar información de un usuario existente.
# 4. **Eliminar usuarios**: Eliminar usuarios individualmente o según un criterio.
# 5. **Validaciones**: Asegúrate de que los datos sean válidos antes de guardarlos en la base de datos.
# 6. **Reportes**: Generar un informe con el total de usuarios y el promedio de edades.

from Setup import session, User

# FUNCIONES CRUD
def create_users(users):
    try:
        session.add_all(users)
        session.commit()
        print("Usuarios creados exitosamente")
    except Exception as e:
        session.rollback()
        print(f"Error al crear usuarios: {e}")


def read_users(age_filter=None):
    if age_filter:
        users = session.query(User).filter(User.age > age_filter).all()
        print(f"Usuarios con edad mayor a {age_filter}")
    else:
        users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Nombre: {user.name}, Edad:{user.age}")


def update_user(user_id, new_name=None, new_age=None):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print(f"Usuario con Id: {user_id} no encontrado ")
        return
    if new_name:
        user.name = new_name
    if new_age:
        user.age = new_age
    session.commit()
    print(f"Usuario con Id: {user_id} actualizado")


def delete_users_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print(f"Usuaio con Id: {user_id} no encontrado ")
        return
    session.delete(user)
    session.commit()
    print(f"Usuario con Id {user_id} eliminado")


def report_users():
    total_users = session.query(User).count()
    if total_users == 0:
        print("No hay usuarios en la base de datos ")
        return
    avg_age = session.query(User.age).all()
    avg_age = sum(age[0] for age in avg_age) / total_users
    print(f"Total del usuarios: {total_users}")
    print(f"Edad primedio: {avg_age:.2f}")


# Simulacion de registro de usuarios
def main():
    # Crear usuarios
    print("Creando usuarios...")
    create_users(
        [
            User(name="Bob", age="30"),
            User(name="Maria", age="20"),
            User(name="Carlos", age="35"),
            User(name="Marcelo", age="12"),
        ]
    )

    # Lista de usuarios
    print("\n Listando usuarios...:")
    read_users()

    # Filtrar usuarios mayores a 25
    print("\n Listando usuarios mayores a 25...")
    read_users(age_filter=25)

    # Actualizar usuario
    print("\n Actualizando usuario con id 2")
    update_user(user_id=2, new_name="Ana", new_age=5)

    # Listar usuarios nuevamente
    print("\n Listando usuarios despues de la actualziacion...")
    read_users()

    # Eliminar un usuario
    print("\n Eliminando usuario con id 27")
    delete_users_by_id(user_id=27)

    # Generamos un reporte
    print("\n Generando reporte...")
    report_users()


if __name__ == "__main__":
    main()