from flask import Flask, render_template, request
from graph import Graph
import visualizer
import time

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        start = request.form["src-link"]
        dest = request.form["dst-link"]
        graph = Graph(str(start), str(dest))
        graph.get_graph()
        
        # start_time_q = time.time()
        # quantum
        # end_time_q = time.time()
        # elapsed_time_q = end_time_q - start_time_q
        start_time_d = time.time()
        graph.shortest_path = graph.find_shortest_djikstra()
        end_time_d = time.time()
        print(graph.shortest_path)
        elapsed_time_d = (end_time_d - start_time_d) * 1000000
        return render_template('post.html', time_d=str(elapsed_time_d), time_q='0')
    else:
        return render_template('index.html')
        
@app.route("/post", methods=["POST", "GET"])
def post():
    if request.method == "POST":
        start = request.form["src-link"]
        dest = request.form["dst-link"]
        graph = Graph(str(start), str(dest))
        graph.get_graph()
        
        # start_time_q = time.time()
        # quantum
        # end_time_q = time.time()
        # elapsed_time_q = end_time_q - start_time_q
        start_time_d = time.time()
        graph.shortest_path = graph.find_shortest_djikstra()
        end_time_d = time.time()
        print(graph.shortest_path)
        elapsed_time_d = (end_time_d - start_time_d) * 1000000
        return render_template('post.html', time_d=str(elapsed_time_d), time_q='0')
    
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)