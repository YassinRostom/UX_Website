from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

# Create Home Page
@core.route('/')
def index():
    return render_template('index.html')

# Create MOT Page
@core.route('/mot')
def mot():
    return render_template('mot.html')

# Create Servicing Page
@core.route('/servicing')
def servicing():
    return render_template('servicing.html')

# Create About Us Page
@core.route('/about')
def about():
    return render_template('about.html')

# Create Contact Us Page
@core.route('/contact')
def contact():
    return render_template('contact.html')

#  Create Online Booking Page
@core.route('/booking')
def booking():
    return render_template('booking.html')

# Create 404 Page
@core.route('/info')
def info():
    return render_template('info.html')