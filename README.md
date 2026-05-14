# Listas_Algoritmos

Repositório focado na resolução de problemas de programação competitiva (estilo Codeforces), consolidando o aprendizado de Algoritmos e Estruturas de Dados. Desenvolvido como parte da evolução técnica no 3º período do curso de Sistemas de Informação no CIn-UFPE, este projeto documenta a transição e a aplicação de conceitos de baixo e alto nível utilizando **C** e **Python**.

## 🚀 Arquitetura e Padrões Aplicados

As resoluções aqui contidas não focam apenas em "funcionar", mas em respeitar limites rigorosos de tempo e memória. Os principais conceitos arquiteturais abordados incluem:

* **Processamento em Lote (Fast I/O):** Uso de `sys.stdin.read().split()` em Python para mitigar gargalos de I/O em entradas massivas ($\mathcal{O}(N)$ instantâneo).
* **Algoritmos Gulosos (Greedy):** Tomada de decisão ótima local para resolução de problemas de otimização (ex: `160A.py`, `twins.c`).
* **Somas Acumuladas (Prefix Sum):** Pré-processamento de arrays para responder a consultas de soma de intervalos em tempo constante ($\mathcal{O}(1)$).
* **Busca Binária (Binary Search):** Otimização de varreduras lineares para $\mathcal{O}(\log N)$ em arrays ordenados.
* **Dois Ponteiros (Two Pointers):** Resolução eficiente de problemas de pares e somas, reduzindo complexidades de $\mathcal{O}(N^3)$ para $\mathcal{O}(N^2)$.
* **Manutenção de Estado Global:** Substituição de contagens lineares custosas por variáveis de estado em tempo real.

## 🛠️ Tecnologias e Configuração

* **Python 3:** Foco em código idiomático (*Pythonic*), manipulação avançada de listas (fatiamento, índices negativos) e dicionários.
* **C (C23):** Implementações manuais utilizando ponteiros, alocação dinâmica (`calloc`, `free`) e ordenação nativa (`qsort`).
* **Build System:** O ambiente C é gerenciado via **CMake**, configurado rigorosamente para o padrão C23.

## 📂 Índice de Resoluções

| Arquivo / Problema | Linguagem | Conceito Principal | Complexidade Dominante |
| :--- | :--- | :--- | :--- |
| `1360B.py` (Honest Coach) | Python | Ordenação (Merge Sort) | $\mathcal{O}(N \log N)$ |
| `1399C.py` (Boats Competition) | Python | Dois Ponteiros (Two Pointers) | $\mathcal{O}(N^2)$ |
| `1491A.py` (K-th Largest Value) | Python | Manutenção de Estado | $\mathcal{O}(N + Q)$ |
| `160A.py` / `twins.c` (Twins) | Python / C | Algoritmo Guloso (Greedy) | $\mathcal{O}(N \log N)$ |
| `433B.py` (Kuriyama Mirai) | Python | Somas Acumuladas (Prefix Sum) | $\mathcal{O}(N \log N + M)$ |
| `863B.py` | Python | Array Simulation / Força Bruta | $\mathcal{O}(N^3)$ |
| `977B.py` (Two-gram) | Python | Manipulação de Strings | $\mathcal{O}(N)$ |
| `worms.c` | C | Busca Binária | $\mathcal{O}(M \log N)$ |
| `less_or_equals.c` | C | Busca Binária | $\mathcal{O}(N \log N)$ |
| `dragoes.c` | C | Algoritmo Guloso / `qsort` | $\mathcal{O}(N \log N)$ |
| `business_trip.c` | C | Algoritmo Guloso | $\mathcal{O}(N \log N)$ |

## 📄 Licença

Este projeto está distribuído sob a Licença MIT (Copyright 2026 Vinicius Oliveira). O software é fornecido "como está", sem garantias explícitas ou implícitas de adequação a um propósito específico. Os autores ou detentores dos direitos autorais não se responsabilizam por quaisquer danos, reclamações ou outras responsabilidades decorrentes do uso do software.
