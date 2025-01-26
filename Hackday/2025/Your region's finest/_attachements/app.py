from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, \
    unset_jwt_cookies, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
import os, time, random, string, math

# I saw in the official _randommodule.c in which both time and pid are used to seed the random generator
# So that must be a good idea, right ? :) Just gonna do it simpler here, but should be as safe.

up = math.floor(time.time())
random.seed(up + os.getpid())

app = Flask(__name__)
app.config['SECRET_KEY'] = "".join(random.choice(string.printable) for _ in range(32))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/site.db'
app.config['JWT_SECRET_KEY'] = "".join(random.choice(string.printable) for _ in range(32))
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='static/images/default.png')
    published = db.Column(db.Boolean, default=True)


class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flag = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    products = Product.query.filter_by(published=True).all()
    return render_template('home.html', products=products)


@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    if not product.published:
        return render_template('product.html', error="Product not available anymore")

    return render_template('product.html', product=product)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=username, additional_claims={'favorite_product': None})
            resp = make_response(redirect(url_for('home')))
            set_access_cookies(resp, access_token)
            return resp
        else:
            return render_template('login.html', error="Username or password incorrect")
    return render_template('login.html')


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('home')))
    unset_jwt_cookies(resp)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('register.html', error="Username already taken")
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/preferences', methods=['GET', 'POST'])
@jwt_required()
def preferences():
    claims = get_jwt()
    current_user = get_jwt_identity()
    if request.method == 'POST':
        favorite_product_id = int(request.form['favorite_product'])
        product = Product.query.get(favorite_product_id)
        if not product:
            return render_template('preferences.html', error="Product does not exist", products=Product.query.all(),
                                   current_user=current_user)
        new_token = create_access_token(identity=get_jwt_identity(),
                                        additional_claims={'favorite_product': favorite_product_id})
        resp = make_response(redirect(url_for('home')))
        set_access_cookies(resp, new_token)
        return resp
    products = Product.query.all()
    return render_template('preferences.html', products=products, favorite_product=claims.get('favorite_product'),
                           current_user=current_user)


@app.route('/favorite_product_info')
@jwt_required()
def favorite_product_info():
    claims = get_jwt()
    favorite_product_id = claims.get('favorite_product')
    if favorite_product_id:
        favorite_product = Product.query.get(favorite_product_id)
        try:
            favorite_product = db.session.execute(
                text("SELECT * FROM product WHERE id = " + str(favorite_product_id))).fetchone()
        except Exception as e:
            return render_template('favorite_product_info.html', product=None, error=e)
        return render_template('favorite_product_info.html', product=favorite_product)

    return render_template('favorite_product_info.html', product=None)


@app.route('/check_auth')
@jwt_required(optional=True)
def check_auth():
    claims = get_jwt()
    return jsonify(logged_in=get_jwt_identity() is not None, favorite_product=claims.get('favorite_product')), 200


@app.route("/healthz")
def healthz():
    return jsonify(status="OK", uptime=time.time() - up)


def create_data():
    # clear all Product db
    db.session.query(Product).delete()

    product1 = Product(name=f'Space Cookie',
                       description='Cookies so delicate, they might just break! No need for brute force, one bite and they’ll melt right into your hands.',
                       price=random.randrange(10, 100))
    product2 = Product(name='Syringe', description='To, hum, inject yourself with medicine I guess ?',
                       price=random.randrange(10, 100))
    product3 = Product(name='Cool looking leaf', description='To add a nice scent to your house :)',
                       price=random.randrange(10, 100))
    with open("flag.txt", "r") as f:
        flag = Flag(flag=f.read().strip())
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(flag)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_data()
    app.run(host="0.0.0.0", port=5000)
