import os
import sys
import importlib.util

# Ermittelt den Basispfad (wo menu.py bzw. die EXE ausgeführt wird)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

def run_script_by_path(relative_path, module_name):
    """Lädt ein Python-Skript dynamisch über seinen Pfad relativ zur menu.py."""
    try:
        full_path = os.path.normpath(os.path.join(base_path, relative_path))
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Datei nicht gefunden: {full_path}")
            
        spec = importlib.util.spec_from_file_location(module_name, full_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        if module_name in sys.modules:
            del sys.modules[module_name]
            
    except Exception as e:
        print(f"\nFehler beim Ausführen von {module_name}: {e}")
        input("\nDrücke Enter, um fortzufahren...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 40)
        print("      WEEK 5 - MENÜ")
        print("=" * 40)
        print("1) Dino")
        print("2) Grade")
        print("3) Reactiontime")
        print("4) Some")
        print("5) Thething")
        print("6) Towerdefense")
        print("7) Beenden")
        print("=" * 40)
        
        auswahl = input("Bitte eine Option wählen (1-7): ").strip()
        
        if auswahl == "1":
            run_script_by_path("dino.py", "dino")
        elif auswahl == "2":
            run_script_by_path("grade.py", "grade")
        elif auswahl == "3":
            run_script_by_path("reactiontime.py", "reactiontime")
        elif auswahl == "4":
            run_script_by_path("some.py", "some")
        elif auswahl == "5":
            run_script_by_path("thething.py", "thething") 
        elif auswahl == "6":
            run_script_by_path("towerdefense.py", "towerdefense")
        elif auswahl == "7":
            print("\nProgramm beendet.")
            break
        else:
            input("\nUngültige Auswahl. Drücke Enter...")
            continue
            
        input("\nDrücke Enter, um zum Menü zurückzukehren...")

if __name__ == "__main__":
    main()
