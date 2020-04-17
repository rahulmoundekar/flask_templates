from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'


@app.route("/", methods=['GET', 'POST'])
def dashboard():
    return render_template('index.html')


@app.route("/about", methods=['GET', 'POST'])
def aboutUs():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contactUs():
    return render_template('contact.html')


@app.route("/register", methods=['GET', 'POST'])
def employees():
    return render_template('form.html')


# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')

# manager.run()
