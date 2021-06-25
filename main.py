from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bb.sqlite'
db = SQLAlchemy(app)


class Bb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(40), nullable=False)
    nickname = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f'{self.id}) პერსონაჟი:{self.characters}; ზედმეტსახელი:{self.nickname}; დაბადების თარიღი:{self.birthday}'


# all_char = Bb.query.all()
# print(all_char)
# for each in all_char:
#     print(each.characters)

# b1 = Bb(characters='Hector Salamanca', nickname='Jimmy', birthday='07-21-1995')
# db.session.add(b1)
# db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/characters')
def characters():
    all_char = Bb.query.all()
    return render_template('characters.html', all_char=all_char)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


if __name__ == "__main__":
    app.run(debug=True)
