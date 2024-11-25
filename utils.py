import os

import networkx as nx
import pathlib
import matplotlib.pyplot as plt

_chapter = os.path.basename(os.getcwd())

if _chapter.startswith("Chapter"):
    BASE_FOLDER = os.environ.get("DATA_FOLDER", os.path.join(os.getcwd(), "..", "data"))
    DATA_DIR = pathlib.Path(BASE_FOLDER) / _chapter
else:
    BASE_FOLDER = os.environ.get("DATA_FOLDER", os.getcwd())
    DATA_DIR = pathlib.Path(BASE_FOLDER)

FIGURES_DIR = DATA_DIR / "figures"

default_edge_color = 'gray'
default_node_color = '#407cc9'
enhanced_node_color = '#f5b042'
enhanced_edge_color = '#cc2f04'

if not FIGURES_DIR.exists():
    FIGURES_DIR.mkdir(parents=True)

# draw a simple graph
def draw_graph(G, node_names={}, filename=None, node_size=50, layout = None, plot_weight=False):
    pos_nodes = nx.spring_layout(G) if layout is None else layout(G)
    node_names = {k: k for k, v in G.nodes.items()} if not node_names else node_names
    nx.draw(G, pos_nodes, with_labels=False, node_size=node_size, edge_color='gray')
    
    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1] + 0.08)
    
    nx.draw_networkx_labels(G, pos_attrs, labels=node_names, font_family='serif', font_size=20)

    if plot_weight:
        edge_labels=dict([((a,b,),d["weight"]) for a,b,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos_nodes, edge_labels=edge_labels)
    
    plt.axis('off')
    axis = plt.gca()
    axis.set_xlim([1.2*x for x in axis.get_xlim()])
    axis.set_ylim([1.2*y for y in axis.get_ylim()])
    
    if filename:
        plt.savefig(FIGURES_DIR / filename, format="png")


# draw enhanced path on the graph
def draw_enhanced_path(G, path_to_enhance, node_names={}, filename=None, layout = None):
    path_edges = list(zip(path_to_enhance,path_to_enhance[1:]))
    pos_nodes = nx.spring_layout(G) if layout is None else layout(G)

    plt.figure(figsize=(5,5),dpi=300)
    pos_nodes = nx.spring_layout(G)
    nx.draw(G, pos_nodes, with_labels=False, node_size=50, edge_color='gray')
    
    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1] + 0.08)
        
    nx.draw_networkx_labels(G, pos_attrs, labels=node_names, font_family='serif')
    nx.draw_networkx_edges(G,pos_nodes,edgelist=path_edges, edge_color='#cc2f04', style='dashed', width=2.0)
    
    plt.axis('off')
    axis = plt.gca()
    axis.set_xlim([1.2*x for x in axis.get_xlim()])
    axis.set_ylim([1.2*y for y in axis.get_ylim()])
    
    if filename:
        plt.savefig(FIGURES_DIR / filename, format="png")
