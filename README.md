# 🚀 Sistema de Gerenciamento de Módulos de Estação Espacial

Este projeto consiste em um **simulador em Python** que gerencia módulos de uma estação espacial, permitindo analisar condições operacionais como **nível de combustível, prioridade de pouso, criticidade da carga, ordem de chegada à órbita e condições de aterrissagem**.

O objetivo principal é aplicar **conceitos fundamentais de programação**, estruturas de dados e lógica condicional em um contexto de simulação espacial.

---

## 📌 Funcionalidades

### 🧱 Definição dos Módulos
Cada módulo da estação espacial é representado por uma lista contendo os seguintes atributos:

1. **Tipo do módulo**
2. **Prioridade de pouso**
3. **Nível de combustível**
4. **Massa total**
5. **Criticidade da carga**
6. **Horário estimado de chegada à órbita**
7. **Status operacional**

### ⛽ Análise de Combustível
- Identifica módulos com **baixo combustível (menos de 70%)**, priorizando-os para reabastecimento.
- Destaca módulos com combustível suficiente para operações adicionais.

### 📦 Busca por Tipo de Carga
- Permite ao usuário buscar módulos conforme a **criticidade da carga**, por meio de entrada no terminal:
  - `1` → Carga crítica
  - `0` → Carga não crítica

### ⏱️ Ordem de Pouso
- Define a **ordem de pouso** dos módulos com base no **horário estimado de chegada à órbita**.
- Utiliza a estrutura de dados `deque` da biblioteca `collections` para manter a sequência.

### 🌤️ Condições de Pouso
- Simula condições ambientais e operacionais:
  - Clima
  - Área de pouso
  - Prioridade mínima do módulo
- Classifica os módulos em:
  - **Módulos pousados**
  - **Módulos em espera**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
