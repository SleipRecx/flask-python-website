from app import db
from models import BlogPost

#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("good","i am good."))
db.session.add(BlogPost("well","i am well."))


#commit changes
db.session.commit()