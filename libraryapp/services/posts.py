from libraryapp.repositories.posts import PostsRepository

class PostsService:
    @staticmethod
    def create_post(author, book_name, publishing_house, year, annotation, rubricator):
        PostsRepository.create_post(author, book_name, publishing_house, year, annotation, rubricator)

    @staticmethod
    def get_posts():
        posts = PostsRepository.get_all_posts()
        return posts

    @staticmethod
    def find_books(what, where):
        posts = PostsRepository.find_book(what, where)
        return posts

    @staticmethod
    def find_change_book(author, book_name, publishing_house, year, annotation, rubricator, chto, gde):
        posts = PostsRepository.find_change_book(author, book_name, publishing_house, year, annotation, rubricator, chto, gde)
        return posts
