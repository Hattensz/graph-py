import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    # Create a graph
    def create(self):
        self.G = nx.Graph()
        elist = [('A', 'B', 10), ('A', 'E', 20), ('A', 'F', 5), ('A', 'G', 15), ('A', 'H', 5), ('A', 'D', 20), ('B', 'D', 10), ('B', 'C', 5), ('B', 'J', 5), ('B', 'I', 15), ('B', 'H', 20), ('C', 'D', 5), ('D', 'E', 10), ('E', 'F', 5), ('F', 'G', 10), ('G', 'H', 5), ('H', 'I', 20), ('I', 'J', 10), ('J', 'C', 15)]
        self.G.add_weighted_edges_from(elist)


    def draw(self, ax):
        # Invert the weights
        for u, v, data in self.G.edges(data=True):
            data["inv_weight"] = 1/data["weight"]

        # Options for draw the graph
        options_nodes = {
            "node_size": 1000,
            "node_color": "white",
            "linewidths": 5,
            "edgecolors": "darkgray",
        }
        options_edges = {
            "edge_color": "black",
            "width": 5,
        }
        options_label ={
            "font_size": 18,
            "font_family": "sans-serif",
            "font_color": "black",
            "font_weight": "bold",
        }
        
        # Draw the graph
        self.pos = nx.spring_layout(self.G, seed=21, weight="inv_weight")
        nx.draw_networkx_nodes(self.G, self.pos, **options_nodes, ax=ax)
        nx.draw_networkx_edges(self.G, self.pos, **options_edges, ax=ax)
        nx.draw_networkx_labels(self.G, self.pos, **options_label, ax=ax)
        edge_labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels, ax=ax)

    # Algorithms for the chosen path
    def path(self, source, target, weight=True):
        if weight:
            path = nx.shortest_path(self.G, source, target, weight="weight")
        else:
            path = nx.shortest_path(self.G, source, target, weight=None)
        return path