# Flask Notes App 

A Flask-based notes application with user authentication and SQLite database integration.

## Features
- User registration and login
- Session-based authentication
- Add personal notes
- Delete notes
- User-specific dashboard
- SQLite database integration

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS

## Project Structure

flask-notes-app/
│
├── app.py
├── database.db
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── add_note.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md

## How to Run

1. Install dependencies

pip install flask flask_sqlalchemy

2. Run application

python app.py

3. Open browser

http://127.0.0.1:5000

## Future Improvements
- Edit notes
- Password hashing
- Profile page
- Bootstrap UI
- PostgreSQL integration

## Author
Abdulkareem Muflihudeen