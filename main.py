from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/get_ip', methods=['GET'])
def get_ip():
    client_ip = request.remote_addr
    return f'The client IP address is: {client_ip}'

@app.route('/exec_bash')
def exec_bash():
    script_path = '/home/kamizato/git/api/hello.sh'
    subprocess.run(['bash', script_path])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

