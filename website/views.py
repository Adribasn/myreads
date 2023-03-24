from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from flask_login import login_required, current_user
import requests
from . import db
from .models import Book
import json

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
                print(data)
                return render_template('search.html', user=current_user, data=data)
        else:
            title = request.form.get('title')
            authors = request.form.get('authors')
            publisher = request.form.get('publisher')
            date = request.form.get('date')
            rating = request.form.get('rating')
            description = request.form.get('description')
            imageLink = request.form.get('imageLink')

            new_book  = Book(title=title, authors=authors, publisher=publisher, date=date, rating=rating, description=description, imageLink=imageLink, user_id=current_user.id)
            print(new_book.title)
            db.session.add(new_book)
            db.session.commit()
            flash('Saved new book!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template('search.html', user=current_user)

@views.route('/delete-book', methods=['POST'])
def delete_book():
    data = json.loads(request.data)
    bookId = data['bookId']
    book = Book.query.get(bookId)
    if book:
        if book.user_id == current_user.id:
            db.session.delete(book)
            db.session.commit()

    return jsonify({})
