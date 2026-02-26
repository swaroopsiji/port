from flask import Flask,render_template,jsonify

app=Flask(__name__)
@app.route("/",methods = ["GET"])

def home():
    return render_template("index.html",name="hii123") 


@app.route("/get_data",methods = ["GET"])
def get_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="flask_app"

    )

    cursor = db.cursor()
    cursor.execute("*SELECT* FROM user_auth*")

    data=cursor.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)