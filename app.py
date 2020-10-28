from flask import Flask, render_template, request, jsonify
from subprocess import check_output, STDOUT, DEVNULL, run as sprun
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

@app.route('/api/tester/target', methods=['GET', 'POST', 'DELETE'])
def target():
    if request.method == 'GET':
        if request.args.get('name'):
            return jsonify(tester.targets[request.args.get('name')])
        return jsonify(tester.targets)
    elif request.method == 'POST':
        tgt = { 'name': request.args.get('name'), 'ip': request.json['ip'] }
        return jsonify({'success': tester.add_tgt(tgt)})
    elif request.method == 'DELETE':
        tgt = request.args.get('name')
        return jsonify({'success': tester.del_tgt(tgt)})

@app.route('/api/tester/actions/run', methods=['POST'])
def run():
    c = request.json['cmd'].replace('^DIR^', tester.path + '/.gbscan')
    print('[RUN]', c)
    return jsonify({'success': sprun(c.split(), stdout=DEVNULL).returncode == 0})

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