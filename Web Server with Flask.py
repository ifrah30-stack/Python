# Simple REST API with Flask
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# In-memory data store
books = [
    {'id': 1, 'title': 'Python Basics', 'author': 'John Doe', 'year': 2020},
    {'id': 2, 'title': 'Web Development', 'author': 'Jane Smith', 'year': 2021}
]

@app.route('/')
def home():
    return render_template('index.html')  # You'd need to create this template

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json.get('title'),
        'author': request.json.get('author'),
        'year': request.json.get('year')
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update({
            'title': request.json.get('title', book['title']),
            'author': request.json.get('author', book['author']),
            'year': request.json.get('year', book['year'])
        })
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
