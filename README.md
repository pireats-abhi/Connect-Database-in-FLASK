# Problem the solution
step 1: exactly write whole code
step 2: install offline mysqlclient
step 3: install flask_mysqldb
step 4: install pyyaml
step 5: open mysql workbench
step 6: make sure user authentication type is 'standard' if not then create a new user
step 7: now run the app.py

# How to fetch all data from a table
cur = mysql.connection.cursor()
resultValue = cur.execute("SELECT * FROM users")
if resultValue > 0:
  userDetails = cur.fetchall()
  return render_template('users.html', userDetails=userDetails)
