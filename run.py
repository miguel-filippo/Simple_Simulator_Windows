import os

gcc_path = os.path.join("mingw32", "bin", "gcc")

warnings = os.popen(gcc_path + " simple_simulator_Template.c -O3 -march=native -o simulador -Wall -lm")

if(warnings):
    print("========= ALERTAS DE COMPILAÇÃO =========")
    print()
    print(warnings.read())
    print("=========================================")
    print()

os.system("simulador.exe")
