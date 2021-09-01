from flask import Flask, render_template
import socket
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.settings')
name = app.config['NAME']

reaction = ['awesome','nicee','splendid','great','bravo','fine job','excellent','spectacular','superb','super','purrfect','keep it up','excellent']

# start postgres connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users (db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40))
  value = db.Column(db.Integer)

  def __init__ (self,name,value):
    self.name = name
    self.value = value
# end postgres stuff

@app.route('/')
def index():    
    hostname = socket.gethostname()
    rawcommit = random.randint(100000,1000000)
    # try inserting to database
    try:
        new_user = Users(name=name, value=rawcommit)
        db.session.add(new_user)
        db.session.commit()
    except:
        pass
    #    
    commit = "{:,}".format(rawcommit)    
    return render_template('index.html', hostname=hostname, commit=commit, name=name, reaction=reaction[random.randint(0,12)])
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')