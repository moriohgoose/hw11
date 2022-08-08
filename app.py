from flask import Flask, request, render_template
import json
from utils import load_candidates
from utils import get_by_id
from utils import get_by_name
from utils import get_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates: list[dict] = load_candidates('candidates.json')
    return render_template('list.html', candidates=candidates)
    
    
@app.route('/candidate/<int:idx>')
def candidate_page(idx: int):
    candidate: dict = get_by_id(idx)
    if not candidate:
        return 'Кандидат не найден'
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name: str):
    candidates: list[dict] = get_by_name(candidate_name)
    if not candidates:
        return 'Кандидаты с таким именем не найдены'
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def search_by_skill(skill_name: str):
    candidates: list[dict] = get_by_skill(skill_name)
    if not candidates:
        return 'Кандидаты с таким навыком не найдены'
    return render_template('skill.html', candidates=candidates, skill=skill_name)


app.run()

