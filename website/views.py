from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

api_key = 'AIzaSyBsxxDP5ZK-lDQ-6N4VtEB96eMtefiS5WE'

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        book = request.form.get('book')

        if book:
            url = f'https://www.googleapis.com/books/v1/volumes?q={book}:keyes&key={api_key}'
            r = requests.get(url)
            data = r.json()
            for element in data['items']:
                print(element['volumeInfo']['title'])
        
    return render_template('search.html', user=current_user)