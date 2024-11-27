from flask import render_template, request, jsonify
from models import Person

def register_routes(app, db):

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            name = request.form.get("name")
            age = int(request.form.get("age"))
            job = request.form.get("job")

            # Creo un nuevo registro
            newPerson = Person(name=name, age=age, job=job)

            # Lo guardo en la base de datos
            db.session.add(newPerson)
            db.session.commit()
        
        people = Person.query.all()

        return render_template("index.html", people=people)

    @app.delete("/delete/<pid>")
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()

        people = Person.query.all()
        print(people)
        return render_template("index.html", people=people)