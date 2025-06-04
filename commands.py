#!/usr/bin/env python3
import sys
from config import password, commands

def list_commands():
    return {label: f"./commands.py {label}" for label in commands.keys()}

if __name__ == "__main__":
    #print(sys.argv)
    try:
        if sys.argv[1] in commands.keys():
            if sys.argv[2] == password:
                command = commands[sys.argv[1]]
                #print(command)
                import subprocess
                result = subprocess.run(command, capture_output=True, text=True)
                if not result.stdout.strip():
                    print("Success")
                else:
                    print(result.stdout)
            else:
                print("Mot de passe incorrect")
    except Exception as e:
        print("Erreur d'exécution")
