# Simple Simulator no Windows
Pasta contendo todas as adições e modificações necessárias para rodar o Simple Simulator do Processador-ICMC desenvolvido pelo Professor Eduardo Valle Simões no Instituto De Ciências Matemáticas e de Computação e disponibilizado em seu repositório [Processador-ICMC](https://github.com/simoesusp/Processador-ICMC/tree/master).

## Adições
- Compilador GCC para casos onde este não esteja instalado e configurado na máquina em que se deseja rodar o Simple Simulator.
- Script ```run.py``` para facilitar a compilação e execução do simulador.

## Modificações
- A biblioteca ```<termios.h>``` foi substituida pelo ```<conio.h>```.
- As funções ```kbhit()```, ```_rotr()``` e ```_rotl()``` uma vez que já estão incluidas nos headers.
- Chamadas da função kbhit() foram substituídas por _kbhit() pois o Windows implica.

## Como rodar
1. Extraia o .zip.
2. Execute o ```run.py```.