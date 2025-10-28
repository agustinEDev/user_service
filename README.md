# 🏗️ Users Service - Clean Architecture

> Sistema de gestión de usuarios implementado con **Clean Architecture** en Python, diseñado para demostrar principios de diseño limpio y desarrollo orientado a pruebas.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-17%2F17%20✅%20Passing-green.svg)](#testing)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean-brightgreen.svg)](#arquitectura)
[![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](#testing)

## 📚 ¿Qué es Clean Architecture?

Clean Architecture separa el código en **capas concéntricas** donde las dependencias apuntan hacia el centro, garantizando que la lógica de negocio sea independiente de frameworks y tecnologías externas.

```
┌─────────────────────────────────────────────────────────┐
│               🌐 External (JSON Files)                  │
│  ┌─────────────────────────────────────────────────┐    │
│  │          🔌 Adapters (Repositories)             │    │
│  │  ┌─────────────────────────────────────────┐    │    │
│  │  │          💼 Use Cases (Business Logic)  │    │    │  
│  │  │  ┌─────────────────────────────────┐    │    │    │
│  │  │  │      🎯 Entities (User)         │    │    │    │
│  │  │  └─────────────────────────────────┘    │    │    │
│  │  └─────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

## 📚 ¿Qué hace este proyecto?

Este proyecto implementa un **sistema de gestión de usuarios** completo siguiendo los principios de Clean Architecture. Permite crear, buscar, listar, actualizar y eliminar usuarios con validación de DNI español.

### ✨ Características principales

- 🎯 **Entidad User** con validación completa de DNI español
- 💼 **5 casos de uso CRUD** completamente implementados
- 🔌 **Repositorio de archivos** con persistencia en JSON
- 🧪 **17 tests unitarios** con cobertura completa
- � **Aplicación CLI funcional** lista para usar
- 📝 **Documentación completa** y script de desarrollo

## 📁 Estructura del Proyecto

```
users_service/
├── 📜 scripts/
│   └── dev.py                    # 🛠️ Script de desarrollo y testing
├── 🎯 entities/
│   └── users.py                  # Entidad User con validación DNI
├── 💼 use_cases/
│   ├── user_repository_interface.py  # Interface del repositorio
│   ├── create_user_use_case.py       # Crear usuario
│   ├── find_user_use_case.py         # Buscar usuario por DNI
│   ├── list_users_use_case.py        # Listar todos los usuarios
│   ├── update_user_use_case.py       # Actualizar usuario
│   └── delete_user_use_case.py       # Eliminar usuario
├── � adapters/
│   └── repositories/
│       ├── file_user_repository.py   # Repositorio con persistencia JSON
│       └── database_user_repository.py # (Preparado para BD)
├── 🌐 external/
│   └── database/                     # (Configuración futura de BD)
├── 🧪 tests/
│   ├── test_entities/               # Tests de entidades
│   ├── test_use_cases/              # Tests de casos de uso
│   └── test_adapters/               # Tests de adaptadores
├── 🚀 main.py                       # Aplicación principal CLI
├── � users.json                    # Archivo de datos de usuarios
└── 📖 README.md                     # Esta documentación
```

## 🚀 Cómo usar el proyecto

### 🛠️ Ejecución del script de desarrollo
```bash
# Ejecutar validaciones completas y todos los tests
python scripts/dev.py
```

### 🎮 Ejecución de la aplicación
```bash
# Ejecutar la aplicación principal
python main.py
```

### 🧪 Ejecutar tests manualmente
```bash
# Ejecutar todos los tests
python -m unittest discover tests -v

# Ejecutar tests específicos
python -m unittest tests.test_entities.test_user -v
python -m unittest tests.test_use_cases.test_create_user_use_case -v
```

## 🎯 Funcionalidades del Sistema
- **Aplicación CLI funcional** lista para usar

### 🎯 **Gestión de Usuarios Completa**

1. **➕ Crear Usuario**
   ```python
   create_user = CreateUserUseCase(repository)
   user = create_user.execute("Juan", "Pérez", "12345678Z")
   ```

2. **🔍 Buscar Usuario por DNI**
   ```python
   find_user = FindUserUseCase(repository)
   user = find_user.execute("12345678Z")
   ```

3. **📋 Listar todos los Usuarios**
   ```python
   list_users = ListUsersUseCase(repository)
   users = list_users.execute()
   ```

4. **✏️ Actualizar Usuario**
   ```python
   update_user = UpdateUserUseCase(repository)
   user = update_user.execute("12345678Z", "Juan Carlos", "Pérez López")
   ```

5. **🗑️ Eliminar Usuario**
   ```python
   delete_user = DeleteUserUseCase(repository)
   delete_user.execute("12345678Z")
   ```

### 🛡️ **Validación de DNI Español**
El sistema incluye validación completa del DNI español:
- ✅ Formato correcto (8 números + 1 letra)
- ✅ Algoritmo de verificación oficial
- ✅ Cálculo automático de la letra de control

## 🧪 Testing

El proyecto incluye una suite completa de 17 tests unitarios:

```bash
# Ejecutar todos los tests
python scripts/dev.py

# Output esperado:
# ✅ 17/17 tests passed
# 🎉 ¡Proyecto completo y tests pasando!
```

### 📊 Cobertura de Tests

- **🎯 Entidades (4 tests)**: Validación de User y DNI
- **💼 Casos de Uso (10 tests)**: Todos los CRUD operations
- **🔌 Adaptadores (3 tests)**: Persistencia JSON y manejo de errores

### 🧪 Tests Específicos

```bash
# Tests de entidades
python -m unittest tests.test_entities.test_user -v

# Tests de casos de uso
python -m unittest tests.test_use_cases.test_create_user_use_case -v
python -m unittest tests.test_use_cases.test_find_user_use_case -v
python -m unittest tests.test_use_cases.test_list_users_user_case -v
python -m unittest tests.test_use_cases.test_update_user_use_case -v
python -m unittest tests.test_use_cases.test_delete_user_use_case -v

# Tests de adaptadores
python -m unittest tests.test_adapters.test_file_user_repository -v
```

## 🏗️ Arquitectura Clean Architecture

### 🎯 Separación de Responsabilidades

- **🎯 Entities**: Lógica de negocio pura (User + validación DNI)
- **💼 Use Cases**: Orquestación de la lógica de aplicación  
- **🔌 Adapters**: Implementaciones concretas (FileUserRepository)
- **🌐 External**: Servicios externos (archivos, futura BD)


Los **Use Cases** dependen de **interfaces** (abstracciones), no de implementaciones concretas:

```python
# ✅ Use Case depende de abstracción
class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):  # Interface
        self.repository = repository

# ✅ Inyección de dependencia en tiempo de ejecución  
repository = FileUserRepository("users.json")  # Implementación concreta
use_case = CreateUserUseCase(repository)
```

### 🧪 Testability

Gracias a la inversión de dependencias, es fácil crear **mocks** para testing:

```python
# Mock repository para tests
class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {}
    
    def save(self, user: User) -> User:
        self.users[user._dni] = user
        return user
```

## 🔍 Ejemplos de Uso

### 📝 Ejemplo Completo de Uso

```python
from adapters.repositories import FileUserRepository
from use_cases import CreateUserUseCase, FindUserUseCase

# 1. Configurar repositorio
repo = FileUserRepository('users.json')

# 2. Crear usuarios
create_user = CreateUserUseCase(repo)
user1 = create_user.execute("Ana", "García", "12345678Z")
user2 = create_user.execute("Luis", "Martín", "87654321X") 

# 3. Buscar usuario
find_user = FindUserUseCase(repo)
found_user = find_user.execute("12345678Z")
print(f"Usuario encontrado: {found_user}")  # Ana García - DNI: 12345678Z
```

### 🗃️ Formato del archivo users.json

```json
{
    "12345678Z": {
        "username": "Ana",
        "lastname": "García", 
        "dni": "12345678Z"
    },
    "87654321X": {
        "username": "Luis",
        "lastname": "Martín",
        "dni": "87654321X"
    }
}
```

## � Conceptos Clave Aprendidos

### 🧩 **Inversión de Dependencias**
```python
# ❌ Malo: Use Case depende de implementación concreta
class CreateUserUseCase:
    def __init__(self):
        self.repository = FileUserRepository("users.json")  # Acoplado!

# ✅ Bueno: Use Case depende de abstracción
class CreateUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository  # Desacoplado!
```

### 🔄 **Responsabilidad Única**
Cada clase tiene una sola razón para cambiar:
- `User`: Solo cambia si cambian las reglas de negocio del usuario
- `CreateUserUseCase`: Solo cambia si cambia el proceso de creación
- `FileUserRepository`: Solo cambia si cambia el formato de persistencia

### 🧪 **Fácil Testing**
```python
# Test con mock repository - no necesita archivos reales
class TestCreateUserUseCase(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryUserRepository()  # Mock
        self.use_case = CreateUserUseCase(self.repository)
    
    def test_create_user_success(self):
        user = self.use_case.execute("Ana", "García", "12345678Z")
        self.assertEqual(user._username, "Ana")
```

## 🛠️ Próximos Pasos Sugeridos

### 🎯 **Extensiones del Proyecto**
1. **Database Adapter**: Implementar `DatabaseUserRepository` con SQLite
2. **HTTP API**: Crear endpoints REST con FastAPI
3. **Validaciones adicionales**: Email, teléfono, edad
4. **Frontend Web**: Interfaz HTML para gestión de usuarios
5. **Logging**: Sistema de logs para auditoría
6. **Docker**: Containerización para despliegue

### 📚 **Siguientes Conceptos a Aprender**
1. **Domain-Driven Design (DDD)**: Value Objects, Aggregates
2. **Event-Driven Architecture**: Domain Events, Event Sourcing
3. **CQRS**: Command Query Responsibility Segregation
4. **Microservices**: Comunicación entre servicios
5. **Hexagonal Architecture**: Puertos y Adaptadores

## 🚀 Demo Rápido - ¡Pruébalo Ahora!

```bash
# 1. Clonar el proyecto
git clone <repository-url>
cd users_service

# 2. Ejecutar validaciones completas
python scripts/dev.py
# 🎯 Output: 17/17 tests passed ✅

# 3. Probar la aplicación
python main.py
# Verás: Crear, buscar, listar, actualizar y eliminar usuarios

# 4. Examinar la persistencia
cat users.json
# Verás los usuarios guardados en formato JSON
```

**🎯 En 2 minutos tendrás**:
- ✅ Clean Architecture funcionando
- ✅ CRUD completo con validación DNI
- ✅ 17 tests unitarios pasando
- ✅ Persistencia JSON funcionando
- ✅ Comprensión práctica de los conceptos

## 🔍 Puntos de Aprendizaje Clave

### ✨ **Lo que este proyecto enseña**
- 🏗️ **Separación por capas**: Entities → Use Cases → Adapters → External
- 🔄 **Inversión de dependencias**: Interfaces vs Implementaciones
- 🧪 **Testabilidad**: Mocks y test unitarios
- 📦 **Responsabilidad única**: Una clase, una responsabilidad
- 🛡️ **Validación de dominio**: DNI español con algoritmo real

### 🎓 **Habilidades que desarrollas**
- Diseño de software limpio y mantenible
- Testing efectivo con mocks
- Separación de concerns
- Interfaces y abstracciones
- Principios SOLID aplicados

## 🤝 Contribuciones

Este es un proyecto educativo orientado al aprendizaje. Si tienes sugerencias de mejora o encuentras errores, ¡son bienvenidas!

### 📬 Contacto
- **GitHub Issues**: Para reportar bugs o sugerir mejoras
- **Pull Requests**: Para contribuir con código
- **Discussions**: Para preguntas sobre arquitectura

## 📚 Referencias y Recursos

- 📖 [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- 🏗️ [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- 🧪 [Test-Driven Development - Kent Beck](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)
- 🎯 [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

---

⭐ **¿Te ha ayudado este proyecto?** ¡Compártelo y dale una estrella!

🎯 **Proyecto educativo** - Cada línea de código está pensada para enseñar Clean Architecture de forma práctica