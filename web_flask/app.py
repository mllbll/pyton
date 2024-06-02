from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('frame2.html')


# @app.route('/about')
# def about():
#     return render_template('page_1.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/user')
def user():
    return 'User page'


if __name__ == '__main__':
    app.run(debug=True)
