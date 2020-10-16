from flask import Flask, render_template, request, jsonify
from subprocess import check_output, STDOUT
from modules.tester import Tester
import sys

if not len(sys.argv) == 2:
        print('Usage: {} <Project Directory>'.format(sys.argv[0]))
        exit()

tester = Tester(sys.argv[1])
app = Flask(__name__, static_folder='static', static_url_path='')
app.config['DEBUG'] = True

#################
### TEMPLATES ###
#################

@app.route('/')
def index():
    return render_template('index.html', instance=tester.getInstance())

@app.route('/shell')
def shell():
    return render_template('shell.html')

#################
### API CALLS ###
#################

@app.route('/api/cmd', methods=['POST'])
def cmd():
    c = request.json['cmd']
    try:
        out = check_output(c, stderr=STDOUT, shell=True).decode()
    except Exception as err:
        out = str(err)

    return jsonify({'ret': out})

if __name__ == '__main__':
    app.run()