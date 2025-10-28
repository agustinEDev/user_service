# Python Version - Clean Architecture Project
"""
Este proyecto implementa Clean Architecture con un sistema de usuarios CRUD completo.

Módulos principales:
- entities: Entidades de dominio (User)
- use_cases: Casos de uso de la aplicación
- adapters: Adaptadores para repositorios y controladores
- external: Servicios externos
- tests: Tests unitarios completos

Ejemplo de uso:
    from adapters.repositories import FileUserRepository
    from use_cases import CreateUserUseCase
    from entities import User
    
    repository = FileUserRepository('users.json')
    create_user = CreateUserUseCase(repository)
    user = create_user.execute("Juan", "Pérez", "12345678Z")
"""

__version__ = "1.0.0"
__author__ = "Agustín Estévez Domínguez"

# Exportar los módulos principales para fácil acceso
from . import entities
from . import use_cases
from . import adapters

__all__ = ['entities', 'use_cases', 'adapters']