from flask import Flask, render_template

app = Flask(__name__,
    template_folder='aide/templates',
    static_folder='aide/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import')
def import_page():
    return render_template('import.html')

@app.route('/export')
def export_page():
    return render_template('export.html')

@app.route('/cartes')
def cartes_page():
    return render_template('cartes.html')

def run_server():
    app.run(port=5001)

def start_help_server():
    from threading import Thread
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()