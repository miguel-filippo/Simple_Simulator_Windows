import os

os.system("mingw32\bin\gcc simple_simulator_Template.c -O3 -march=native -o simulador -Wall -lm")
os.system("cls")
os.system("simulador")
