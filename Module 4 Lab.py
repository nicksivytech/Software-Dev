from flask import Flask, jsonify, request

app = Flask(__name__)

# simple list to store books
books = [
    {
        "id": 1,
        "book_name": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publisher": "Allen & Unwin"
    }
]

# get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# get one book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"error": "Book not found"})


# add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book)


# update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            data = request.json
            book["book_name"] = data["book_name"]
            book["author"] = data["author"]
            book["publisher"] = data["publisher"]
            return jsonify(book)
    return jsonify({"error": "Book not found"})


# delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"})


if __name__ == '__main__':
    app.run(debug=True)
