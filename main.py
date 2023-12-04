from flask import Flask, render_template,jsonify

app = Flask(__name__)

courses = [
  {
    "id" : 1,
   "title": "Python Programming",
    "course_description": "Learn Python Programming",
    "location" : "Blue nile institute ",
    "course_price": 500,
    "start_date": "10 March 2023",
    "course_image": "https://www.python.org/static/img/python-logo.png"
  },
  {
    "id" : 2,
     "title": "oracle database Administrator",
      "course_description": "Learn DBA , SQL , PLSQL ",
      "location" : "Gazera university ",
      "course_price": 1000,
      "start_date": "12 january 2023",
      "course_image": "https://www.oracle.com/a/ocom/img/rc08-1982.png"
  },
  {
    "id" : 3,
     "title": "visual basic dot net",
    "course_description": "Object orented lanaguge using C## , .net",
    "location" : "Tech 200 institute",
      "course_price": 2000,
     "start_date": "11 May 2022",
  }
]
@app.route('/api/courses')
def list_courses():
  return jsonify(courses)
@app.route('/')
def home():
  return render_template("index.html",all_courses = courses )


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
