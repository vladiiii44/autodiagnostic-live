from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.config.from_object(Config)

CONTACT_INFO = {
    'name': 'Павел',
    'phone': '+375 (29) 628-50-00',
    'phone_raw': '+375296285000',
    'work_hours': 'Пн-Пт: 9:00-20:00, Сб-Вс: 10:00-18:00',
    'address': 'Минск и область'
}

SERVICES = [
    {
        'id': 1,
        'title': 'Компьютерная диагностика',
        'description': 'Считывание и расшифровка кодов ошибок, проверка всех систем автомобиля',
        'icon': 'fas fa-laptop-code'
    },
    {
        'id': 2,
        'title': 'Диагностика двигателя',
        'description': 'Проверка компрессии, системы зажигания, топливной системы, датчиков',
        'icon': 'fas fa-cogs'
    },
    {
        'id': 3,
        'title': 'Диагностика Mercedes',
        'description': 'Диагностика дилерским мультиплексором',
        'icon': 'fas fa-star',
        'special': True
    },
    {
        'id': 4,
        'title': 'Диагностика электрооборудования',
        'description': 'Проверка генератора, стартера, проводки, аккумулятора, освещения',
        'icon': 'fas fa-bolt'
    },
    {
        'id': 5,
        'title': 'Диагностика подвески',
        'description': 'Проверка амортизаторов, сайлентблоков, шаровых опор, ШРУСов',
        'icon': 'fas fa-car'
    },
    {
        'id': 6,
        'title': 'Диагностика трансмиссии',
        'description': 'Проверка коробки передач, сцепления, мехатроника',
        'icon': 'fas fa-exchange-alt'
    }
]
CONTACT_INFO = {
    'name': 'Павел',
    'phone': '+375 (29) 628-50-00',
    'phone_raw': '+375296285000',
    'work_hours': 'Пн-Пт: 9:00-20:00, Сб-Вс: 10:00-18:00',
    'address': 'Минск и область'
}

SERVICES = [
    {
        'id': 1,
        'title': 'Компьютерная диагностика',
        'description': 'Считывание и расшифровка кодов ошибок, проверка всех систем автомобиля',
        'icon': 'fas fa-laptop-code'
    },
@app.route('/')
def index():
    return render_template('index.html', services=SERVICES[:3], contact=CONTACT_INFO)

@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES, contact=CONTACT_INFO)

@app.route('/about')
def about():
    return render_template('about.html', contact=CONTACT_INFO)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        car_model = request.form.get('car_model')
        year = request.form.get('year')
        service_type = request.form.get('service_type')
        message = request.form.get('message')
        
        print(f"Новая заявка: {name}, {phone}, {car_model}")
        
        return redirect(url_for('thanks', name=name))
    
    return render_template('contact.html', contact=CONTACT_INFO)

@app.route('/thanks')
def thanks():
    name = request.args.get('name', '')
    return render_template('thanks.html', name=name, contact=CONTACT_INFO)

if __name__ == '__main__':
    app.run(debug=True)
