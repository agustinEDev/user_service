import unittest
from typing import Optional
from use_cases import FindUserUseCase, UserRepositoryInterface
from entities import User

class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {}

    def save(self, user: User) -> User:
        self.users[user._dni] = user
        return user

    def get(self, dni: str) -> User:
        return self.users.get(dni)

    def delete(self, dni: str) -> None:
        if dni in self.users:
            del self.users[dni]

    def list(self) -> list[User]:
        return list(self.users.values())
    
    def update(self, dni: str, new_username: str, new_last_name: str) -> Optional[User]:
        if not self.users.get(dni):
            return None
        # Crear nuevo objeto User (inmutabilidad)
        updated_user = User(new_username, new_last_name, dni)
        self.users[dni] = updated_user
        return updated_user
    
class TestFindUserUseCase(unittest.TestCase):
    def setUp(self):
        repository = InMemoryUserRepository()
        self.use_case = FindUserUseCase(repository)
    
    def test_find_existing_user(self):
        # 1. Crear y guardar un usuario
        user = User("Jane", "Doe", "87654321X")
        self.use_case.repository.save(user)
        # 2. Buscarlo con FindUserUseCase
        found_user = self.use_case.execute("87654321X")
        # 3. Verificar que es el correcto
        self.assertEqual(found_user._username, "Jane")
        self.assertEqual(found_user._lastname, "Doe")
        self.assertEqual(found_user._dni, "87654321X")

    def test_find_nonexistent_user(self):
        # 1. Buscar un DNI que no existe
        with self.assertRaises(ValueError):
            self.use_case.execute("00000000Y")

if __name__ == '__main__':
    unittest.main(verbosity=2)
