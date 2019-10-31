from flask import Flask, render_template, escape

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/<name>/<target>')
def result(name, target):
  name = escape(name)
  target = escape(target)
  return 'Calling {} with {}'.format(name, target)

if __name__ == '__main__':
  app.run(debug=True)