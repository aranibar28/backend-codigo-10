from sesion10.app import db

class Movie(db.Model):
    id = db.Column("idMovie", db.Integer, primary_key = True)
    title = db.Column("Title", db.String(45))
    plot = db.Column("Plot", db.String(250))
    year = db.Column("Year", db.Integer)
    length = db.Column("Length", db.Integer)
    director = db.Column("Director", db.String(45))
    background = db.Column("Background", db.String(250))
    coverimage = db.Column("CoverImage", db.String(250))
    maincolor = db.Column("MainColor", db.String(45))

    def create_movie(**kwargs):
        new_movie = Movie(**kwargs)
        db.session.add(new_movie)
        db.session.commit()
