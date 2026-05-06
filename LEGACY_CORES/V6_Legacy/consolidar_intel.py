import os

repositorios_fragmentados = [
    "m82_core.py", "MOLINA_UNIFIED_KEY_FINAL", 
    "MASTER_UNIFICATION_V3", "M82-Sovereign-Core",
    "MOLINA__IA__Plataform", "M1982"
]

def consolidar():
    print(">> INICIANDO BARRIDO DE FRAGMENTOS...")
    for repo in repositorios_fragmentados:
        path = os.path.expanduser(f"~/{repo}")
        if os.path.exists(path):
            print(f"[-] Eliminando redundancia: {repo}")
            os.system(f"rm -rf {path}")
    print(">> MATRIZ UNIFICADA: LIMPIA Y CENTRALIZADA.")

if __name__ == "__main__":
    consolidar()
