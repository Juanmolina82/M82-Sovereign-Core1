#!/bin/bash
# NODO: MOLINA-GLOBAL-CORE-V6
# OBJETIVO: Sincronización Total (Termux -> GitHub -> Cloud)

DATE=$(date '+%Y-%m-%d %H:%M:%S')
echo ">> [${DATE}] INICIANDO RESPALDO ROBUSTO..."

cd ~/MOLINA-GLOBAL-CORE-V6

# A. Limpieza de procesos duplicados antes de sincronizar
pkill -9 -f python

# B. Consolidación en GitHub (La Verdad Única)
git add .
git commit -m "ROBUST_BACKUP: [${DATE}] - Integración AGI y Milken Intel"
git push origin main

# C. Verificación de Integridad de Carpetas
echo ">> VERIFICANDO ESTRUCTURA..."
ls -R > estructura_core.log

echo ">> [${DATE}] RESPALDO COMPLETADO CON ÉXITO."
