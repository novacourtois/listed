import jinja2
from flask import Flask, request, render_template
app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('templates/')

def get_db(databasename='tasklist', username='postgres', password='thisisapass'):
	return psycopg2.connect(database=databasename,
		user=username, password=password)

# @app.route('/')
# def hello():
# 	return render_template('show_entries.html', entries=entries)

@app.route('/')
def show_entries():
    # cur = g.db.execute('select title, text from entries order by id desc')
    # entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # return render_template('show_entries.html', entries=entries)
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    return render_template('show_entries.html', entries=[{'description':'Walk Dog', 'priority':'2', 'due_date':'12/14/2014', 'status':'incomplete'},{'description':'Do Homework', 'priority':'5', 'due_date':'12/14/2014', 'status':'incomplete'},{'description':'Do Laundry', 'priority':'3', 'due_date':'12/14/2014', 'status':'incomplete'},{'description':'Read Book', 'priority':'1', 'due_date':'12/14/2014', 'status':'incomplete'}])

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

# @app.route('/user', methods = ['POST'])
# def create_user():
# 	conn = get_db()
# 	username = request.form['username']
# 	password = request.form['password']

# 	sql = ('insert into taskuser (username, password) values(%s, %s)')
# 	cur = conn.cursor()
# 	cur.execute(sql, (username, password))
# 	conn.commit()
# 	print('created a user called {0}'.format(username))

# @app.route('/tasks')
# def get_tasks():
# 	pass

# @app.route('/tasks', methods = ['POST'])
# def add_task():
# 	pass

if __name__ == "__main__":
	app.run(debug=True)

# curl localhost:5000/tasks