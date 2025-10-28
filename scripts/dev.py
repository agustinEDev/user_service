#!/usr/bin/env python3
"""
dev_pv.py - Script de desarrollo para Python Version Project

Este script ejecuta validaciones completas del proyecto Python Version,
incluyendo tests unitarios y validación de archivos del proyecto.
Diseñado para funcionar desde la raíz del proyecto python_version.
"""

import subprocess
import sys
import os
from pathlib import Path

def print_banner():
    """Imprime banner del proyecto"""
    print("=" * 70)
    print("🏗️  CLEAN ARCHITECTURE PROJECT - PYTHON VERSION")
    print("🐍  Python Implementation with Clean Architecture")
    print("=" * 70)

def validate_project_structure():
    """Valida que la estructura del proyecto sea correcta"""
    print("🔍 Validando estructura del proyecto...")
    print("-" * 50)
    
    required_items = {
        "README.md": "📖 Documentación principal",
        "README_PV.md": "📖 Documentación Python Version",
        "main.py": "🚀 Aplicación principal",
        "users.json": "💾 Archivo de datos",
        "tests/": "🧪 Tests unitarios",
        "entities/": "🎯 Entidades del negocio",
        "use_cases/": "💼 Casos de uso",
        "adapters/": "🔌 Adaptadores",
        "adapters/repositories/": "🗄️ Repositorios",
        "adapters/controllers/": "🎮 Controladores",
        "external/": "🌐 Servicios externos",
        "scripts/": "📜 Scripts de desarrollo"
    }
    
    all_good = True
    for item, description in required_items.items():
        path = Path(item)
        if path.exists():
            print(f"✅ {description}: {item}")
        else:
            print(f"❌ {description}: {item} - NO ENCONTRADO")
            all_good = False
    
    return all_good

def get_project_stats():
    """Obtiene estadísticas del proyecto"""
    print("\n📊 ESTADÍSTICAS DEL PROYECTO:")
    print("-" * 50)
    
    # Python Version Stats
    print("🐍 PYTHON VERSION:")
    tests_dir = Path("tests")
    if tests_dir.exists():
        test_files = list(tests_dir.rglob("test_*.py"))
        print(f"   🧪 Archivos de test: {len(test_files)}")
    
    use_cases_dir = Path("use_cases")
    if use_cases_dir.exists():
        use_case_files = list(use_cases_dir.glob("*_use_case.py"))
        print(f"   💼 Casos de uso: {len(use_case_files)}")
    
    entities_dir = Path("entities")
    if entities_dir.exists():
        entity_files = list(entities_dir.glob("*.py"))
        entity_count = len([f for f in entity_files if not f.name.startswith('__')])
        print(f"   🎯 Entidades: {entity_count}")
    
    adapters_dir = Path("adapters")
    if adapters_dir.exists():
        repo_files = list(adapters_dir.rglob("*repository*.py"))
        repo_count = len([f for f in repo_files if not f.name.startswith('__')])
        print(f"   🗄️ Repositorios: {repo_count}")
    
    users_json = Path("users.json")
    if users_json.exists():
        print("   💾 users.json: ✅ Datos existentes")
    else:
        print("   💾 users.json: ⚪ Sin datos")
    
    # Verificar documentación
    readme = Path("README_PV.md")
    if readme.exists():
        lines = len(readme.read_text().splitlines())
        print(f"📖 README_PV.md: ✅ {lines} líneas de documentación")

def run_python_tests():
    """Ejecuta todos los tests de Python Version"""
    print("\n🧪 Ejecutando Tests de Python Version...")
    print("-" * 50)
    
    # Buscar todos los archivos de test
    test_files = []
    test_dir = Path("tests")
    
    if test_dir.exists():
        for test_file in test_dir.rglob("test_*.py"):
            test_files.append(test_file)
    
    if not test_files:
        print("⚠️  No se encontraron archivos de test")
        return False, 0, 0
    
    print(f"📋 Encontrados {len(test_files)} archivos de test:")
    for test_file in sorted(test_files):
        print(f"   - {test_file}")
    
    print("\n🚀 Ejecutando tests...")
    
    # Ejecutar cada test individualmente
    all_passed = True
    passed_tests = []
    failed_tests = []
    
    for test_file in sorted(test_files):
        test_name = test_file.name
        
        # Convertir la ruta del archivo a módulo Python
        module_path = str(test_file).replace('/', '.').replace('.py', '')
        
        print(f"\n▶️  Ejecutando {test_name}...")
        
        try:
            result = subprocess.run([
                sys.executable, "-m", module_path
            ], capture_output=True, text=True)
            
            # Parsear número de tests ejecutados desde el output
            import re
            test_count = 1  # Default a 1 si no se puede parsear
            test_output = (result.stdout or '') + (result.stderr or '')
            if test_output:
                match = re.search(r'Ran (\d+) test', test_output)
                if match:
                    test_count = int(match.group(1))
            
            if result.returncode == 0:
                print(f"   ✅ {test_name} - PASSED ({test_count} tests)")
                for i in range(test_count):
                    passed_tests.append(f"{test_name}_test_{i}")
            else:
                print(f"   ❌ {test_name} - FAILED ({test_count} tests)")
                if result.stderr:
                    print(f"      Error: {result.stderr.strip()}")
                if result.stdout:
                    print(f"      Output: {result.stdout.strip()}")
                for i in range(test_count):
                    failed_tests.append(f"{test_name}_test_{i}")
                all_passed = False
                
        except Exception as e:
            print(f"   ❌ {test_name} - ERROR: {e}")
            failed_tests.append(test_name)
            all_passed = False
    
    # Resumen final
    print(f"\n📊 RESUMEN DE TESTS:")
    print(f"   ✅ Pasaron: {len(passed_tests)}")
    print(f"   ❌ Fallaron: {len(failed_tests)}")
    
    if failed_tests:
        print(f"\n❌ Tests que fallaron:")
        for test in failed_tests:
            print(f"   - {test}")
    
    return all_passed, len(passed_tests), len(failed_tests)

def check_git_status():
    """Verifica el estado de Git"""
    print("\n📝 Estado de Git:")
    print("-" * 50)
    
    try:
        # Verificar si hay cambios
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, check=True
        )
        
        if result.stdout.strip():
            print("📝 Cambios detectados:")
            for line in result.stdout.strip().split('\n'):
                print(f"   {line}")
        else:
            print("✅ No hay cambios pendientes")
            
        # Mostrar rama actual
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, check=True
        )
        print(f"🌿 Rama actual: {branch_result.stdout.strip()}")
        
    except subprocess.CalledProcessError:
        print("⚠️  No es un repositorio Git o Git no está disponible")

def main():
    """Función principal del modo desarrollo"""
    print_banner()
    
    # Validar estructura
    structure_ok = validate_project_structure()
    
    # Mostrar estadísticas
    get_project_stats()
    
    # Verificar estado de Git
    check_git_status()
    
    # Ejecutar tests si la estructura es correcta
    if structure_ok:
        tests_passed, passed_count, failed_count = run_python_tests()
    else:
        print("\n❌ Estructura del proyecto incorrecta, saltando tests...")
        tests_passed = False
        passed_count = 0
        failed_count = 0
    
    # Resumen final detallado
    print("\n" + "=" * 70)
    print("📋 RESUMEN FINAL")
    print("=" * 70)
    
    if structure_ok:
        test_icon = "✅" if tests_passed else "❌"
        print(f"{test_icon} PYTHON VERSION:")
        if tests_passed:
            total_tests = passed_count + failed_count
            print(f"   🧪 Todos los tests unitarios pasaron ({passed_count}/{total_tests})")
            print("   💼 Casos de uso implementados")
            print("   📦 Entidades y adaptadores validados")
        else:
            total_tests = passed_count + failed_count
            print(f"   ❌ Algunos tests unitarios fallaron ({passed_count}/{total_tests})")
    else:
        print("❌ PYTHON VERSION: Estructura incompleta")
    
    # Resultado general
    print("\n" + "-" * 70)
    if structure_ok and tests_passed:
        total_tests = passed_count + failed_count
        print("🎉 RESULTADO: ¡Proyecto completo y tests pasando!")
        print(f"📊 TOTALES: {total_tests}/{total_tests} tests pasaron")
        print("🚀 Estado: Listo para commit y push")
        sys.exit(0)
    else:
        print("🔧 RESULTADO: Revisar errores antes de continuar")
        total_issues = 0
        if not structure_ok:
            print("   🏗️  Estructura del proyecto incompleta")
            total_issues += 1
        if structure_ok and not tests_passed:
            print("   🐍 Tests fallando")
            total_issues += 1
        print(f"📊 Total de problemas encontrados: {total_issues}")
        sys.exit(1)

if __name__ == "__main__":
    main()
