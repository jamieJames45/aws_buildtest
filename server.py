from bottle import route, run, default_app
import requests
application = default_app()

@route('/test')
def test():
    URL = "https://jsonplaceholder.typicode.com/todos/1"
    r = requests.get(url = URL)
    return r.json()


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
