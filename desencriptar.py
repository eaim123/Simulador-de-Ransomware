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

EXTENSIONES_OBJETIVO = ['.txt', '.jpg', '.jpeg', '.png', '.mp4', '.docx', '.odt', '.ods', '.odp']
ARCHIVOS_EXCLUIDOS = [
    "ransomware_simulador.py",
    "desencriptar.py",
    ".clave.key",
    "README_RESCATE.txt"
]

# === CARGA DE CLAVE ===

if not os.path.exists(".clave.key"):
    print("❌ ERROR: No se encontró '.clave.key'. No se puede desencriptar.")
    exit(1)

with open(".clave.key", "rb") as f:
    clave = f.read()

fernet = Fernet(clave)

# === DESENCRIPTADO DE ARCHIVOS ===

archivos_restaurados = 0
archivos_fallidos = 0

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
                archivos_fallidos += 1
                print(f"⚠️ No se pudo desencriptar (token inválido): {ruta_completa}")
            except Exception as e:
                archivos_fallidos += 1
                print(f"⚠️ Error en {ruta_completa}: {e}")

# === RESULTADO FINAL ===

print("\n📊 Resultado de la restauración:")
print(f"✅ Archivos desencriptados correctamente: {archivos_restaurados}")
print(f"❌ Archivos que no pudieron desencriptarse: {archivos_fallidos}")

if archivos_restaurados == 0:
    print("\n⚠️ No se desencriptó ningún archivo.")
else:
    print("\n🎉 Desencriptado finalizado correctamente.")
