from scraper import scraper
import time

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
    
    def removeLast(self):
        self.path.pop()

class Graph:
    paths = []          # list of Paths
    shortest_path = Path()
    def __init__(self, start_vert, end_vert):
        self.start = start_vert
        self.end = end_vert
        self.graph = {("static/" + start_vert):[]}
    def find_shortest_djikstra(self):
        parents = self.find_shortest()
        path = ["static/" + self.end]
        current = "static/" + self.end
        while parents[current]:
            path.insert(0, parents[current])
            current = parents[current]
        return path

        # end timer
    def find_shortest_quantum(self, start, end):
        # start timer
        self.shortest_path = []
        # end timer
    def add(self, path):
        self.paths.append(path)
    def build_graph(self, article, scraper):
        article = "static/" + article
        edges = scraper.scrapeArticle(article)
        for edge in edges:
            if article not in self.graph:
                self.graph[article] = ["static/" + edge['href']]
            else:
                self.graph[article].append("static/" + edge['href'])
        for edge in edges:
            edge2 = "static/" + edge['href']
            if edge2 not in self.graph:
                self.build_graph(edge['href'], scraper)
    def print_graph(self):
        print(self.graph)
    def get_graph(self):
        scrap = scraper(self.start, self.end)
        self.build_graph(self.start, scrap)
    def find_shortest(self):
        start = "static/" + self.start
        parents = {start : None}
        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        while queue:
            current = queue.pop(0)
            for dest in self.graph[current]:
                if dest not in visited:
                    visited.add(dest)
                    parents[dest] = current
                    queue.append(dest)
        return (parents)
        # queue = [("static/" + self.start, ["static/" + self.start])]
        # while queue:
        #     (vertex, path) = queue.pop(0)
        #     for next in set(self.graph[vertex]) - set(path):
        #         if next == ("static/" + self.end):
        #             yield (path + [next])
        #         else:
        #             queue.append((next, path + [next]))

    # def dfs(self, article, path, depth, scraper):
    #     counter = 0
    #     if depth < 3:
    #         edges = scraper.scrapeArticle(article)
    #         if self.end in edges:
    #             path.add(self.end)
    #             self.add(path)
    #         else:
    #             for edge in edges:
    #                 path.add(edge)
    #                 self.dfs(edge, path, depth + 1, scraper)
    #                 path.removeLast()
    #                 counter += 1
    #                 print("counter: " + str((counter)))