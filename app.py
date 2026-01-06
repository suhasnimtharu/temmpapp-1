from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # render_template looks into the /templates folder automatically
    return render_template('index.html', title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)