import pydot

# [1: [1, 2, 3, 4]]
def display(graph_data):
    graph_viz = pydot.Dot(graph_type="directed")
    graph_viz.set_label("Link Graph")

    # insert vertices
    for v in graph_data.shortest_path:
        vertex = pydot.Node(v)
        vertex.set_style("filled")
        vertex.set_fillcolor("#b2cede")
        graph_viz.add_node(vertex.get_title())

    # insert directed edges
    for i in range(len(graph_data.shortest_path)-1):
        start = graph_data.shortest_path[i]
        end = graph_data.shortest_path[i+1]
        edge = pydot.Edge(start.get_title(), end.get_title())
        graph_viz.add_edge(edge)
        
    
    graph_viz.write_png('static/graph_output.png')
    