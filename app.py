import random
import string

from flask import Flask, render_template, redirect, abort
from flask_bootstrap import Bootstrap
import os

from forms import EditForm

app = Flask(__name__)


def gen_uuid():
    uuid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    if not os.path.exists('./notes'):
        os.mkdir('./notes')
    while os.path.isfile('./notes/{}.txt'.format(uuid)):
        uuid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    return uuid


@app.route('/', methods=['get', 'post'])
def index():
    form = EditForm()
    if form.validate_on_submit():
        uuid = gen_uuid()
        open('./notes/{}.txt'.format(uuid), 'w').write(form.content.data)
        return redirect('/' + uuid)
    return render_template('note/edit.html', form=form)


@app.route('/<note_id>', methods=['get', 'post'])
def edit(note_id):
    note_id = os.path.basename(note_id)
    note_path = './notes/{}.txt'.format(note_id)
    if os.path.isfile(note_path):
        form = EditForm()
        if form.validate_on_submit():
            open(note_path, 'w').write(form.content.data)
        else:
            form.content.data = open(note_path).read()
        return render_template('note/edit.html', form=form)
    else:
        abort(404)


app.secret_key = b'_5#y2L"F4Q8z\n\xeadawdqwac]/'
Bootstrap(app)
if __name__ == '__main__':
    app.run()
