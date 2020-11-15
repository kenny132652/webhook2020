from flask import Flask
from redis import Redis

app = Flask(_name_)
redis = Redis(host="redis")

@app.route ("/")
def hello():
    visits = redis.incr('counter')
    html = "<h3>Hello World!</h3>" \
            "<b>Visits:</b> {visits}" \
            "<br/>"
    return html.format(visits=visits)

if_name_== "_main_":
    app.run(host="0.0.0.0", port=80)
