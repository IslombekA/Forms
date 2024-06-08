from cs50 import SQL
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

db = SQL("sqlite:///text.db")



@app.route('/', methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        last_name = request.form.get("last_name")
        first_name = request.form.get("first_name")    
        db.execute("INSERT INTO persons(first_name, last_name)VALUES(?,?)", first_name, last_name)       

        return redirect('/registrants')

    return render_template('index.html')


@app.route('/registrants')
def registrants():
    persons = db.execute("SELECT * FROM persons")
    return render_template('registrants.html', persons=persons)

@app.route('/delete', methods=["POST"])
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM persons WHERE id = ?", id)
    return redirect('/registrants')

if __name__ == "__main__":
    app.run(debug="True")