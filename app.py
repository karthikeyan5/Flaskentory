from flask import Flask, render_template, url_for, redirect, abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from wtforms import validators, Form
import os

app = Flask(__name__)
app.config['demo'] = os.environ.get('IS_DEMO', True)
app.config['is_production'] = os.environ.get('IS_PRODUCTION', False)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '0012345679')

# set bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'lumen'

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://root:toor@localhost/flaskentory')
app.config['SQLALCHEMY_ECHO'] = not (app.config['is_production'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = not (
    app.config['is_production'])
db = SQLAlchemy(app)


class ModelViewProduct(ModelView):
    can_delete = False
    can_view_details = True
    can_export = True
    export_types = ['csv', 'xls']
    column_labels = dict(name='Product Name',
                         description='Product Description')
    column_filters = ['id', 'name', 'description',
                      'time_created', 'time_updated']
    page_size = 20
    column_exclude_list = ['time_created', 'time_updated']
    column_searchable_list = ['name', 'description']
    column_editable_list = ['name', ]
    form_excluded_columns = ['time_created', 'time_updated']
    form_args = {
        'name': {
            'label': 'Product Name',
            'validators': [validators.DataRequired()]
        },
        'description': {
            'label': 'Product Description'
        }
    }


class ModelViewLocation(ModelView):
    can_delete = False
    can_view_details = True
    can_export = True
    export_types = ['csv', 'xls']
    column_labels = dict(name='Location Name', other_details='Other Details')
    column_filters = ['id', 'name', 'other_details',
                      'time_created', 'time_updated']
    page_size = 20
    column_exclude_list = ['time_created', 'time_updated']
    column_searchable_list = ['name', 'other_details']
    column_editable_list = ['name', ]
    form_excluded_columns = ['time_created', 'time_updated']
    form_args = {
        'name': {
            'label': 'Location Name',
            'validators': [validators.DataRequired()]
        },
        'other_details': {
            'label': 'Other Details'
        }
    }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(1000))
    time_created = db.Column(db.TIMESTAMP, server_default=db.func.now())
    time_updated = db.Column(
        db.TIMESTAMP, onupdate=db.func.now(), server_default=db.func.now())

    def __str__(self):
        return "{}, {}".format(self.name)

    def __repr__(self):
        return "{}: {}".format(self.id, self.__str__())


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    other_details = db.Column(db.String(1000))
    time_created = db.Column(db.TIMESTAMP, server_default=db.func.now())
    time_updated = db.Column(
        db.TIMESTAMP, onupdate=db.func.now(), server_default=db.func.now())

    def __str__(self):
        return "{}, {}".format(self.name)

    def __repr__(self):
        return "{}: {}".format(self.id, self.__str__())


admin = Admin(app, name='Inventory Management',
              template_mode='bootstrap3', url='/')
admin.add_view(ModelViewProduct(Product, db.session, category="Master"))
admin.add_view(ModelViewLocation(Location, db.session, category="Master"))


def create_demo_data():
    products_demo_data = [
        {'name': 'PSLV-3S', 'description': 'Polar Satellite Launch Vehicle'},
        {'name': 'GSLV Mk.III', 'description': 'Geosynchronous Satellite Launch Vehicle'},
        {'name': 'Starship Enterprise',
            'description': 'USS Enterprise (NCC-1701-A)'},
        {'name': 'USS Voyager', 'description': 'NCC-74656'},
        {'name': 'Vanguard', 'description': 'Generational ship'},
        {'name': 'Venture Star',
            'description': 'Known for transporting humans to the moon Pandora'},
        {'name': 'Jupiter 2', 'description': 'A nuclear-powered spacecraft '},
        {'name': 'Event Horizon', 'description': 'gravity drive exploration starship'},
        {'name': 'Axiom', 'description': 'the Buy n Large starliner designed to provide a temporary home for humanity'},
        {'name': 'Athena', 'description': 'starship which transported humans to a space station orbiting the planet Solaris'},
        {'name': 'Raza', 'description': 'An Interstellar spaceship'},
        {'name': 'Millennium Falcon',
            'description': 'Designed by the Corellian Engineering Corporation (CEC), the highly modified YT-1300 is durable, modular, and is stated as being the second-fastest vessel in the Star Wars canon'},
        # {'name': '', 'description': ''},
        # {'name': '', 'description': ''},
        # {'name': '', 'description': ''},
        # {'name': '', 'description': ''},
    ]

    for demo_product in products_demo_data:
        product = Product()
        product.name = demo_product['name']
        product.description = demo_product['description']
        db.session.add(product)

    location_demo_data = [
        {'name': 'Vikram Sarabhai Space Centre',
            'other_details': 'Thiruvananthapuram , Kerala'},
        {'name': 'Satish Dhawan Space Centre ',
            'other_details': 'Sriharikota, Andhra Pradesh'},
        {'name': 'Abdul Kalam Island', 'other_details': 'Balasore, Odisha'},
        {'name': 'Rocket Launch Site Berlin',
            'other_details': 'Berlin-Reinickendorf '},
        {'name': 'Cape Canaveral Air Force Station', 'other_details': 'Florida'},
        {'name': 'Vandenberg Air Force Base', 'other_details': 'California'},
        {'name': 'Kennedy Space Center', 'other_details': 'Florida'},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
        # {'name':'', 'other_details': ''},
    ]

    for demo_location in location_demo_data:
        location = Location()
        location.name = demo_location['name']
        location.other_details = demo_location['other_details']
        db.session.add(location)

    db.session.commit()

    return


if __name__ == "__main__":
    if app.config['demo']:
        db.drop_all()
        db.create_all()
        create_demo_data()
    debug = not (app.config['is_production'])
    app.run(debug=True)
