from flask import Flask, render_template, jsonify

courses = [{
    "id": 1,
    "title": "Python Programming",
    "course_description": "Learn Python Programming",
    "location": "Blue nile institute ",
    "course_price": 500,
    "start_date": "10 March 2023",
    "course_image": "https://www.python.org/static/img/python-logo.png"
}, {
    "id": 2,
    "title": "oracle database Administrator",
    "course_description": "Learn DBA , SQL , PLSQL ",
    "location": "Gazera university ",
    "course_price": 1000,
    "start_date": "12 january 2023",
    "course_image": "https://www.oracle.com/a/ocom/img/rc08-1982.png"
}, {
    "id":
    3,
    "title":
    "visual basic dot net",
    "course_description":
    "Object orented lanaguge using C## , .net",
    "location":
    "Tech 200 institute",
    "course_price":
    2000,
    "start_date":
    "11 May 2022",
    "course_image":
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/VB.NET_Logo.svg/130px-VB.NET_Logo.svg.png"
}, {
    "id":
    4,
    "title":
    "Web devloper",
    "course_description":
    "shoud learn HTML , JAVA ,CSS ",
    "location":
    "Tech 200 institute",
    "course_price":
    2000,
    "start_date":
    "11 May 2022",
    "course_image":
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/VB.NET_Logo.svg/130px-VB.NET_Logo.svg.png"
}]
started_lates = [{
    "id": 1,
    "title": "Python Programming",
    "location": "Blue nile institute",
    "duraion": " 3 Months.",
    "studnet_count": 30,
    "empty_seats": 20
}, {
    "id": 2,
    "title": "C# Programming",
    "location": "Alfateh for Computer ",
    "duraion": "1 Months.",
    "studnet_count": 30,
    "empty_seats": 10
}, {
    "id": 3,
    "title": "Oracle DBA ",
    "location": "Alfateh for Computer ",
    "duraion": "2 Weeks ",
    "studnet_count": 25,
    "empty_seats": 5
}, {
    "id": 4,
    "title": "Web Developer for Begineer  ",
    "location": "Alfateh for Computer ",
    "duraion": "2 months ",
    "studnet_count": 40,
    "empty_seats": 15
}]

app = Flask(__name__)


@app.route('/api/courses')
def list_courses():
  return jsonify(courses)


@app.route('/')
def home():
  return render_template("index.html",
                         all_courses=courses,
                         started=started_lates)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
