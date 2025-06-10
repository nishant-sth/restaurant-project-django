# Kunama- Restaurant Management System (Work In Progress)

A comprehensive Django-based restaurant management system that helps streamline restaurant operations, manage orders, and handle customer interactions efficiently.

## 🚀 Features

- **Order Management**: Track and manage customer orders
- **Menu Management**: Maintain and update restaurant menu items
- **Customer Management**: Handle customer information and preferences
- **PDF Generation**: Generate invoices and reports using xhtml2pdf
- **Barcode Integration**: Support for barcode scanning and management
- **Email Notifications**: Automated email communication system
- **Responsive Design**: Mobile-friendly interface

## 🛠️ Tech Stack

- **Backend Framework**: Django 5.1.7
- **Database**: MySQL
- **Additional Libraries**:
  - Django REST Framework
  - xhtml2pdf
  - python-barcode
  - python-dotenv

## 📋 Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd elite_kitchen
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with the following variables:
```
SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=3306
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-email-password
```

5. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## 📁 Project Structure

```
elite_kitchen/
├── elite_kitchen/          # Main project directory
├── restaurant/            # Main application
├── static/               # Static files (CSS, JS, images)
├── media/                # User-uploaded files
├── manage.py            # Django management script
└── .env                 # Environment variables
```

## 🔒 Security Features

- CSRF Protection enabled
- Secure password validation
- Environment variable-based configuration
- Secure email handling

## 🧪 Testing

Run tests using:
```bash
python manage.py test
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support, please contact the development team or create an issue in the repository.

## 🙏 Acknowledgments

- Django Framework
- All contributors and maintainers
- Open-source community

---
Made with ❤️ by Nishant Shrestha
