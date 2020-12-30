from psycopg2 import sql
from libraryapp import db, logger


class Refill_db_books:
    #создание БД
    @staticmethod
    def refill_db2():
        try:
            with db.cursor() as cursor:
                #удалить старую таблицу
                cursor.execute("DROP TABLE if exists books")
                #создать новую таблицу
                cursor.execute('''CREATE TABLE books
                (id INT PRIMARY KEY NOT NULL,
                author TEXT,
                book_name TEXT NOT NULL,
                publishing_house TEXT,
                year INT,
                annotation TEXT,
                rubricator TEXT);''')
                cursor.execute('''
                    INSERT INTO books 
                    VALUES (1, 'Jerome Salinger', 'The Catcher in the Rye', 'Testpublishing_house', 1951, 'The Catcher in the Rye is told from the first person point of view of Holden Caulfield, a teenager living in New York City in the late 1940s. Holdens ambivalence about the adult world drives the novels conflicts and provokes questions about human behavior.', 'novel');''')
                cursor.execute('''
                    INSERT INTO books 
                    VALUES (2, 'Stephen Hawking', 'The Theory of Everything', 'Phoenix Books and Audio', 2006,
                    'Stephen Hawking is widely believed to be one of the worlds greatest minds: a brilliant theoretical physicist whose work helped to reconfigure models of the universe and to redefine whats in it. Imagine sitting in a room listening to Hawking discuss these achievements and place them in historical context. It would be like hearing Christopher Columbus on the New World. Hawking presents a series of seven lec-turescovering everything from big bang to black holes to string theorythat capture not only the brilliance of Hawkings mind but his characteristic wit as well. Of his research on black holes, which absorbed him for more than a decade, he says, It might seem a bit like looking for a black cat in a coal cellar. Hawking begins with a history of ideas about the universe, from Aristotles determination that the Earth is round to Hubbles discovery, over 2000 years later, that the universe is expanding. Using that as a launching pad, he explores the reaches of modern physics, including theories on the origin of the universe (e.g., the big bang), the nature of black holes, and space-time.',
                    'scientific');''')
                cursor.execute('''
                    INSERT INTO books
                    VALUES (3, 'William Gerald Golding', 'Lord of the Flies', 'Faber and Faber', 1954,
                    'The book begins with the boys arriving on the island after their plane has been shot down during what seems to be part of a nuclear World War III. Some of the marooned characters are ordinary students, while others arrive as a musical choir under an established leader. With the exception of Sam and Eric and the choirboys, they appear never to have encountered each other before. The book portrays their descent into savagery; left to themselves on a paradisiacal island, far from modern civilization, the well-educated boys regress to a primitive state.',
                    'novel');''')
                cursor.execute('''
                    INSERT INTO books
                    VALUES (4, 'Charlotte Brontë', 'Jane Eyre', 'Smith, Elder & Company', 1847,
                    'The novel revolutionised prose fiction by being the first to focus on its protagonists moral and spiritual development through an intimate first-person narrative, where actions and events are coloured by a psychological intensity. Charlotte Brontë has been called the first historian of the private consciousness, and the literary ancestor of writers like Proust and Joyce.',
                    'drama');''')
                cursor.execute('''
                    INSERT INTO books
                    VALUES (5, 'Arkady and Boris Strugatsky', 'Hard to Be a God', 'AST', 1963,
                    'This 1963 masterpiece is widely considered one of the best novels of the greatest Russian writers of science fiction. Yet until now the only English version (unavailable for over thirty years) was based on a German translation, and was full of errors, infelicities, and misunderstandings. Now, in a new translation by Olena Bormashenko, whose translation of the authors Roadside Picnic has received widespread acclaim, here is the definitive edition of this brilliant work. It tells the story of Don Rumata, who is sent from Earth to the medieval kingdom of Arkanar with instructions to observe and to save what he can. Masquerading as an arrogant nobleman, a dueler and a brawler, Don Rumata is never defeated, but can never kill. With his doubt and compassion, and his deep love for a local girl named Kira, Rumata wants to save the kingdom from the machinations of Don Reba, the first minister to the king. But given his orders, what role can he play? Hard to Be a God has inspired a role-playing video game and two movies, including Aleksei Germans long-awaited swan song. This long overdue translation will reintroduce one of the most profound Soviet-era novels to an eager audience.',
                    'science fiction');''')
            db.commit()
        except Exception as e:
            logger.warning('Refilling books with SQL failed with errors: {e}', exc_info=True)
            return {'message': str(e)}, 400
        return "Table books refreshed and refilled"