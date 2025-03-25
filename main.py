import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from graph import Graph

class GraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafo")
        self.setGeometry(100, 100, 800, 600)

        self.graph = Graph()
        self.graph.create()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Draw the graph
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.draw_graph()

        # Select for the source vertex
        self.source_combo = QComboBox()
        self.source_combo.addItems(self.graph.G.nodes)
        self.source_combo.setPlaceholderText("Selecione o vértice de origem")
        self.layout.addWidget(self.source_combo)
        
        # Select for the target vertex
        self.target_combo = QComboBox()
        self.target_combo.addItems(self.graph.G.nodes)
        self.target_combo.setPlaceholderText("Selecione o vértice de destino")
        self.layout.addWidget(self.target_combo)

        # Type of path
        self.weight_combo = QComboBox()
        self.weight_combo.addItems(["Tempo mais rápido", "Distância mais curta"])
        self.weight_combo.setPlaceholderText("Selecione o tipo de caminho")
        self.layout.addWidget(self.weight_combo)
        
        # Button to find the custom path
        self.find_path_button = QPushButton("Encontrar caminho")
        self.find_path_button.clicked.connect(self.find_shortest_path)
        self.layout.addWidget(self.find_path_button)
        
        # Result of the path
        self.result_label = QLabel("Resultado")
        self.layout.addWidget(self.result_label)
        
    def draw_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        self.graph.draw(ax)
        self.canvas.draw()
        
    def find_shortest_path(self):
        source = self.source_combo.currentText()
        target = self.target_combo.currentText()
        weight = self.weight_combo.currentText()
        if weight == "Tempo mais rápido":
            path = self.graph.path(source, target, weight=True)
        else:
            path = self.graph.path(source, target, weight=False)
        self.result_label.setText(f"O caminho mais curto de {source} a {target} foi encontrado: {' -> '.join(path)}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GraphApp()
    widget.show()
    sys.exit(app.exec())