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


@app.post('/search/text')
def text():
    posting_description = request.json['description']
    sorted_class_recommendations = compute_similarity(
        encode_text(posting_description),
        class_descriptions_encoded,
    )

    return {
        'records': [
            { 'class_details': class_details[rec[0]], 'score': rec[1].item() }
            for rec in sorted_class_recommendations
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)