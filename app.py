from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def search_ligand(keyword):
    conn = sqlite3.connect("ligands.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, structure_path FROM ligands WHERE name LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        results = search_ligand(keyword)
        return render_template("result.html", results=results, keyword=keyword)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
        
