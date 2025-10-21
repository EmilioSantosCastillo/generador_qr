# 📘 GUÍA: Configurar Proyecto en Nuevo Computador

Esta guía te ayudará a configurar el proyecto "Generador de QR" en cualquier computador nuevo.

---

## 🎯 REQUISITOS PREVIOS

Antes de comenzar, asegúrate de tener instalado:

### 1. Python 3.10 o superior
- **Descargar:** https://www.python.org/downloads/
- ✅ Durante la instalación, marca: **"Add Python to PATH"**
- **Verificar instalación:**
```powershell
  python --version
```
  Debe mostrar: `Python 3.10.x` o superior

### 2. Git
- **Descargar:** https://git-scm.com/downloads/
- **Verificar instalación:**
```powershell
  git --version
```

### 3. Visual Studio Code (Opcional pero recomendado)
- **Descargar:** https://code.visualstudio.com/

---

## 📥 PASO 1: Clonar el Repositorio

### Opción A: Desde la Terminal
```powershell
# Navega a donde quieres guardar el proyecto
cd C:\Users\TuUsuario\Documents\Proyectos

# Clona el repositorio
git clone https://github.com/tu-usuario/qr-generator.git

# Entra a la carpeta
cd qr-generator
```

### Opción B: Desde VS Code

1. Abre Visual Studio Code
2. Presiona `Ctrl + Shift + P`
3. Escribe: "Git: Clone"
4. Pega la URL: `https://github.com/tu-usuario/qr-generator.git`
5. Selecciona dónde guardar el proyecto

---

## 🐍 PASO 2: Crear Entorno Virtual
```powershell
# Asegúrate de estar en la carpeta del proyecto
cd qr-generator

# Crear entorno virtual
python -m venv venv
```

**¿Qué hace esto?**
Crea una carpeta `venv/` con un ambiente aislado de Python para este proyecto.

---

## ⚡ PASO 3: Activar Entorno Virtual

### En Windows PowerShell:
```powershell
# Si es la primera vez, necesitas dar permisos:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activar el entorno:
.\venv\Scripts\Activate.ps1
```

### En Windows CMD:
```cmd
venv\Scripts\activate.bat
```

### En Mac/Linux:
```bash
source venv/bin/activate
```

### ✅ Confirmación

Deberías ver `(venv)` al inicio de tu línea de comandos:
```powershell
(venv) PS C:\Users\TuUsuario\...\qr-generator>
```

---

## 📦 PASO 4: Instalar Dependencias

Con el entorno virtual activado:
```powershell
# Actualizar pip a la última versión
pip install --upgrade pip

# Instalar todas las dependencias del proyecto
pip install -r requirements.txt
```

**⏳ Esto tomará entre 2-5 minutos**

Verás que se descargan e instalan:
- PyQt6 (interfaz gráfica)
- segno (generación de QR)
- Pillow (procesamiento de imágenes)
- requests (cliente HTTP)
- reportlab (exportación PDF)
- vobject (vCard)
- Y más...

---

## ✅ PASO 5: Verificar Instalación
```powershell
# Ver todas las librerías instaladas
pip list
```

Deberías ver listadas:
- PyQt6
- segno
- Pillow
- requests
- reportlab
- vobject
- pytest
- black
- flake8

### Probar que funciona:
```powershell
python
```

Dentro del intérprete de Python:
```python
>>> import PyQt6
>>> import segno
>>> import PIL
>>> print("¡Todo funciona!")
>>> exit()
```

Si no hay errores, ¡perfecto! ✅

---

## 🎨 PASO 6: Configurar VS Code (Opcional)

Si usas Visual Studio Code:

### 1. Abrir el proyecto
```
File → Open Folder → Selecciona la carpeta qr-generator
```

### 2. Seleccionar el intérprete de Python
- Presiona `Ctrl + Shift + P`
- Escribe: `Python: Select Interpreter`
- Selecciona: `.\venv\Scripts\python.exe`

### 3. Instalar extensiones recomendadas
- Python (Microsoft)
- Pylance
- GitLens (opcional)

VS Code detectará automáticamente el archivo `.gitignore` y el entorno virtual.

---

## 🚀 PASO 7: Ejecutar la Aplicación
```powershell
# Asegúrate de que el entorno esté activado (debes ver (venv))
python main.py
```

*Nota: Por ahora `main.py` no existe, lo crearemos en las siguientes fases del desarrollo.*

---

# 🔄 USO DIARIO

## 📅 Al Comenzar a Trabajar Cada Día
```powershell
# 1. Abrir terminal en la carpeta del proyecto
cd C:\ruta\a\tu\proyecto\qr-generator

# 2. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 3. Descargar últimos cambios de GitHub
git pull

# 4. Si hubo cambios en requirements.txt, actualizar dependencias
pip install -r requirements.txt

# 5. ¡Empezar a trabajar!
```

---

## 💾 Al Terminar de Trabajar
```powershell
# 1. Ver qué archivos cambiaron
git status

# 2. Agregar todos los archivos modificados
git add .

# 3. Guardar cambios con un mensaje descriptivo
git commit -m "Descripción clara de lo que hiciste"

# 4. Subir cambios a GitHub
git push

# 5. Desactivar entorno virtual
deactivate
```

---

# 🔄 SINCRONIZACIÓN ENTRE COMPUTADORES

## Escenario: Trabajaste en Computador A, ahora quieres continuar en Computador B

### En Computador A (antes de irte):
```powershell
git add .
git commit -m "Avance de hoy: [descripción]"
git push
```

### En Computador B (al llegar):
```powershell
# 1. Ir al proyecto
cd ruta\al\proyecto

# 2. Activar entorno
.\venv\Scripts\Activate.ps1

# 3. Descargar cambios
git pull

# 4. Si hay nuevas dependencias
pip install -r requirements.txt

# 5. Continuar trabajando
```

---

# 🆕 SI INSTALASTE UNA NUEVA LIBRERÍA

### En el computador donde la instalaste:
```powershell
# 1. Instalar la librería
pip install nombre-de-libreria

# 2. Actualizar requirements.txt
pip freeze > requirements.txt

# 3. Subir a GitHub
git add requirements.txt
git commit -m "Agregada librería: nombre-de-libreria"
git push
```

### En otros computadores:
```powershell
# 1. Descargar cambios
git pull

# 2. Instalar la nueva librería
pip install -r requirements.txt
```

---

# 🚨 SOLUCIÓN DE PROBLEMAS

## ❌ Error: "No se puede activar el entorno virtual en PowerShell"

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**Alternativa:** Usa CMD en lugar de PowerShell
```cmd
venv\Scripts\activate.bat
```

---

## ❌ Error: "python no se reconoce como comando"

**Solución 1:** Usa `python3` en lugar de `python`
```powershell
python3 --version
python3 -m venv venv
```

**Solución 2:** Reinstala Python y marca "Add Python to PATH"

---

## ❌ Error: "pip no funciona"

**Solución:**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## ⚠️ Conflictos al hacer git pull

**Opción 1: Guardar cambios temporalmente**
```powershell
git stash              # Guarda tus cambios
git pull               # Descarga cambios remotos
git stash pop          # Recupera tus cambios
```

**Opción 2: Sobrescribir cambios locales (¡CUIDADO!)**
```powershell
git reset --hard       # Descarta TODOS tus cambios locales
git pull               # Descarga versión de GitHub
```

---

## 🤔 Olvidé hacer push y trabajé en otro computador
```powershell
# En el computador donde olvidaste hacer push:

# 1. Intentar descargar cambios
git pull

# 2. Si hay conflictos, Git te lo dirá
# Abre los archivos en conflicto y busca esto:
<<<<<<< HEAD
Tu código local
=======
Código de GitHub
>>>>>>> branch-name

# 3. Edita manualmente y quédate con lo que necesites

# 4. Después de resolver:
git add .
git commit -m "Resueltos conflictos"
git push
```

---

# 📋 CHECKLIST RÁPIDO

## ✅ Primera vez en un computador nuevo

- [ ] Instalar Python 3.10+
- [ ] Instalar Git
- [ ] Clonar repositorio
- [ ] Crear entorno virtual: `python -m venv venv`
- [ ] Activar entorno: `.\venv\Scripts\Activate.ps1`
- [ ] Instalar dependencias: `pip install -r requirements.txt`
- [ ] Verificar: `pip list`
- [ ] Configurar VS Code (opcional)

## ✅ Cada vez que trabajes

- [ ] Activar entorno virtual
- [ ] `git pull` (descargar cambios)
- [ ] Trabajar en el proyecto
- [ ] `git add .` (agregar cambios)
- [ ] `git commit -m "..."` (guardar cambios)
- [ ] `git push` (subir a GitHub)
- [ ] `deactivate` (desactivar entorno)

---

# 📝 COMANDOS DE REFERENCIA

## Git - Comandos Esenciales
```powershell
git status                    # Ver estado actual
git pull                      # Descargar cambios
git add .                     # Agregar todos los archivos
git add archivo.py            # Agregar archivo específico
git commit -m "mensaje"       # Guardar cambios
git push                      # Subir a GitHub
git log --oneline             # Ver historial
git diff                      # Ver diferencias
```

## Python/pip - Comandos Esenciales
```powershell
python --version              # Ver versión de Python
pip --version                 # Ver versión de pip
pip list                      # Ver librerías instaladas
pip install libreria          # Instalar librería
pip uninstall libreria        # Desinstalar librería
pip freeze > requirements.txt # Guardar dependencias
pip install -r requirements.txt # Instalar desde archivo
```

## Entorno Virtual
```powershell
# Crear
python -m venv venv

# Activar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activar (Windows CMD)
venv\Scripts\activate.bat

# Activar (Mac/Linux)
source venv/bin/activate

# Desactivar (cualquier sistema)
deactivate
```

---

# 🆘 SOPORTE

Si encuentras problemas no cubiertos aquí:

1. **Revisa la documentación oficial:**
   - Python: https://docs.python.org/3/
   - PyQt6: https://www.riverbankcomputing.com/static/Docs/PyQt6/
   - Git: https://git-scm.com/doc

2. **Busca en Stack Overflow:**
   - https://stackoverflow.com/

3. **Revisa los Issues del proyecto en GitHub**

---

# 📚 RECURSOS ADICIONALES

- **Documentación del Proyecto:** Ver `README.md`
- **Especificaciones Técnicas:** Ver documento maestro en `/docs/`
- **API Backend:** Ver `/docs/API.md` (cuando esté disponible)

---

**Última actualización:** Octubre 2025  
**Versión:** 1.0.0