from collections import namedtuple
from flask import Blueprint, request, render_template
from libraryapp.services.posts import PostsService
from libraryapp.database_settings.db_settings import Refill_db_books
from libraryapp import logger


posts_controller = Blueprint(name='posts_controller', import_name=__name__)

Message = namedtuple('Message','text tag')
messages = []


#Основа
@posts_controller.route('/', methods=['GET'])
def source():
    try:
        return render_template('index.html')
    except Exception as e:
        logger.warning ('Getting index.html failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400

#Заполнить БД начальными значениями
@posts_controller.route("/refill_db", methods=['GET'])
def refill_db():
    try:
        return Refill_db_books.refill_db2()
    except Exception as e:
        logger.warning('Refilling failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400

#Поиск книги
@posts_controller.route('/main', methods=['GET'])
def main():
    try:
        return render_template('main.html', messages=messages)
    except Exception as e:
        logger.warning('Getting main.html failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400

#Поиск книги 2
@posts_controller.route('/add_message', methods=['POST'])
def add_message():
    try:
        text = request.form['text']
        tag = request.form['tag'] #текст это что, тэг это где
    except Exception as e:
        logger.warning('Post find_book failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400
    return (PostsService.find_books(text, tag))

#Список всех книг
@posts_controller.route("/get_all_books", methods=['GET'])
def get_all_books():
    try:
        return (PostsService.get_posts())
    except Exception as e:
        logger.warning('Getting all books failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400

#добавить книгу
@posts_controller.route('/add_book2', methods=['GET'])
def add_book2():
    try:
        return render_template('add_book2.html')
    except Exception as e:
        logger.warning('Adding books(get) failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400

#добавить книгу 2
@posts_controller.route("/add_book123", methods=['POST'])
def add_book123():
    try:
        author = request.form['author']
        book_name = request.form['book_name']
        publishing_house = request.form['publishing_house']
        year = request.form['year']
        annotation = request.form['annotation']
        rubricator = request.form['rubricator']
        PostsService.create_post(author, book_name, publishing_house, year, annotation, rubricator)
    except Exception as e:
        logger.warning('Adding books(post) failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400
    return ('Kniga Dobavlena')

#найти и изменить книгу
@posts_controller.route('/сhange_book', methods=['GET'])
def сhange_book():
    try:
        return render_template('сhange_book.html')
    except Exception as e:
        logger.warning('Changing books(get) failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400
#найти и изменить книгу2
@posts_controller.route('/сhange_book2', methods=['POST'])
def сhange_book2():
    try:
        author = request.form['author']
        book_name = request.form['book_name']
        publishing_house = request.form['publishing_house']
        year = request.form['year']
        annotation = request.form['annotation']
        rubricator = request.form['rubricator']
        gde2 = request.form['gde2']
        chto2 = request.form['chto2']
        PostsService.find_change_book(author, book_name, publishing_house, year, annotation, rubricator, chto2, gde2)
    except Exception as e:
        logger.warning('Changing books(post) failed with errors: {e}', exc_info=True)
        return {'message': str(e)}, 400
    return render_template('сhange_book.html')

