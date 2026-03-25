# Indução Matemática e Recursividade: Parte Prática 💻

Este repositório contém a implementação prática de três problemas clássicos discutidos na disciplina de **Matematica Discreta** (UFPB). O objetivo é demonstrar como a indução matemática serve como base teórica para a construção de algoritmos recursivos.

## 🚀 Conceitos Abordados

A recursividade em computação é a aplicação direta do **Princípio da Indução Matemática**:
1.  **Caso Base (Base da Indução):** A condição de parada que garante que o algoritmo não entre em loop infinito.
2.  **Passo Indutivo:** A regra que quebra o problema em instâncias menores até atingir a base.

---

## 🛠️ Algoritmos Implementados

### 1. Fatorial (`fatorial.py`)
O exemplo mais puro de recursão linear. Prova que $n! = n \times (n-1)!$.
* **Base:** $0! = 1$
* **Aplicação:** Cálculo combinatório e análise de algoritmos.

### 2. Sequência de Fibonacci (`fibonacci.py`)
Demonstra a **Indução Forte**, onde cada termo depende dos dois anteriores ($F_n = F_{n-1} + F_{n-2}$).
* **Base:** $F(0) = 0, F(1) = 1$
* **Importância:** Modelagem de crescimento populacional e proporções naturais.

### 3. Torres de Hanói (`hanoi.py`)
Problema clássico para provar que o número mínimo de movimentos necessários para $n$ discos é dado pela fórmula:
$$M(n) = 2^n - 1$$
* **Desafio Computacional:** Este algoritmo possui complexidade exponencial $O(2^n)$. 
* **Nota:** Para $n=64$ (conforme a lenda), o tempo de execução ultrapassaria a idade atual do universo! No código, recomenda-se testar com valores baixos (ex: $n=10$) para evitar *Stack Overflow*.

---

## 📦 Como Rodar

Certifique-se de ter o Python 3 instalado. Clone o repositório e execute:

```bash
# Para rodar o fatorial
python fatorial.py

# Para rodar Fibonacci
python fibonacci.py

# Para rodar Torres de Hanói
python hanoi.py
