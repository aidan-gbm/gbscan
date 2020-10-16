from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shell')
def shell():
    return render_template('shell.html')

@app.route('/api/cmd', methods=['POST'])
def cmd():
    c = request.json['cmd']
    try:
        out = subprocess.check_output(c, stderr=subprocess.STDOUT, shell=True).decode()
    except Exception as err:
        out = str(err)

    return jsonify({'ret': out})

if __name__ == '__main__':
    app.run()