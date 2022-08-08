import json


def load_candidates(path) -> list[dict]:
    """загрузит данные из файла"""
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)


def get_by_id(candidate_id: int) -> dict:
    """вернет кандидата по id"""
    for candidate in load_candidates('candidates.json'):
        if candidate['id'] == candidate_id:
            return candidate


def get_by_name(candidate_name: str) -> list[dict]:
    """вернет кандидата по имени"""
    result = []
    for candidate in load_candidates('candidates.json'):
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_by_skill(skill_name: str) -> list[dict]:
    """вернет кандидатов по навыку"""
    result = []
    for candidate in load_candidates('candidates.json'):
        skills = candidate['skills'].lower().split(', ')
        for skill in skills:
            if skill_name == skill:
                result.append(candidate)
    return result


print(get_by_name('Sh'))
