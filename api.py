import flask
import argparse
from flask import request
from joblib import load
from os.path import isfile

app = flask.Flask(__name__)
model = None

@app.route('/api/v1/text-triage')
def text_triage():
    args = request.args
    text_len = args['text_len']
    n_buyers = args['buyers']
    triage_type = args['type']

    if triage_type == 'simple':
        return simple_triage(text_len, n_buyers)
    elif triage_type == 'ml':
        return ml_triage(text_len, n_buyers)
    else:
        return 'unknown triage type'


def simple_triage(text_len, n_buyers):
    if int(text_len) > 50 and int(n_buyers) >= 10:
        return '1'
    else:
        return '0'


def ml_triage(text_len, n_buyers):
    probs = model.predict_proba([[int(text_len), int(n_buyers)]])
    return '{:1.6f}'.format(probs[0, 1])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('model', help='path to saved model')
    cli_args = parser.parse_args()
    return cli_args


if __name__ == '__main__':
    cli_args = parse_args()

    if isfile(cli_args.model):
        model = load(cli_args.model)
    else:
        raise FileNotFoundError('could not find model file.')

    app.run()