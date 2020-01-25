from flask import Flask, current_app
app = Flask(__name__)

@app.route('/models/<model>')
def load_model(model):
    htmlpage = '''
    <!doctype HTML>
    <html>
    <script src="https://aframe.io/releases/1.0.0/aframe.min.js"></script>
    <script src="https://raw.githack.com/jeromeetienne/AR.js/2.1.4/aframe/build/aframe-ar.js"></script>

    <body style='margin : 0px; overflow: hidden;'>
        <a-scene embedded arjs>
            <a-marker id="memarker" type="pattern" url="../static/patterns/pattern-earth.patt" vidhandler>
                <a-entity obj-model="obj: url(../static/models/{}.obj); mtl: url(../static/models/{}.mtl)" scale="0.1 0.1 0.1"> </a-entity>
            </a-marker>
            <a-entity camera></a-entity>
        </a-scene>
    </body>

    </html>
    '''.format(model,model)
    return htmlpage

@app.route('/poly/<model>')
def load_poly(model):
    htmlpage = '''
    <!doctype HTML>
    <html>
    <script src="https://aframe.io/releases/1.0.0/aframe.min.js"></script>
    <script src="https://raw.githack.com/jeromeetienne/AR.js/2.1.4/aframe/build/aframe-ar.js"></script>
    <script src="../static/js/aframe-google-poly-component.min.js"></script>
    <body style='margin : 0px; overflow: hidden;'>
        <a-scene embedded arjs google-poly="api_key:AIzaSyCz39baiiaQ6cT146JzAN91YbHVIyf0fz4">
            <a-marker id="memarker" type="pattern" url="../static/patterns/pattern-earth.patt" vidhandler>
                <a-google-poly src="{}" scale="0.1 0.1 0.1"></a-google-poly>
            </a-marker>
            <a-entity camera></a-entity>
        </a-scene>
    </body>

    </html>
    '''.format(model)
    return htmlpage


@app.route('/<page>')
def load_page(page):
    return current_app.send_static_file('{}.html'.format(page))

@app.route('/')
def hello_world():
    return current_app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=4000)
    # https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html