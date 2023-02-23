# Holberton School AirBnB Clone

This repository contains the project files for AirBnB clone project, which is a part of the Holberton School curriculum. At the moment, the goal of this project is to build a command-line interface (**The Console**) that can create, update, and delete objects. After this, we'll create:

- A **website** (*front-end*) that shows the final product to everybody;
- A **database** or files that store data;
- An **API** that provides a communication interface between the front-end and our data.

## What’s The Console?

Is a command line interpreter like the Shell, but limited to a specific use-case. In our case, we are able to manage objects in our storage system (JSON file):

- Create a new object (ex a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

The Console is the tool to validate this storage engine


## Getting Started with The Console

To use The Console you need to clone this repository to your local machine, using the following command:

    git clone https://github.com/GabrielPaganMateo/holbertonschool-AirBnB_clone.git

Finally, you can execute The Console using the following command:

    ./console.py

## How to use The Console?

After executing The Console, you can use it with the following commands:

    help: displays a list of available commands.
    quit: exits the program.
    create: creates a new object and saves it to a JSON file.
    show: displays the details of an existing object.
    destroy: deletes an existing object.
    all: displays a list of all existing objects.
    update: updates the attributes of an existing object.

### Examples:

    terminal@My_laptop:$ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb) help quit
    Quit command to exit the program
    (hbnb) help update
    Updates the attributes of an existing object
    (hbnb) create BaseModel
    3f56505c-c566-4969-aa8e-1c913fb9d7a6
    (hbnb) show BaseModel 3f56505c-c566-4969-aa8e-1c913fb9d7a6
    [BaseModel] (3f56505c-c566-4969-aa8e-1c913fb9d7a6) {'id': '3f56505c-c566-4969-aa8e-1c913fb9d7a6', 'created_at': datetime.datetime(2023, 2, 21, 18, 25, 26, 869079), 'updated_at': datetime.datetime(2023, 2, 21, 18, 25, 26, 869106)}
    (hbnb) destroy BaseModel 3f56505c-c566-4969-aa8e-1c913fb9d7a6
    (hbnb) show BaseModel 3f56505c-c566-4969-aa8e-1c913fb9d7a6
    ** no instance found **
    (hbnb) create User
    ac3e0b8f-470a-4a11-93f0-2122a3ae2604
    (hbnb) all 
    ["[BaseModel] (8f37e7e1-2b6e-4e3a-b5ca-505dcac8ef0f) {'id': '8f37e7e1-2b6e-4e3a-b5ca-505dcac8ef0f', 'created_at': datetime.datetime(2023, 2, 21, 18,   31, 28, 998945), 'updated_at': datetime.datetime(2023, 2, 21, 18, 31, 28, 998967)}", "[User] (ac3e0b8f-470a-4a11-93f0-2122a3ae2604) {'id': 'ac3e0b8f-470a-4a11-93f0-2122a3ae2604', 'created_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120526), 'updated_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120540)}"]
    (hbnb) all User
    ["[User] (ac3e0b8f-470a-4a11-93f0-2122a3ae2604) {'id': 'ac3e0b8f-470a-4a11-93f0-2122a3ae2604', 'created_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120526), 'updated_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120540)}"]
    (hbnb) update User ac3e0b8f-470a-4a11-93f0-2122a3ae2604 name "Rafael Vega"
    ["[User] (ac3e0b8f-470a-4a11-93f0-2122a3ae2604) {'id': 'ac3e0b8f-470a-4a11-93f0-2122a3ae2604', 'created_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120526), 'updated_at': datetime.datetime(2023, 2, 21, 18, 32, 0, 120540), 'name': 'Rafael Vega'}"]
    (hbnb) quit
    terminal@My_laptop:$

## Credits

This project was developed by Gabriel Pagan Mateo and Rafael O. Vega Rodriguez for the Holberton School curriculum.
