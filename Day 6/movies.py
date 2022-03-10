import sqlite3 as s
from prettytable import PrettyTable
connection = s.connect("moviesdata.db")

listoftables = connection.execute("select name from sqlite_master where type='table' AND name='movie'").fetchall()

if listoftables != []:
    print("Table already exist")

else:
    connection.execute('''create table movie(
                              ID integer primary key autoincrement,
                              movieName text,
                              releasedyr integer,
                              heroName text,
                              heroineName text,
                              directorName text);''')
    print("Table Created Successfully.")



while True:
    print("1. Add movie:")
    print("2. View movie :")
    print("3. Search movie using Partial movie name :")
    print("4. Search movie using hero or heroine name :")
    print("5. Update movie with hero name :")
    print("6. Delete using released year :")
    print("7. hero name who acted more movies :")
    print("8. Total Count of movies :")
    print("9. Average number of movie hero does :")
    print("10. hero Who acted below avg :")
    print("11. EXIT")

    choice=int(input("Enter choice :"))

    if choice==1:
        getName=input("Enter movie name :")
        getReleasedyr=input("Enter released date :")
        getHero=input("Enter hero name :")
        getHeroine=input("Enter heroine name :")
        getdir=input("Enter director name:")

        connection.execute("insert into movie(movieName,Releasedyr,HeroName,HeroineName,DirectorName)\
                           values('"+getName+"',"+getReleasedyr+",'"+getHero+"','"+getHeroine+"','"+getdir+"')")
        connection.commit()
        print("movies Data Added Successfully.")


    elif choice == 2:
        result = connection.execute("select * from movie")
        table = PrettyTable(["ID", "MOVIE NAME", "RELEASED YEAR", "HERO NAME", "HEROINE NAME", "DIRECTOR NAME "])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)



    elif choice == 3:
        getName = input("Enter movie Name (Single Letter or multiple letters): ")

        result = connection.execute("SELECT * FROM movie WHERE moviename LIKE '%" + getName + "%'")
        table = PrettyTable(["ID", "MOVIE NAME", "RELEASED YEAR", "HERO NAME", "HEROINE NAME", "DIRECTOR NAME "])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)


    elif choice == 4:
        getHero = input("Enter hero name for search ")
        getHeroine = input("Enter heroine name for search :")

        result = connection.execute(
            "select * from movie where heroname='" + getHero + "' or heroinename='" + getHeroine + "'")
        table = PrettyTable(["ID", "MOVIE NAME", "RELEASED YEAR", "HERO NAME", "HEROINE NAME", "DIRECTOR NAME "])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)

    elif choice==5:
        gethero = input("Enter the hero name to get Update :")

        getName = input("Enter movie name :")
        getReleasedyr = input("Enter released date :")
        getHero = input("Enter hero name :")
        getHeroine = input("Enter heroine name :")
        getdir = input("Enter director name:")
        result = connection.execute(" UPDATE movie SET moviename='"


