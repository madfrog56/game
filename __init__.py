from flask import Flask, render_template, request, session
app=Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('app.html')

@app.route('/test/<tempvar>')
def test(tempvar):
	return tempvar

@app.route('/login', methods=['POST'])
def login():
	user_id = request.form['user_id']
	user_pw = request.form['user_pw']
	if user_id == 'madfrog':
		if user_pw =='1234':
			session['logged_in'] = True
			return 'login success'
		else:
			return 'wrong password'
	else:
		return 'wrong id'


if __name__=='__main__':
	app.secret_key = 'dfddffffsdfsdfsdfds'
	app.run(debug=True, host='0.0.0.0')
