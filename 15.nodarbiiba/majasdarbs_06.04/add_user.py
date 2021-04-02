from flask import Flask, request, render_template
import profile
app = Flask(__name__)
@app.route('/', methods=['GET'])
@app.route('/add_user/', methods=['POST'])
def index(add_user=None):
    return render_template(profile.html)

if __name__ == "__main__":
    app.run(debug=True)
