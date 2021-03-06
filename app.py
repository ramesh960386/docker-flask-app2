from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is landing page'


@app.route('/page/<id>')
def page(id):
    return 'This is page: '+str(int(id)+2)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()
