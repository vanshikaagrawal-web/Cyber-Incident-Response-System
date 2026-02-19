import networkx as nx
import matplotlib.pyplot as plt

def build_threat_graph(logs):
    G = nx.Graph()

    for log in logs:
        src = log.get("source_ip")
        dst = log.get("destination_ip")

        if src and dst:
            G.add_edge(src, dst)

    if len(G.nodes()) == 0:
        print("No graph data available.")
        return []

    compromised_node = max(G.degree, key=lambda x: x[1])[0]
    print("Compromised Node Selected:", compromised_node)

    blast = nx.single_source_shortest_path_length(G, compromised_node, cutoff=2)
    subgraph = G.subgraph(blast.keys())
    print("Affected Nodes:", list(blast.keys()))

    plt.figure(figsize=(6, 4))
    nx.draw(subgraph, with_labels=True)
    plt.title("Blast Radius")
    plt.show()

    return list(blast.keys())
