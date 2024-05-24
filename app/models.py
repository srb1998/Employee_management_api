from app.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    ext_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable =True)

    def __repr__(self):
        return f'<Employee {self.name}>'