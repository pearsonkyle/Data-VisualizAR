from flask import Flask, current_app
app = Flask(__name__)

@app.route('/<page>')
def load_page(page):
    return current_app.send_static_file('{}.html'.format(page))

@app.route('/')
def hello_world():
    return current_app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=4000,ssl_context='adhoc')
    # create script to animate 3D models 
    # blender folder? 
    # static examples 