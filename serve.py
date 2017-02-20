from flask import Flask, jsonify, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# enter a new movie
@app.route('/enternew')
def enternew():
	return render_template('movie.html')

# add a movie to the database
@app.route('/addmovie', methods = {'POST'})
def addmovie():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	try:
		name = request.form['name']
		genre = request.form['genre']
		cur.execute('INSERT INTO movies(name,genre) VALUES(?,?)',(name,genre))
		conn.commit()
		message = 'Record Successfully Added'
	except:
		conn.rollback()
		message = 'Error in INSERT OPERATION'
	finally:
		return render_template('result.html',message=message)
		conn.close()


@app.route('/search')
def search():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	try:
		name = (request.args.get('name'),)
		cur.execute('SELECT * FROM movies WHERE name=?',name)
		conn.commit()
		message = cur.fetchall()
	except:
		message =('DataBase Error')
	finally:
		messageList=jsonify(message)
		conn.close()
		return messageList


#### Extra Credit ####
# retrieve a all movies from the database
@app.route('/movies')
def movies():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	try:
		
		cur.execute('SELECT * FROM movies')
		conn.commit()
		message = cur.fetchall()
	except:
		message =('Database Error')
	finally:
		messageList=jsonify(message)
		conn.close()
		return messageList	
		

app.run(debug=True)

