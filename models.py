from app import db

print("Se crea un modelo")
class Person(db.Model):
    __tablename__ = "people"

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.String(40))

    def __repr__(self):
        return f"Person {{\n  pid = {self.pid}\n  name = {self.name}\n  age = {self.age}\n  job = {self.job}\n}}"