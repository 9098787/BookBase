from database import Database

db = Database()

while True:
    param = input('''1 - Добавить жанр
2 - Добавить книгу
3 - Показать все книги
4 - Посмотреть подробную информацию о книге
5 - Показать книги по жанру
6 - Поиск книги
7 - Удаление книги
0 - Выйти
''')
    
    match param:
        case '1':
            genre_name = input('Введите жанр: ')
            db.add_genre(genre_name)
            print('Новый жанр успешно добавлен!\n')
        case '2':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            description = input('Введите описание книги: ')
            genres = db.get_genres()
            if not genres:
                print('Жанры не добавлены!')
                continue
            for genre in genres:
                print(f'ID: {genre[0]} Жанр: {genre[1]}')
            genre = input('Выберите жанр (ID): ')
            if db.add_book(title, author, description, genre):
                print('Новая книга добавлена успешно!\n')
            else:
                print('Ошибка жанра! Выберите из списка\n')
        case '3':
            books = db.get_books()
            if not books:
                print('Книги не добавлены!')
                continue
            for book in books:
                print(f'ID: {book[0]} Название: {book[1]} Автор: {book[2]}')
        case '4':
            books = db.get_books()
            if not books:
                print('Книги не добавлены!')
                continue
            for book in books:
                print(f'ID: {book[0]} Название: {book[1]} Автор: {book[2]}')
            book = input('Выберите ID для подробной информации: ')
            if not book.isnumeric():
                print('ID должен быть числом!\n')
                continue
            info = db.get_book_info(int(book))
            if info:
                print(f'\nID: {info[0]}\nНазвание: {info[1]}\nАвтор: {info[2]}\nОписание: {info[3]}\nЖанр: {info[4]}\n')
        case '5':
            genres = db.get_genres()
            if not genres:
                print('Жанры не добавлены!')
                continue
            for genre in genres:
                print(f'ID: {genre[0]} Жанр: {genre[1]}')
            genre = input('Выберите жанр (ID): ')
            if not genre.isnumeric():
                print('ID должен быть числом!\n')
                continue
            books = db.get_books_by_genre(int(genre))
            if not books:
                print('Книг по данному запросу нет')
            for book in books:
                print(f'ID: {book[0]} Название: {book[1]} Автор: {book[2]}')
        case '6':
            keyword = input('Введите ключевое слово: ')
            books = db.get_books_by_word(keyword)
            if not books:
                print('Книг по данному запросу нет')
                continue
            for book in books:
                print(f'ID: {book[0]} Название: {book[1]} Автор: {book[2]}')
        case '7':
            books = db.get_books()
            if not books:
                print('Книги не добавлены!')
                continue
            for book in books:
                print(f'ID: {book[0]} Название: {book[1]} Автор: {book[2]}')
            book = input('Выберите ID для удаления книги: ')
            if not book.isnumeric():
                print('ID должен быть числом!\n')
                continue
            db.delete_book(int(book))
        case '0':
            break
        case _:
            print('Неизвестный параметр')

