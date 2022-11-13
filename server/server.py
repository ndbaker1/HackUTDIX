from lib import *

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("preparing utd encoded class data...")

print("fetching class id's...")
id_set = set()
for page in range(0, 500, 20):
    items = fetch_class_ids(page)
    if items is None:
        break
    id_set.update(items)

print(f'fetched {len(id_set)} classes.')

print("fetching class descriptions...")
class_details = {
    class_id: fetch_class_data(class_id)
    for class_id
    in id_set
}

print("encoding class descriptions...")
class_descriptions_encoded = {
    class_id: encode_text(details['description'])
    for class_id, details
    in class_details.items()
}

print("finished preparing class data!")

from enum import Enum
class FilterParams(Enum):
    NUM_min_level = 'min course level'
    NUM_max_level = 'max course level'

def class_filter(class_id, filter_params: dict):
    details = class_details[class_id]

    if FilterParams.NUM_min_level.value in filter_params:
        if int(details['course_number'][0]) < int(filter_params[FilterParams.NUM_min_level.value]):
            return False

    if FilterParams.NUM_max_level.value in filter_params:
        if int(details['course_number'][0]) > int(filter_params[FilterParams.NUM_max_level.value]):
            return False

    return True

@app.get('/params')
def field_params():
    return [(item.name, item.value) for item in FilterParams]

@app.post('/search/text')
def text():
    posting_description = request.json['description']
    filter_params = request.json['filter_params']

    print(request.json)

    filtered_class_encodings = {
        class_id: enc
        for class_id, enc
        in class_descriptions_encoded.items()
        if class_filter(class_id, filter_params)
    }

    sorted_class_recommendations = compute_similarity(
        encode_text(posting_description),
        filtered_class_encodings,
    )

    return {
        'records': [
            { 'class_details': class_details[rec[0]], 'score': rec[1].item() }
            for rec in sorted_class_recommendations
        ]
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')