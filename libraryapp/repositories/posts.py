from psycopg2 import sql
from libraryapp import db, logger


class PostsRepository:
    @staticmethod
    def create_post(author, book_name, publishing_house, year, annotation, rubricator):
        try:
            with db.cursor() as cursor:
                db.autocommit = True
                values = [
                    (author, book_name, publishing_house, year, annotation, rubricator)
                ]
                insert = sql.SQL(
                    'INSERT INTO books (author, book_name, publishing_house, year, annotation, rubricator) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except Exception as e:
            logger.warning('Creating books (SQL) failed with errors: {e}', exc_info=True)
            return {'message': str(e)}, 400
        print("Creating book")

    @staticmethod
    def get_all_posts():
        try:
            ret = {}
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM books;')
                for row in cursor:
                    ret[row[0]] = {
                        'author': row[1],
                        'book_name': row[2],
                        'publishing_house': row[3],
                        'year': row[4],
                        'annotation': row[5],
                        'rubricator': row[6]
                    }
        except Exception as e:
            logger.warning('Getting all books (SQL) failed with errors: {e}', exc_info=True)
            return {'message': str(e)}, 400
        return ret

    @staticmethod
    def find_book(chto, gde):
        try:
            founded = {}
            with db.cursor() as cursor:
                db.autocommit = True
                cursor.execute("SELECT * FROM books WHERE " + gde + "=" + "'" + chto + "'")
                for row in cursor:
                    founded[row[0]] = {
                        'author': row[1],
                        'book_name': row[2],
                        'publishing_house': row[3],
                        'year': row[4],
                        'annotation': row[5],
                        'rubricator': row[6]
                    }
        except Exception as e:
            logger.warning('Finding book (SQL) failed with errors: {e}', exc_info=True)
            return {'message': str(e)}, 400
        return founded

    @staticmethod
    def find_change_book(author, book_name, publishing_house, year, annotation, rubricator, chto, gde):
        try:
            founded = {}
            with db.cursor() as cursor:
                db.autocommit = True
                cursor.execute("UPDATE books SET author =" + "'" + author + "', book_name =" + "'" + book_name + "', publishing_house =" + "'" + publishing_house + "', year =" + "'" + year + "', annotation =" + "'" + annotation + "', rubricator =" + "'" + rubricator + "' WHERE " + gde + "=" + "'" + chto + "'")
        except Exception as e:
            logger.warning('Finding and changing book (SQL) failed with errors: {e}', exc_info=True)
            return {'message': str(e)}, 400
        return "Changes complete"