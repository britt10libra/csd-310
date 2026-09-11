""" import statements """

import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values


# using the .env file
secrets = dotenv_values(".env")



""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}


""" try/catch black for handling potential MySQL database errors """

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM studio")

    studios = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")

    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}\n".format(studio[1]))
    cursor.execute("SELECT * FROM genre")

    genres = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")

    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}\n".format(genre[1]))
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

    short_films = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")

    for film in short_films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}\n".format(film[1]))
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")

    for director in directors:
        print("Film Name: {}".format(director[0]))
        print("Director: {}\n".format(director[1]))
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()


