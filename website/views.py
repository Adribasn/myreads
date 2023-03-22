from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        formType = request.form.get('formType')

        if formType == 'searchForm':
            book = request.form.get('book')

            if book:
                url = f'https://www.googleapis.com/books/v1/volumes?q={book}&langRestrict=en'
                r = requests.get(url)
                data = r.json()
                for element in data['items']:
                    print(element['volumeInfo'])
                
                return render_template('search.html', user=current_user, data=data)
        else:
            title = request.form.get('title')
            authors = request.form.get('authors')
            publisher = request.form.get('publisher')
            date = request.form.get('date')
            description = request.form.get('description')
            print(title)
            print(authors)
            print(publisher)
            print(date)
            print(description)
        
    return render_template('search.html', user=current_user)