from flask import Flask, request, abort
import json
import csv

app = Flask(__name__)


@app.route('/list')
def get_list():
    with open('my_csv.csv') as my_file:
        all_data = [{k: v for k, v in row.items()}
                    for row in csv.DictReader(my_file, skipinitialspace=True)]
    if request.args:
        new_df = [i for i in all_data if i['product_name'] == request.args.get('product_name')]
        if len(new_df) == 0:
            abort(404)
    else:
        new_df = all_data
    return json.dumps(new_df)


@app.route('/add', methods=['POST'])
def add():
    data = request.form.to_dict()
    with open('my_csv.csv') as my_file:
        all_data = [{k: v for k, v in row.items()}
                    for row in csv.DictReader(my_file, skipinitialspace=True)]
    if data not in all_data:
        with open('my_csv.csv', 'a', newline=None) as my_file:
            dict_writer = csv.DictWriter(my_file, delimiter=',', fieldnames=all_data[0].keys())
            dict_writer.writerow(data)
        return 'OK', 200
    return 'Already exists', 400


if __name__ == '__main__':
    app.run(debug=True)
