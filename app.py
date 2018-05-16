import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


app = Flask(__name__)

app.config.from_object(__name__)



app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flask_laser.db'),
    SECRET_KEY= 'dev key',
    USERNAME='tetracore',
    PASSWORD='agate'
))

app.config.from_envvar('flask_laser_SETTINGS', silent=True) 

def connect_db():
    """Connects to the SQLite database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


        

@app.cli.command('initdb')
def init_db_command():
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def start_up():
    """Fetches database when app starts up so you have access to the data"""
    db = get_db()
    cur = db.execute("select * from spectra order by image_path desc")
    spectra = cur.fetchall()
    return render_template('index.html', spectra=spectra)


@app.route('/AcquireDark', methods=['GET', 'POST'])
def AcquireDark():
 

def Acquire():



@app.route('/Clear', methods=['GET', 'POST'])
def Clear():



@app.route('/autoBio', methods=['GET', 'POST'])
def autoBio():
