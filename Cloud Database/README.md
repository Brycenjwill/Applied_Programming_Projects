# Overview

My program will only work for someone who has the correct account files for my database in the same directory as the program. There are 4 options when using my program that will act on the database, you can either add, update, delete, search the database. The update feature is used currently to update teh inStock field within the database to track how many of each book the library has. Note that the update, search, and delete features allow the user to search the database by name. The search feature also allows the user to sort the books by category. 

I made this program as an introduction for myself into programming with cloud databases. I decided to use Google Firestore, since it was a free resource with a good deal of functionality that I wanted. 

[Software Demo Video](https://youtu.be/ZB_Xd5tvRTE)

# Cloud Database

The cloud database that I used is Google Firestore. Google firestore is a NoSql cloud database, that allows you to manage your cloud database remotely using one of several different language options.

The database that I created consists of a main "table", named inventory, where each of the documents are stored. Each of these documents represent a book in a fictional library, each containing a category, inStock, and pages field.

# Development Environment

I developed this program using Visual Studio Code, adn the Google Firebase website.

I used python for this program. I imported several functions from the firebase_admin library for this project, including credentials and firestore.
 

# Useful Websites

I mostly reffered to the Firebase documentation as a tool for building this project.

- [Firebase Documentation](https://firebase.google.com/docs)


# Future Work

- Would like to add:
    -A way to authenticate users without needing the authorization file.
