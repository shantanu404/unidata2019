from flask import Flask, render_template, escape, jsonify
from compare import lagging, INSTITUITIONS

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', inst=INSTITUITIONS)

@app.route('/api/<merit>/<target>/<other>/<cutoff>')
def result(merit, target, other, cutoff):
  merit = escape(merit)
  target = escape(target)
  try:
    return jsonify({'data': lagging(int(merit), target, other, int(cutoff))})
  except ValueError:
    return jsonify({'error': 'Invalid `roll` or `instituition`'}), 500
  except Exception:
    return jsonify({'error': 'Uh oh! Looks like the server crashed. Contact the developers!'}), 500

@app.errorhandler(404)
def not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)