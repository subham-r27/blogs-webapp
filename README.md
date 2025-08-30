# Django Blog Project

A Django web application with user authentication and blog post functionality.

## Features

- User registration and authentication
- Blog post creation and management
- Responsive web design
- Admin interface for content management

## Technologies Used

- Django 4.x
- SQLite database
- HTML/CSS/JavaScript
- Bootstrap (for styling)

## Project Structure

```
myproject/
├── myproject/          # Main project settings
├── posts/             # Blog posts app
├── users/             # User authentication app
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS)
└── media/             # User uploaded files
```

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd Clone
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
cd myproject
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

- Visit `http://127.0.0.1:8000/` to view the blog
- Access admin panel at `http://127.0.0.1:8000/admin/`
- Register new users and create blog posts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
