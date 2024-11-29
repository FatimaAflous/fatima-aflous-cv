from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cv')
def afficher_cv():
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True)
