from flask import Flask,render_template

app = Flask(__name__)
userlist = []
@app.route('/list/')

def list():
	return render_template('list.html',userlist=userlist)

@app.route('/user/<username>/')
	
def tuika(username):
	userlist.append(username)
	return render_template('tuika.html',message=username)
	
if __name__ == '__main__':
	app.debug = True
	app.run()