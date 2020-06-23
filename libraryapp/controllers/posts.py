from collections import namedtuple
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from libraryapp.services.posts import PostsService


posts_controller = Blueprint(name='posts_controller', import_name=__name__)

db = []
Message = namedtuple('Message','text tag')
messages = []

#Основа
@posts_controller.route('/', methods=['GET'])
def source():
    return render_template('index.html')

#Поиск книги
@posts_controller.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)
#Поиск книги 2
@posts_controller.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag'] #текст это что, тэг это где
    return (PostsService.find_books(text, tag))

#Список всех книг
@posts_controller.route("/get_all_books", methods=['GET'])
def get_all_books():
    return (PostsService.get_posts())

#добавить книгу
@posts_controller.route('/add_book2', methods=['GET'])
def add_book2():
    return render_template('add_book2.html')
#добавить книгу 2
@posts_controller.route("/add_book123", methods=['POST'])
def add_book123():
    author = request.form['author']
    book_name = request.form['book_name']
    publishing_house = request.form['publishing_house']
    year = request.form['year']
    annotation = request.form['annotation']
    rubricator = request.form['rubricator']
    PostsService.create_post(author, book_name, publishing_house, year, annotation, rubricator)
    return ('Kniga Dobavlena')

#найти и изменить книгу
@posts_controller.route('/сhange_book', methods=['GET'])
def сhange_book():
    return render_template('сhange_book.html')
#найти и изменить книгу2
@posts_controller.route('/сhange_book2', methods=['POST'])
def сhange_book2():
    author = request.form['author']
    book_name = request.form['book_name']
    publishing_house = request.form['publishing_house']
    year = request.form['year']
    annotation = request.form['annotation']
    rubricator = request.form['rubricator']
    gde2 = request.form['gde2']
    chto2 = request.form['chto2']
    PostsService.find_change_book(author, book_name, publishing_house, year, annotation, rubricator, chto2, gde2)
    return render_template('сhange_book.html')

