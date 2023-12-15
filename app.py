from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yolov7_custom/<path:filename>', methods=['GET'])
def model_files(filename):
    return send_from_directory('yolov7_custom', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
