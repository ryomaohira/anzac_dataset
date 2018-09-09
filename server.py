from flask import Flask, request, redirect, render_template
import jinja2

app = Flask(__name__, static_url_path='', static_folder='www')
www_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('www')
])
app.jinja_loader = www_loader # add /www to template search path


@app.route('/')
@app.route('/page')
@app.route('/page/')
def index():
    return redirect('/page/search')


@app.route('/page/<page>')
def pages(page):
    try:
        return render_template('root.html', page=page)
    except jinja2.exceptions.TemplateNotFound as e:
        if e.name.endswith('.html'):
            # We tried to navigate to an unknown page
            return render_template('root.html', page='pagenotfound',
                                   origpage=page)


@app.route('/<path:path>')
def resources(path):
    return send_from_directory('', path)
