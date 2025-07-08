<div align="center">

# 🗺️ Dijkstra Algorithm Application



### Interactive Educational Tool for Shortest Path Finding

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![NetworkX](https://img.shields.io/badge/Graphs-NetworkX-orange.svg)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-red.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---


</div>

## 🎯 About the Project

**Dijkstra Algorithm Application** is an interactive educational tool that demonstrates Dijkstra's shortest path algorithm. Created for educational purposes, it provides step-by-step visualization of how the algorithm works on both directed and undirected graphs.

### 🎓 Educational Features

- **Step-by-step algorithm execution** with detailed explanations
- **Interactive graph generation** with customizable parameters  
- **Real-time visualization** using NetworkX and Matplotlib
- **Complexity analysis** with practical examples
- **Comparison** between directed and undirected graphs

## ✨ Key Features

### 🔧 Core Functionality
- ✅ **Random graph generation** with 2-3x more edges than vertices
- ✅ **Interactive graph visualization** with edge weights (1-14)
- ✅ **Real-time algorithm execution** tracking each step
- ✅ **Shortest path reconstruction** and complete analysis
- ✅ **Detailed results** with complexity calculations

### 📊 Graph Types
- 🔄 **Directed graphs** - with directional arrows
- ↔️ **Undirected graphs** - bidirectional connections
- 🎲 **Random edge weights** - integer values 1-14
- 📈 **Scalable size** - 5-20 vertices recommended

### 🖥️ User Interface
- 🎨 **Full-screen application** with professional layout
- 🔧 **Simple controls** - just set vertices and start vertex
- 📊 **Comprehensive results** - paths, steps, and complexity analysis
- 🌐 **Bilingual interface** - supports both graph types

## 🛠️ Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language | 3.12+ |
| ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) | Graphical user interface | Built-in |
| ![NetworkX](https://img.shields.io/badge/NetworkX-Graph-orange) | Graph visualization | 3.0+ |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-red) | Graph rendering | 3.7+ |
| ![PyInstaller](https://img.shields.io/badge/PyInstaller-Executable-blue) | Standalone .exe creation | 5.0+ |

## 🚀 Download

### Ready-to-Use Executable

**Windows Users**: Download the standalone executable (no Python installation required)

📥 **[DijksryApp.exe](dist/dijkstryApp.exe)** 

> **⚠️ Security Notice**: Windows may show a security warning for unsigned executables. Click "More info" → "Run anyway" to proceed.

### System Requirements
- 🖥️ **OS**: Windows 10/11 (64-bit)
- 💾 **RAM**: 512 MB minimum
- 💿 **Storage**: 50 MB free space
- 🖼️ **Display**: 1024x768 minimum resolution

## 🔧 Installation

Simply download and run `DijkstryApp.exe` - no additional setup required!

*Source code is also available in this repository for developers.*

## 💻 Usage

### Quick Start Guide

1. **Launch Application**
   - Double-click `DijkstryApp.exe`
   - Application opens in full-screen mode

2. **Configure Graph**
   - Enter number of vertices (5-15 recommended)
   - Choose graph type: **Directed** or **Undirected**
   - Click **"Generate Graph"**

3. **Run Algorithm**
   - Enter starting vertex number (0 to n-1)
   - Click **"Run Dijkstra Algorithm"**
   - View detailed step-by-step results

### 🎮 Interface Controls

| Control | Function |
|---------|----------|
| **Number of Vertices** | Set graph size |
| **Graph Type Radio** | Select directed/undirected |
| **Generate Graph** | Create random graph |
| **Start Vertex** | Choose algorithm starting point |
| **Run Algorithm** | Execute Dijkstra's algorithm |
| **Close Application** | Exit program |

### 📊 Results Analysis

The application displays:
- **Shortest Paths Table** - distances and paths to all vertices
- **Step-by-Step Execution** - detailed algorithm progress
- **Complexity Analysis** - O(V²) calculations for your graph
- **Performance Summary** - reachable vertices and statistics

## 🧮 Algorithm Overview

### Dijkstra's Algorithm Explained

**Purpose**: Find shortest paths from source vertex to all other vertices in weighted graph with non-negative edge weights.

**How it works**:
1. **Initialize** distances (0 for start, ∞ for others)
2. **Select** unvisited vertex with minimum distance
3. **Update** distances to neighbors if shorter path found
4. **Repeat** until all reachable vertices processed

**Time Complexity**: 
- Our implementation: **O(V²)** - optimal for dense graphs
- Binary heap version: **O((V+E)log V)** - better for sparse graphs
- Fibonacci heap: **O(E + V log V)** - theoretical optimum

**Space Complexity**: **O(V)** for distance and predecessor arrays

### Practical Applications

- 🗺️ **GPS Navigation** - finding shortest driving routes
- 🌐 **Network Routing** - packet routing in computer networks  
- 🎮 **Game AI** - pathfinding for characters
- 📦 **Logistics** - delivery route optimization
- 🔗 **Social Networks** - shortest connection paths

## 📚 Complete Documentation

📄 **[Full Documentation PL (DOCX)](Dijkstry_PL.docx)**

The complete documentation includes:
- Detailed algorithm theory and mathematical foundations
- Step-by-step example with 5-vertex graph
- Comprehensive complexity analysis with charts
- Complete user manual and technical specifications

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary**: Free to use, modify, and distribute. Just keep the original copyright notice.

## 👨‍💻 Author

**Sebastian Ciborowski**

- 🎓 Computer Science Student & IT Enthusiast.  
- 💼 Specializing in CyberSec,, Python & AI.
- 🔗 GitHub: [@sebastian-c87](https://github.com/sebastian-c87)

---

<div align="center">

**⭐ If this project helped you understand Dijkstra's algorithm, please consider giving it a star!**

**Made with ❤️ for education and learning**

</div>
<br>
<br>

---
---
---
<br>
<br>

<div align="center">

# 🗺️ Aplikacja Algorytmu Dijkstry

### Interaktywne Narzędzie Edukacyjne do Znajdowania Najkrótszych Ścieżek

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![NetworkX](https://img.shields.io/badge/Grafy-NetworkX-orange.svg)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Wizualizacja-Matplotlib-red.svg)](https://matplotlib.org/)
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

--- 
</div>


## 🎯 O Projekcie

**Aplikacja Algorytmu Dijkstry** to interaktywne narzędzie edukacyjne demonstrujące algorytm najkrótszej ścieżki Dijkstry. Stworzona w celach edukacyjnych, zapewnia wizualizację krok po kroku działania algorytmu na grafach skierowanych i nieskierowanych.

### 🎓 Funkcje Edukacyjne

- **Wykonanie algorytmu krok po kroku** ze szczegółowymi wyjaśnieniami
- **Interaktywne generowanie grafów** z konfigurowalnymi parametrami
- **Wizualizacja w czasie rzeczywistym** przy użyciu NetworkX i Matplotlib
- **Analiza złożoności** z praktycznymi przykładami
- **Porównanie** grafów skierowanych i nieskierowanych

## ✨ Kluczowe Funkcje

### 🔧 Podstawowa Funkcjonalność
- ✅ **Losowe generowanie grafów** z 3-4x więcej krawędzi niż wierzchołków
- ✅ **Interaktywna wizualizacja grafów** z wagami krawędzi (1-14)
- ✅ **Wykonanie algorytmu w czasie rzeczywistym** ze śledzeniem każdego kroku
- ✅ **Rekonstrukcja najkrótszych ścieżek** i kompletna analiza
- ✅ **Szczegółowe wyniki** z obliczeniami złożoności

### 📊 Typy Grafów
- 🔄 **Grafy skierowane** - ze strzałkami kierunkowymi
- ↔️ **Grafy nieskierowane** - połączenia dwukierunkowe
- 🎲 **Losowe wagi krawędzi** - wartości całkowite 1-14
- 📈 **Skalowalny rozmiar** - zalecane 5-20 wierzchołków

### 🖥️ Interfejs Użytkownika
- 🎨 **Aplikacja pełnoekranowa** z profesjonalnym układem
- 🔧 **Proste kontrolki** - tylko ustaw wierzchołki i punkt startowy
- 📊 **Kompleksowe wyniki** - ścieżki, kroki i analiza złożoności
- 🌐 **Dwujęzyczny interfejs** - obsługuje oba typy grafów

## 🛠️ Stos Technologiczny

| Technologia | Przeznaczenie | Wersja |
|-------------|---------------|--------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Główny język programowania | 3.12+ |
| ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) | Graficzny interfejs użytkownika | Wbudowany |
| ![NetworkX](https://img.shields.io/badge/NetworkX-Grafy-orange) | Wizualizacja grafów | 3.0+ |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-Wykresy-red) | Renderowanie grafów | 3.7+ |
| ![PyInstaller](https://img.shields.io/badge/PyInstaller-Exe-blue) | Tworzenie pliku wykonywalnego | 5.0+ |

## 🚀 Pobieranie

### Gotowy Plik Wykonywalny

**Użytkownicy Windows**: Pobierz samodzielny plik wykonywalny (nie wymaga instalacji Pythona)

📥 **[DijkstryApp.exe](dist/dijkstryApp.exe)** 

> **⚠️ Uwaga Bezpieczeństwa**: Windows może wyświetlić ostrzeżenie dla niepodpisanych plików wykonywalnych. Kliknij "Więcej informacji" → "Uruchom mimo to".

### Wymagania Systemowe
- 🖥️ **System**: Windows 10/11 (64-bit)
- 💾 **RAM**: Minimum 512 MB
- 💿 **Miejsce**: 50 MB wolnego miejsca
- 🖼️ **Wyświetlacz**: Rozdzielczość minimum 1024x768

## 🔧 Instalacja

Po prostu pobierz i uruchom `dijkstryApp.exe` - nie wymaga dodatkowej konfiguracji!

*Kod źródłowy jest również dostępny w tym repozytorium dla programistów.*

## 💻 Użytkowanie

### Przewodnik Szybkiego Startu

1. **Uruchom Aplikację**
   - Kliknij dwukrotnie `dijkstryApp.exe`
   - Aplikacja otwiera się w trybie pełnoekranowym

2. **Skonfiguruj Graf**
   - Wprowadź liczbę wierzchołków (zalecane 5-15)
   - Wybierz typ grafu: **Skierowany** lub **Nieskierowany**
   - Kliknij **"Wygeneruj graf"**

3. **Uruchom Algorytm**
   - Wprowadź numer wierzchołka startowego (0 do n-1)
   - Kliknij **"Uruchom algorytm Dijkstry"**
   - Zobacz szczegółowe wyniki krok po kroku

### 🎮 Kontrolki Interfejsu

| Kontrolka | Funkcja |
|-----------|---------|
| **Liczba wierzchołków** | Ustaw rozmiar grafu |
| **Typ grafu (radio)** | Wybierz skierowany/nieskierowany |
| **Wygeneruj graf** | Utwórz losowy graf |
| **Wierzchołek startowy** | Wybierz punkt początkowy algorytmu |
| **Uruchom algorytm** | Wykonaj algorytm Dijkstry |
| **Zamknij aplikację** | Wyjdź z programu |

### 📊 Analiza Wyników

Aplikacja wyświetla:
- **Tabelę Najkrótszych Ścieżek** - odległości i ścieżki do wszystkich wierzchołków
- **Wykonanie Krok po Kroku** - szczegółowy postęp algorytmu
- **Analizę Złożoności** - obliczenia O(V²) dla twojego grafu
- **Podsumowanie Wydajności** - osiągalne wierzchołki i statystyki

## 🧮 Przegląd Algorytmu

### Algorytm Dijkstry - Wyjaśnienie

**Cel**: Znajdowanie najkrótszych ścieżek od wierzchołka źródłowego do wszystkich innych wierzchołków w grafie ważonym z nieujemnymi wagami krawędzi.

**Jak działa**:
1. **Inicjalizacja** odległości (0 dla startu, ∞ dla pozostałych)
2. **Wybór** nieodwiedzonego wierzchołka o minimalnej odległości
3. **Aktualizacja** odległości do sąsiadów jeśli znaleziono krótszą ścieżkę
4. **Powtarzanie** aż wszystkie osiągalne wierzchołki zostaną przetworzone

**Złożoność Czasowa**: 
- Nasza implementacja: **O(V²)** - optymalna dla gęstych grafów
- Wersja z kopcem binarnym: **O((V+E)log V)** - lepsza dla rzadkich grafów
- Kopiec Fibonacciego: **O(E + V log V)** - teoretyczne optimum

**Złożoność Pamięciowa**: **O(V)** dla tablic odległości i poprzedników

### Praktyczne Zastosowania

- 🗺️ **Nawigacja GPS** - znajdowanie najkrótszych tras jazdy
- 🌐 **Routing Sieciowy** - routing pakietów w sieciach komputerowych
- 🎮 **AI w Grach** - pathfinding dla postaci
- 📦 **Logistyka** - optymalizacja tras dostaw
- 🔗 **Sieci Społeczne** - najkrótsze ścieżki połączeń

## 📚 Kompletna Dokumentacja

📄 **[Pełna Dokumentacja (DOCX)](DijkstryApp_PL.docx)**

Kompletna dokumentacja zawiera:
- Szczegółową teorię algorytmu i podstawy matematyczne
- Przykład krok po kroku z grafem 5-wierzchołkowym
- Kompleksową analizę złożoności z wykresami
- Pełny podręcznik użytkownika i specyfikacje techniczne

## 📄 Licencja

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.

**Podsumowanie Licencji MIT**: Wolne do użytku, modyfikacji i dystrybucji. Zachowaj tylko oryginalną notę o prawach autorskich.

## 👨‍💻 Autor

**Sebastian Ciborowski**

- 🎓 Student & Entuzjasta Informatyki 
- 💼 Specjalizacja w Cyberbezpieczeństwie, Pythonie & AI.
- 🔗 GitHub: [@sebastian-c87](https://github.com/sebastian-c87)

---

<div align="center">

**⭐ Jeśli ten projekt pomógł Ci zrozumieć algorytm Dijkstry, rozważ oznaczenie go gwiazdką!**

**Stworzone z ❤️ dla edukacji i nauki**

</div>
