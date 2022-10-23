from scraper import scraper
# import timer

class Vertex:
    url = ""
    title = ""
    connected_vertices = [] # list of Vertexes
    def __init__(self, url, title, connections):
        self.url = url
        self.title = title
        self.connected_vertices = connections
    def get_url(self):
        return self.url
    def get_title(self):
        return self.title

class Path:
    def __init__(self):
        self.path = []
    
    def get_path(self):
        return self.path
    
    def add(self, node):
        self.path.append(node)
    
    def remove(self, edge):
        self.path.remove(edge)

class Graph:
    paths = []          # list of Paths
    shortest_path = Path()
    djikstra_time = 0
    quant_time = 0
    def __init__(self, start_vert, end_vert):
        self.start = start_vert
        self.end = end_vert
    def find_shortest_djikstra(self, start, end):
        # start timer
        self.shortest_path = []
        # end timer
    def find_shortest_quantum(self, start, end):
        # start timer
        self.shortest_path = []
        # end timer
    def get_djik_time(self):
        return self.djikstra_time
    def get_quant_time(self):
        return self.quant_time
    def add(self, path):
        self.paths.append(path)
    def get_paths(self):
        path = Path()
        path.add(self.start)
        scrap = scraper(self.start, self.end)
        self.dfs(self.start, path, 0, scrap)
    def dfs(self, article, path, depth, scraper):
        if depth < 6:
            edges = scraper.scrapeArticle(article)
            if self.end in edges:
                path.add(self.end)
                self.add(path)
            else:
                for edge in edges:
                    path.add(edge)
                    self.dfs(edge, path, depth + 1, scraper)
                    path.remove(edge)
    def print_graph(self):
        print (self.paths)