from flask import Flask, render_template, request, redirect, url_for, flash
from db_helper import DBHELPER





app = Flask(__name__)
app.secret_key = "Secret Key"
helper = DBHELPER()




#This is the index route where we are going to
#query on all our book data
@app.route('/')
def Index():
    all_data = helper.fetch_all()
    return render_template("index.html", books = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        book_name = request.form['book_name']

        helper.insert_user(name, email, phone,book_name)

        flash("Book Data Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update our book
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        id = request.form.get('id')
        new_name = request.form['name']
        new_email = request.form['email']
        new_phone = request.form['phone']
        book_name = request.form['book_name']

        helper.update_user(id,new_name, new_email, new_phone,book_name)
        flash("Book Data Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our book
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):

    helper.delete_user(id)
    flash("Book Data Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)