from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/<item>')
def carbon_offset(item):
    """
    this serves as a demo purpose
    :param item:
    :return: str
    """
    return "%s offsets over 9000 tons of carbon!" % item


@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})


@app.route('/')
def index():
    return "This is the snapcycle backend! Use the get method by typing the item name after the URL"


if __name__ == '__main__':
    app.run()
