from flask import Flask, render_template, redirect, url_for, request
from graph import Graph
import time

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        start = request.form["src-link"]
        dest = request.form["dst-link"]
        graph = Graph(url_for(start), url_for(dest))
        graph.get_paths()
        graph.print_graph()
        return redirect(url_for('post.html', graph=graph))
    else:
        return render_template('index.html')
        
@app.route("/post")
def post(graph):
    if request.method == "POST":
        start = request.form["src-link"]
        dest = request.form["dst-link"]
        graph = Graph(url_for(start), url_for(dest))
        graph.get_paths()
        return redirect(url_for('post.html', graph=graph))
    
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)