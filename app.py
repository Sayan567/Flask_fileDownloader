from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('admin_panel'))

@app.route('/admin_panel', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('admin_panel'))

    files = os.listdir(UPLOAD_FOLDER)
    return render_template('admin_panel.html', files=files)

@app.route('/download_file/<path:filename>')
def download_file(filename):
    try:
        return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=filename, as_attachment=True)
    except Exception as e:
        print(e)
        return "Internal Server Error", 500


@app.route('/read_file/<path:filename>')
def read_file(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(filepath)
        else:
            return "File format not supported.", 400

        return render_template('read_file.html', data=df.to_dict('records'))
    except Exception as e:
        print(e)
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)

