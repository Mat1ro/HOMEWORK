from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = get_all()
    result = get_information(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidate = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += get_information([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    candidate = get_by_skill(skill)
    result = get_information(candidate)
    return result


app.run(host='0.0.0.0', port=8000)
