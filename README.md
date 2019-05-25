> Note: This software has been written only for technology demonstration purpose. If you are looking for a real Inventory Management System or a Full-fledged ERP, head over to the awesome [ERPNext](https://github.com/frappe/erpnext).

# Flaskentory

A Sample Inventory Management Web Application made with [Flask](http://flask.pocoo.org/) and [PostgreSQL](https://www.postgresql.org)

Visit https://flaskentory.herokuapp.com/ for demo version of the application.

### Instruction to install and run the application.
1. Install python3.7.
2. Download this repository by using `git clone https://github.com/karthikeyan5/Flaskentory.git`.
3. Install the dependencies using `cd Flaskentory && python3.7 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`.
4. Set environment `DATABASE_URL` to you PostgreSQL DB. 
     > eg: `postgresql://username:password@localhost/dbname`
5. Start the app using `python app.py`. 
6. Visit [http://localhost:5000/](http://localhost:5000/) from your browser to access the app.

## Views:
Below are the views available in the application and their screenshot. 
- ### Product:
This view helps to manage products:
![Product page](docs/screenshots/product_master.png?raw=true "Product View")

- ### Location:
This view helps to manage Warehouse Locations:
![Location page](docs/screenshots/location_master.png?raw=true "Location View")

- ### Product Movement:
This view helps to make data entry of product movement:
![Product Movement page](docs/screenshots/product_movement.png?raw=true "Product Movement View")

## Reports:
The reports are shown below.
- ### Product Stock:
This reports shows the balance quantity in each location:
![Product Stock page](docs/screenshots/Product_stock.png?raw=true "Product Stock View")
