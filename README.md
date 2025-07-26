# 🛡️ Simulador de Ransomware y Desencriptador AES en Python

Este proyecto consiste en **dos scripts escritos en Python 3.11** que simulan el proceso de cifrado y descifrado de archivos mediante el algoritmo **AES (Advanced Encryption Standard)**, con fines educativos y de concientización en ciberseguridad.

> ⚠️ **Este repositorio es solo para fines educativos.** No debe usarse para actividades maliciosas o no autorizadas.

---

## 📁 Contenido
--ransomware_simuladro.py
--desencriptar.py
---

## 🔐 ¿Qué hace el simulador?

El script de ransomware simulado realiza un cifrado AES de archivos en una carpeta objetivo y todas sus subcarpetas (búsqueda recursiva). Esto simula el comportamiento de un ransomware real que cifra el contenido de un sistema de archivos, causando pérdida de acceso a los documentos del usuario. Luego, el desencriptador puede **revertir el proceso** si se proporciona la clave correcta.

### Ejemplo de flujo:
1. El usuario ejecuta `ransomware_simulado.py` y los archivos son cifrados.
2. Para recuperar los archivos, el usuario debe usar `desencriptador_simulado.py` con la clave original.

---

## 🛠️ Requisitos

- Python 3.11
- [`pycryptodome`](https://pypi.org/project/pycryptodome/):
  ```bash
  pip install pycryptodome
