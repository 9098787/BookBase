import sqlite3
from typing import Literal


class Database:
    '''
    Class for work with database
    '''
    def __init__(self) -> None:
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS genres (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            description TEXT,
                            genre INTEGER,
                            FOREIGN KEY (genre) REFERENCES genres (id) ON DELETE CASCADE ON UPDATE CASCADE
        )''')

    def add_genre(self, name: str) -> None:
        '''
        Add genre method

        :param name: genre's name
        '''
        self.cursor.execute('INSERT INTO genres (name) VALUES (?)', (name, ))
        self.connection.commit()

    def get_genres(self) -> list:
        '''
        Get genres method

        :returns: list of genres, id and name
        '''
        self.cursor.execute('SELECT * FROM genres')
        return self.cursor.fetchall()
    
    def add_book(self, title: str, author: str, description: str, genre: int) -> bool:
        '''
        Add book method

        :param title: book's title
        :param author: book's author
        :param description: book's description
        :param genre: book's genre id
        :returns: false, if genre don't exists in genres table, true if query completed successfully
        '''
        try:
            self.cursor.execute('INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)',
                                (title, author, description, genre))
            self.connection.commit()
            return True
        except:
            return False
    
    def get_books(self) -> list:
        '''
        Get books method

        :returns: list of books (id, title, author, description, genre)
        '''
        self.cursor.execute('''SELECT books.id, books.title, books.author, books.description, genres.name FROM books, genres
                            WHERE books.genre = genres.id''')
        return self.cursor.fetchall()
    
    def get_book_info(self, book_id: int) -> tuple:
        '''
        Get book's inforamtion method

        :param book_id: book's ID
        :returns: tuple of information (id, title, author, descriptio, genre)
        '''
        self.cursor.execute('''SELECT books.id, books.title, books.author, books.description, genres.name FROM books, genres
                            WHERE books.genre = genres.id AND books.id = ?''', (book_id, ))
        return self.cursor.fetchone()
    
    def get_books_by_genre(self, genre: int) -> list:
        '''
        Get books by genre method

        :param genre: genre ID
        :returns: list of books 
        '''
        self.cursor.execute('SELECT * FROM books WHERE genre = ?', (genre, ))
        return self.cursor.fetchall()
    
    def get_books_by_word(self, keyword: str) -> list:
        '''
        Get books by keyword method

        :param keyword: keyword
        :returns: list of books
        '''
        self.cursor.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
        return self.cursor.fetchall()

    def delete_book(self, book_id: int) -> None:
        '''
        Delete book

        :param book_id: book's id
        '''
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id, ))
        self.connection.commit()