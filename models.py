# THIS FILE IS FOR DATA MODELS

from app import db



class Task(db.Model):
    # NOW WE DEFINE THE COLUMNS
    
    # THE PRIMARY KEY
    id = db.Column(db.Integer, primary_key = True)

    # TO DEFINE THE TTLE OF THE TASK
    title = db.Column(db.String, nullable=False)

    # TO NOTE DOWN THE DATE OF THE TASK
    date = db.Column(db.Date, nullable=False)

    # FUNCTION TO REPRESENT DATA
    def __repr__(self):
        return f'{self.title} WAS CREATED ON {self.date}'
