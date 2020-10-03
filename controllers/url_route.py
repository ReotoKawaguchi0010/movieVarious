import json
import ast

from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import jsonify

import models
import utils.util as util

def url_route(url_path):
    if url_path == 'test':
        return render_template('test.html')
    elif url_path == 'create_title':
        return create_title()
    elif url_path == 'option':
        return option()
    elif url_path == 'analysis':
        return analysis()
    elif url_path == 'schedule':
        return schedule()
    return render_template('error404.html')

def w_url_route(url_path, query_path2):
    if url_path == 'workspace':
        return workspace(query_path2)
    elif url_path == 'model':
        return model(query_path2)
    return render_template('error404.html')

def t_url_route(query_path, query_path2, query_path3):
    return render_template('error404.html')

def f_url_route(query_path, query_path2, query_path3, query_path4):
    return render_template('error404.html')


def create_title():
    if request.method == 'POST':
        work = models.writing.work.UserOperation()
        title = request.form['title']
        author = request.form['author']
        work.create_new_title(title, author)
        title = util.urlencode(title)
        return redirect(f'/workspace/{title}')
    return render_template('create_title.html')

def option():
    return render_template('option.html')

def analysis():
    return render_template('analysis.html')

def schedule():
    return render_template('schedule.html')

def model(query_path2):
    if request.method == 'GET':
        query_path2 = util.urldecode(query_path2)
        read_character = models.writing.character.UserOperation()
        read_letter_body = models.writing.letter_body.UserOperation()
        read_work = models.writing.work.UserOperation()
        re = read_letter_body.read_title(read_work.read_title_name(query_path2)['id'])
        characters = read_character.read_character_id(read_work.read_title_name(query_path2)['id'])
        re['characters'] = characters
        print(re)
        return jsonify(re), 200
    return 'test', 400

def workspace_post():
    save_character =  models.writing.character.UserOperation()
    save_letter_body = models.writing.letter_body.UserOperation()
    read_work = models.writing.work.UserOperation()
    if request.method == 'POST':
        req_json = request.json
        title_name = req_json['title']
        character_names = req_json['characters']
        letter_body = req_json['letterBody']
        page_num = req_json['page_num']
        title_id = read_work.read_title_name(title_name)['id']
        if save_letter_body.read_id(title_id) is None:
            save_character.create_new_character(character_names, title_id)
            characters_id = save_character.read_character_title(title_id)
            print(characters_id)
            save_letter_body.create_new_letter_body(title_id, page_num, letter_body, characters_id)
        else:
            save_character.update_character(title_id, character_names)
            save_letter_body.update_letter_body(title_id, letter_body)
        print(title_id)
        print(req_json)
    return 404

def workspace(w_url_path):
    op_title = models.writing.work.UserOperation()
    title_dict = op_title.read_title_name(util.urldecode(w_url_path))
    workspace_post()
    return render_template('create_story.html', title=title_dict['title'])