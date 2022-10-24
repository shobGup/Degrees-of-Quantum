# import pydot
# from IPython.display import Image, display


# # [1: [1, 2, 3, 4]]
# def display(graph_data):
#     vizual = pydot.Dot(graph_type="digraph")
#     vizual.set_label("Link Graph")

#     # insert vertices
#     for v in graph_data:
#         vertex = pydot.Node(v)
#         # vertex.set_style("filled")
#         # vertex.set_fillcolor("#b2cede")
#         vizual.add_node(vertex)

#     # insert directed edges
#     for i in graph_data:
#         start = i
#         for j in graph_data[start]:
#             end = j
#             edge = pydot.Edge(start, end)
#         vizual.add_edge(edge)
        
#     im = Image(vizual.create_jpeg())
#     display(im)    

# # graph = pydot.Dot(graph_type = "graph")
# # graph.add_edge(pydot.Edge("1", "2"))
# # graph.add_edge(pydot.Edge("1", "3"))
# # graph.write("graph_output", format="png")