import json


def get_all():
    with open('candidates.json', 'r', encoding="utf-8") as candidates:
        candidates = json.load(candidates)
    return candidates


def get_information(candidates):
    result = '<pre>'
    for candidate in candidates:
        result += f'{candidate["name"]}\n' \
                  f'{candidate["position"]}\n' \
                  f'{candidate["skills"]}\n' \
                  f'<pre>'
    return result


def get_by_pk(pk_name):
    '''Возвращает кандидата по pk, если такого кандитата не было найдено, выведет неправильный pk'''

    candidates = get_all()
    for candidate in candidates:
        if candidate["pk"] == pk_name:
            return candidate
    return 'Wrong pk'


def get_by_skill(skill_name):
    '''Возвращает списко кандидатов по скиллам'''

    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill_name in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result
