from flask import Flask, render_template
import socket
import random

app = Flask(__name__)
app.config.from_object('config.settings')
name = app.config['NAME']

reaction = ['awesome','nicee','splendid','great','bravo','fine job','excellent','spectacular','superb','super','purrfect','keep it up','excellent']

@app.route('/')
def index():    
    hostname = socket.gethostname()
    commit = "{:,}".format(random.randint(100000,1000000))
    
    return render_template('index.html', hostname=hostname, commit=commit, name=name, reaction=reaction[random.randint(0,12)])
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')