import random
import tkinter as tk
from tkinter import messagebox, scrolledtext
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sys

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorytm Dijkstry - Znajdowanie Najkrótszych Ścieżek")
        # self.root.geometry("1000x900")  # Zwiększona wysokość dla instrukcji
        self.root.state('zoomed')
        
        self.graph = {}
        self.node_positions = {}
        self.create_widgets()
    
    def create_widgets(self):
        # Panel sterowania - góra
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(fill="x")
        
        # Liczba wierzchołków
        tk.Label(control_frame, text="Liczba wierzchołków:").grid(row=0, column=0, padx=5, pady=5)
        self.num_vertices_entry = tk.Entry(control_frame, width=10)
        self.num_vertices_entry.grid(row=0, column=1, padx=5, pady=5)
        self.num_vertices_entry.insert(0, "10")
        
        # Przycisk generowania grafu
        generate_button = tk.Button(control_frame, text="Generuj graf", command=self.initialize_graph, 
                                   bg="#4CAF50", fg="white")
        generate_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Wierzchołek startowy
        tk.Label(control_frame, text="Wierzchołek startowy:").grid(row=1, column=0, padx=5, pady=5)
        self.start_vertex_entry = tk.Entry(control_frame, width=10)
        self.start_vertex_entry.grid(row=1, column=1, padx=5, pady=5)
        self.start_vertex_entry.insert(0, "0")
        
        # Przycisk uruchomienia algorytmu
        run_button = tk.Button(control_frame, text="Uruchom algorytm", command=self.run_dijkstra,
                              bg="#2196F3", fg="white")
        run_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Przycisk zamknięcia
        exit_button = tk.Button(control_frame, text="Zamknij aplikację", command=self.exit_application,
                              bg="#F44336", fg="white")
        exit_button.grid(row=1, column=3, padx=5, pady=5)
        
        # NOWY KOD - opcje wyboru typu grafu
        graph_type_frame = tk.Frame(control_frame)
        graph_type_frame.grid(row=2, column=0, columnspan=4, pady=10)

        tk.Label(graph_type_frame, text="Typ grafu:").pack(side=tk.LEFT, padx=5)

        self.graph_type = tk.StringVar(value="skierowany")
        tk.Radiobutton(graph_type_frame, text="Skierowany", variable=self.graph_type, 
               value="skierowany").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(graph_type_frame, text="Nieskierowany", variable=self.graph_type, 
               value="nieskierowany").pack(side=tk.LEFT, padx=5)

        # Panel instrukcji
        instruction_frame = tk.LabelFrame(self.root, text="Instrukcja obsługi", padx=10, pady=5)
        instruction_frame.pack(fill="x", padx=10, pady=5)
        
        instructions = """
Instrukcja użytkownika:

1. Wprowadź liczbę wierzchołków grafu (np. 5-15 dla lepszej czytelności).
2. Wybierz typ grafu: skierowany lub nieskierowany.
3. Kliknij przycisk 'Generuj graf', aby utworzyć losowy graf z połączeniami.
4. Wprowadź numer wierzchołka startowego (od 0 do liczba_wierzchołków-1).
5. Kliknij 'Uruchom algorytm', aby znaleźć najkrótsze ścieżki z wybranego wierzchołka.
6. Wyniki pojawią się w górnym oknie - zobaczysz najkrótsze ścieżki oraz szczegółowe kroki algorytmu.
7. Aby zamknąć aplikację, kliknij przycisk 'Zamknij aplikację'.

Algorytm Dijkstry służy do znajdowania najkrótszej ścieżki od jednego wierzchołka do wszystkich pozostałych w grafie.
Algorytm przypisuje każdemu wierzchołkowi etykietę z aktualną odległością od źródła i aktualizuje ją,
gdy znajduje krótszą ścieżkę.
        """
        
        instruction_text = scrolledtext.ScrolledText(instruction_frame, height=8, wrap=tk.WORD)
        instruction_text.pack(fill="x", padx=5, pady=5)
        instruction_text.insert(tk.END, instructions)
        instruction_text.config(state="disabled")
        
        # Panel wyników - PIERWSZY, będzie na górze
        results_frame = tk.LabelFrame(self.root, text="Wyniki algorytmu", padx=10, pady=10)
        results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=12)
        self.results_text.pack(fill="both", expand=True)
        self.results_text.insert(tk.END, "Tu pojawią się wyniki algorytmu po jego uruchomieniu.\n")
        
        # Panel grafu - DRUGI, będzie na dole
        self.graph_frame = tk.LabelFrame(self.root, text="Wizualizacja grafu", padx=10, pady=10)
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Dodajemy label informacyjny w panelu grafu
        self.graph_label = tk.Label(self.graph_frame, text="Graf zostanie wyświetlony po wygenerowaniu")
        self.graph_label.pack(pady=15)
    
    def exit_application(self):
        """Całkowicie zamyka aplikację"""
        if messagebox.askokcancel("Zamknij", "Czy na pewno chcesz zamknąć aplikację?"):
            self.root.destroy()
            sys.exit(0)  # Całkowicie kończy proces Pythona
    
    def initialize_graph(self):
        try:
            num_vertices = int(self.num_vertices_entry.get())
            if num_vertices <= 0:
                messagebox.showerror("Błąd", "Liczba wierzchołków musi być dodatnia")
                return
            
            # Inicjalizacja grafu
            self.graph = {}
            for i in range(num_vertices):
                self.graph[i] = []
            
            # Generowanie pozycji wierzchołków
            self.node_positions = {}
            for i in range(num_vertices):
                angle = 2 * math.pi * i / num_vertices
                self.node_positions[i] = (0.8 * math.cos(angle), 0.8 * math.sin(angle))
            
            # Generowanie losowych krawędzi (2-3 razy więcej niż wierzchołków)
            min_edges = 1 * num_vertices
            max_edges = 3 * num_vertices
            target_edges = random.randint(min_edges, max_edges)
            
            edges_added = 0
            attempts = 0
            max_attempts = 1000
            
            is_directed = self.graph_type.get() == "skierowany"

            while edges_added < target_edges and attempts < max_attempts:
                start = random.randint(0, num_vertices - 1)
                end = random.randint(0, num_vertices - 1)
                if start != end:
                    weight = random.randint(1, 14) # round(random.uniform(1, 20), 1)
        
                    # Sprawdzamy, czy krawędź start -> end już istnieje
                    edge_exists = any(e[0] == end for e in self.graph[start])
        
                    if not edge_exists:
                        # Dodanie krawędzi w kierunku start -> end
                        self.graph[start].append((end, weight))
            
            # Jeśli graf nieskierowany, dodaj krawędź w drugą stronę
                        if not is_directed:
                # Sprawdź czy krawędź powrotna end -> start już istnieje
                            reverse_exists = any(e[0] == start for e in self.graph[end])
                            if not reverse_exists:
                                self.graph[end].append((start, weight))
            
                        edges_added += 1
    
                attempts += 1
            
            # Wyświetl informacje o wygenerowanym grafie w panelu wyników (górny panel)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Wygenerowano graf z {num_vertices} wierzchołkami i {edges_added} krawędziami.\n")
            self.results_text.insert(tk.END, "Przykładowe krawędzie:\n")
            
            count = 0
            for start, edges in self.graph.items():
                for end, weight in edges:
                    self.results_text.insert(tk.END, f"{start} → {end} (waga: {weight})\n")
                    count += 1
                    if count >= 30:
                        break
                if count >= 30:
                    break
            
            if edges_added > 30:
                self.results_text.insert(tk.END, f"... i {edges_added - 30} więcej krawędzi.\n")
            
            # Rysuj graf w dolnym panelu
            self.draw_graph()
            
            messagebox.showinfo("Info", f"Wygenerowano graf z {num_vertices} wierzchołkami i {edges_added} krawędziami")
            
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną liczbę wierzchołków")
    
    def draw_graph(self):
        # Usuń poprzedni wykres
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Utwórz nowy graf
        # NOWY KOD - sprawdzenie typu grafu
        is_directed = self.graph_type.get() == "skierowany"

# Utwórz odpowiedni typ grafu dla NetworkX
        if is_directed:
            G = nx.DiGraph()  # Graf skierowany
        else:
            G = nx.Graph()    # Graf nieskierowany

# Dodaj wierzchołki
        for node in self.graph:
            G.add_node(node)

# Dodaj krawędzie do NetworkX
        if is_directed:
    # Graf skierowany - dodaj wszystkie krawędzie jak są
            for start, edges in self.graph.items():
                for end, weight in edges:
                    G.add_edge(start, end, weight=weight)
        else:
    # Graf nieskierowany - dodaj tylko unikalne krawędzie
            added_edges = set()
            for start, edges in self.graph.items():
                for end, weight in edges:
            # Utwórz unikalny identyfikator krawędzi (mniejszy, większy)
                    edge_id = (min(start, end), max(start, end))
                    if edge_id not in added_edges:
                        G.add_edge(start, end, weight=weight)
                        added_edges.add(edge_id)

# Rysuj graf
        fig, ax = plt.subplots(figsize=(8, 5))
        pos = self.node_positions
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=10, font_weight='bold', 
                arrows=is_directed, arrowsize=15 if is_directed else 0, 
                arrowstyle='->' if is_directed else None)
        
        # Dodaj etykiety wag
        edge_labels = {}
        for start, edges in self.graph.items():
            for end, weight in edges:
                edge_labels[(start, end)] = weight
                
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        
        # Umieść wykres w interfejsie
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def dijkstra(self, graph, start):
        # Inicjalizacja
        distances = {}
        for vertex in graph:
            distances[vertex] = float('infinity')
        distances[start] = 0
        
        predecessors = {}
        for vertex in graph:
            predecessors[vertex] = None
        
        unvisited = list(graph.keys())
        steps = []
        
        # Zapisz stan początkowy
        steps.append({
            'description': 'Inicjalizacja',
            'distances': distances.copy(),
            'unvisited': unvisited.copy(),
            'current': None
        })
        
        # Główna pętla algorytmu
        while unvisited:
            # Znajdź wierzchołek o najmniejszej odległości
            current = min(unvisited, key=lambda v: distances[v])
            
            # Jeśli odległość to nieskończoność, pozostałe wierzchołki są nieosiągalne
            if distances[current] == float('infinity'):
                break
            
            # Zapisz ten krok
            steps.append({
                'description': f'Wybrano wierzchołek {current}',
                'distances': distances.copy(),
                'unvisited': unvisited.copy(),
                'current': current
            })
            
            # Usuń wierzchołek z listy nieodwiedzonych
            unvisited.remove(current)
            
            # Sprawdź sąsiadów
            for neighbor, weight in graph[current]:
                # Oblicz nową odległość
                distance = distances[current] + weight
                
                # Jeśli znaleziono krótszą ścieżkę
                if distance < distances[neighbor]:
                    old_distance = distances[neighbor]
                    distances[neighbor] = distance
                    predecessors[neighbor] = current
                    
                    # Zapisz krok aktualizacji
                    steps.append({
                        'description': f'Aktualizacja odległości do {neighbor}: {old_distance if old_distance != float("infinity") else "∞"} → {distance}',
                        'distances': distances.copy(),
                        'unvisited': unvisited.copy(),
                        'current': current
                    })
        
        return distances, predecessors, steps
    
    def reconstruct_path(self, predecessors, target):
        # Odtwarzanie ścieżki
        path = []
        current = target
        
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]
        
        return path
    
    def add_summary_to_results(self, distances, predecessors, start_vertex):
        """Dodaje podsumowanie wyników algorytmu"""
        # Znajdź wierzchołek najdalej położony od startowego (maksymalna odległość)
        max_distance = -1
        farthest_vertex = None
        for vertex, dist in distances.items():
            if dist != float('infinity') and dist > max_distance:
                max_distance = dist
                farthest_vertex = vertex
        
        # Licz statystyki
        reachable_vertices = 0
        unreachable_vertices = 0
        sum_distances = 0
        for vertex, dist in distances.items():
            if dist != float('infinity'):
                reachable_vertices += 1
                sum_distances += dist
            else:
                unreachable_vertices += 1
        
        avg_distance = sum_distances / reachable_vertices if reachable_vertices > 0 else 0
        
        # Przygotuj tekst podsumowania
        summary = f"\n{'=' * 30}\nPODSUMOWANIE WYNIKÓW ALGORYTMU\n{'=' * 30}\n\n"
        
        summary += f"Wierzchołek startowy: {start_vertex}\n"
        summary += f"Liczba osiągalnych wierzchołków: {reachable_vertices}\n"
        summary += f"Liczba nieosiągalnych wierzchołków: {unreachable_vertices}\n"
        summary += f"Średnia odległość do osiągalnych wierzchołków: {avg_distance:.2f}\n\n"
        
        if farthest_vertex is not None:
            path = self.reconstruct_path(predecessors, farthest_vertex)
            summary += f"Najdalszy osiągalny wierzchołek: {farthest_vertex} (odległość: {max_distance})\n"
            summary += f"Najkrótsza ścieżka do tego wierzchołka: {' → '.join(map(str, path))}\n\n"
        
        # Dodaj informacje o złożoności obliczeniowej
        summary += f"{'=' * 30}\nZŁOŻONOŚĆ ALGORYTMU\n{'=' * 30}\n\n"
        
        # Dane grafu
        v = len(self.graph)  # liczba wierzchołków
        e = sum(len(edges) for edges in self.graph.values())  # liczba krawędzi
        
        summary += f"Dane grafu:\n"
        summary += f"- Liczba wierzchołków (V): {v}\n"
        summary += f"- Liczba krawędzi (E): {e}\n\n"
        
        summary += f"Złożoność czasowa algorytmu Dijkstry:\n"
        summary += f"- Nasza implementacja (z tablicą): O(V²) = O({v}²) = O({v*v})\n"
        summary += f"- Z kolejką priorytetową: O((V+E)log V) = O(({v}+{e})log {v})\n\n"
        
        summary += f"Złożoność pamięciowa: O(V) = O({v})\n\n"
        
        summary += f"Wyjaśnienie:\n"
        summary += f"- V² wynika z faktu, że dla każdego z V wierzchołków przeszukujemy tablicę V wierzchołków\n"
        summary += f"  aby znaleźć wierzchołek o najmniejszej odległości.\n"
        summary += f"- Implementacja z kolejką priorytetową byłaby efektywniejsza dla rzadkich grafów.\n"
        summary += f"- Algorytm Dijkstry działa efektywnie dla grafów z nieujemnymi wagami krawędzi.\n"
        
        # Dodaj podsumowanie do wyników
        self.results_text.insert(tk.END, summary)
    
    def run_dijkstra(self):
        if not self.graph:
            messagebox.showerror("Błąd", "Najpierw wygeneruj graf")
            return
        
        try:
            start_vertex = int(self.start_vertex_entry.get())
            
            if start_vertex not in self.graph:
                messagebox.showerror("Błąd", f"Wierzchołek startowy poza zakresem (0-{len(self.graph)-1})")
                return
            
            # Uruchomienie algorytmu
            distances, predecessors, steps = self.dijkstra(self.graph, start_vertex)
            
            # Wyświetlanie wyników - w górnym panelu
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Wyniki algorytmu Dijkstry z wierzchołka {start_vertex}:\n\n")
            
            # Tabela najkrótszych ścieżek
            self.results_text.insert(tk.END, f"{'Cel':<10}{'Odległość':<15}{'Ścieżka'}\n")
            self.results_text.insert(tk.END, "-" * 50 + "\n")
            
            for vertex in sorted(self.graph.keys()):
                path = self.reconstruct_path(predecessors, vertex)
                path_str = " → ".join(str(v) for v in path) if path else "Nieosiągalny"
                
                distance = distances[vertex]
                distance_str = str(distance) if distance != float('infinity') else "∞"
                
                self.results_text.insert(tk.END, f"{vertex:<10}{distance_str:<15}{path_str}\n")
            
            # Szczegółowe kroki
            self.results_text.insert(tk.END, "\nSzczegółowe kroki algorytmu:\n\n")
            
            for i, step in enumerate(steps):
                self.results_text.insert(tk.END, f"Krok {i+1}: {step['description']}\n")
                
                # Wyświetl odległości
                self.results_text.insert(tk.END, "Odległości: ")
                for v in sorted(step['distances'].keys()):
                    d = step['distances'][v]
                    d_str = "∞" if d == float('infinity') else str(d)
                    self.results_text.insert(tk.END, f"{v}:{d_str} ")
                
                self.results_text.insert(tk.END, "\n\n")
            
            # Dodaj podsumowanie wyników
            self.add_summary_to_results(distances, predecessors, start_vertex)
            
            # Przewiń na początek tekstu
            self.results_text.see("1.0")
            
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawny wierzchołek startowy")

def main():
    root = tk.Tk()
    app = DijkstraApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_application)  # Obsługa zamknięcia okna
    root.mainloop()

if __name__ == "__main__":
    main()
