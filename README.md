# Django Blog Application

A simple blog web application built with Django that allows users to create, view, and manage blog posts. The project focuses on clean backend structure, responsive UI, and basic CRUD functionality using Django and SQLite.

## Features

- Create, read, update, and delete blog posts
- Responsive UI with Bootstrap
- Clean Django app structure
- SQLite database integration
- Static file handling (CSS, JS)
- Template-based rendering with Django

## Tech Stack

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Bootstrap
- SQLite (default Django database)

## Project Structure

```
blog_project/
│
├── blog/              # Main app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── blog_project/      # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

(Or install from requirements file if you add one)

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

Open browser and visit:

```
http://127.0.0.1:8000/
```

## Usage

- Add new blog posts from the admin panel or UI
- Edit or delete existing posts
- Browse posts from the homepage

To access Django admin:

```bash
python manage.py createsuperuser
```

Then go to:

```
http://127.0.0.1:8000/admin/
```

## Future Improvements

- User authentication system
- Comments and likes
- Search functionality
- Pagination
- REST API integration
- Rich text editor for posts

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you want to change.

## License

This project is open source and available under the MIT License.

## Author

Nuruzzaman Islam
GitHub: https://github.com/Niloy178
