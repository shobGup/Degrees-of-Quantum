from flask import Flask, render_template
from graph import Graph

start = "https://en.wikipedia.org/wiki/Quantum_computing"
end = "https://en.wikipedia.org/wiki/Quantum_logic_gate"
graph = Graph(start, end)
graph.get_paths()
graph.print_graph()

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)