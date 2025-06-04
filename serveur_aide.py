from flask import Flask, render_template

app = Flask(__name__,
    template_folder='aide/templates',
    static_folder='aide/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import.html')
def import_page():
    return render_template('import.html')

@app.route('/export.html')
def export_page():
    return render_template('export.html')

# @app.route('/carte')
# def carte():
#     return render_template('carte.html')
#
# @app.route('/donnees')
# def donnees():
#     return render_template('donnees.html')
#
# @app.route('/outils')
# def outils():
#     return render_template('outils.html')

@app.route('/export')
def export():
    return render_template('export.html')

def run_server():
    app.run(port=5001)

def start_help_server():
    from threading import Thread
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()