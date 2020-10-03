from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import jsonify
from flask import url_for
from flask import make_response

import models.writing.work as projects
import utils.util as util
import controllers.url_route as url_path

app = Flask(__name__, template_folder='./templates', static_folder='./static')


@app.route('/', methods=['GET', 'POST'])
def home():
    op = projects.UserOperation()
    titles = op.read_titles()
    url_title = [util.urlencode(title['title']) for title in titles]
    return render_template('home.html', titles=titles, range=range(len(url_title)), link=url_title)

@app.route('/<query_path>', methods=['GET', 'POST'])
def routing(query_path):
    return url_path.url_route(query_path)

@app.route('/<query_path>/<query_path2>', methods=['GET', 'POST'])
def w_routing(query_path, query_path2):
    return url_path.w_url_route(query_path, query_path2)

@app.route('/<query_path>/<query_path2>/<query_path3>', methods=['GET', 'POST'])
def t_routing(query_path, query_path2, query_path3):
    return url_path.t_url_route(query_path, query_path2, query_path3)

@app.route('/<query_path>/<query_path2>/<query_path3>/<query_path4>', methods=['GET', 'POST'])
def f_routing(query_path, query_path2, query_path3, query_path4):
    return url_path.f_url_route(query_path, query_path2, query_path3, query_path4)


if __name__ == '__main__':
    app.run()
