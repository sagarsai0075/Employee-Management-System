#  Employee Management System

A comprehensive Django-based web application for managing employee information efficiently. This system provides functionality for CRUD operations, department management, employee search, and secure authentication.

##  Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Validations](#-validations)
- [API Endpoints](#-api-endpoints)
- [Contributing](#-contributing)
- [License](#-license)

---

##  Features

- **Employee Management**
  - Create, Read, Update, and Delete (CRUD) employee records
  - View all employees with detailed information
  - Search employees by name with real-time filtering
  - Automatic timestamp tracking (created_at, updated_at)

- **Department Management**
  - Organize employees by department
  - Unique department names
  - Automatic sorting by department name

- **User Authentication**
  - Secure login system
  - Logout functionality
  - Protected views (only authenticated users can access)

- **Data Validation**
  - Email uniqueness and format validation
  - Phone number validation (10-15 characters)
  - Name validation (letters, spaces, hyphens, apostrophes only)
  - Salary validation (must be positive)
  - Phone number format: supports formats like +1 (555) 123-4567

- **User Interface**
  - Clean, responsive Bootstrap-based design
  - Form validations with helpful error messages
  - Intuitive navigation
  - Base template for consistency

---

##  Tech Stack

- **Backend Framework**: Django 6.0.4
- **Database**: SQLite3 (default)
- **Python Version**: 3.x
- **Frontend**: HTML5, Bootstrap CSS
- **Web Server**: ASGI/WSGI compatible

---

##  Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/sagarsai0075/Employee-Management-System.git
cd Employee-Management-System
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

---

##  Configuration

### Database Setup
The project uses SQLite by default. To change the database:

1. Edit `config/settings.py`
2. Modify the `DATABASES` configuration
3. Run migrations: `python manage.py migrate`

### Static Files
Collect static files for production:
```bash
python manage.py collectstatic
```

### Security Settings (Production)
Update these in `config/settings.py`:
- Change `DEBUG = False`
- Update `ALLOWED_HOSTS` with your domain
- Generate a new `SECRET_KEY`
- Configure `DATABASES` for production

---

##  Usage

### Access the Application
1. Open browser and navigate to `http://127.0.0.1:8000/login/`
2. Login with your superuser credentials
3. Navigate to the employee management dashboard

### Main Operations

#### View Employees
- Navigate to the dashboard to see all employees
- Employees are ordered by most recent first

#### Add Employee
- Click "Add Employee"
- Fill in all required fields:
  - Full Name (letters, spaces, hyphens, apostrophes only)
  - Email (must be unique and valid)
  - Phone (10-15 characters, supports various formats)
  - Salary (must be positive)
  - Joining Date
  - Address
  - Department
- Submit the form

#### Search Employees
- Use the search bar to find employees by name
- Results update in real-time

#### Update Employee
- Click "Edit" on an employee record
- Modify the fields as needed
- Save changes

#### Delete Employee
- Click "Delete" on an employee record
- Confirm the deletion

#### Admin Panel
- Access admin panel at `/admin/`
- Manage users, employees, and departments
- Perform bulk operations

---

##  Project Structure

```
Employee-Management-System/
├── config/                          # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Project URL routing
│   ├── asgi.py                     # ASGI configuration
│   └── wsgi.py                     # WSGI configuration
│
├── employees/                       # Main app
│   ├── models.py                   # Database models
│   ├── views.py                    # View functions
│   ├── forms.py                    # Django forms
│   ├── urls.py                     # App URL routing
│   ├── admin.py                    # Admin configuration
│   ├── apps.py                     # App configuration
│   ├── tests.py                    # Unit tests
│   │
│   ├── migrations/                 # Database migrations
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_*.py
│   │
│   └── templates/
│       ├── employees/
│       │   ├── base.html           # Base template
│       │   ├── employee_list.html  # List view
│       │   ├── add_employee.html   # Add form
│       │   ├── update_employee.html # Edit form
│       │   └── delete_employee.html # Delete confirmation
│       │
│       └── registration/
│           └── login.html          # Login page
│
├── db.sqlite3                       # SQLite database
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

##  Validations

### Field Validations

#### Employee Model
| Field | Validation Rules | Error Message |
|-------|------------------|---------------|
| **Name** | 2+ chars, letters/spaces/hyphens/apostrophes | "Name must be at least 2 characters and contain only allowed characters" |
| **Email** | Valid format, unique | "Must be a valid email address and unique" |
| **Phone** | 10-15 digits, can contain +, -, spaces, () | "Phone number must be 10-15 digits with allowed characters" |
| **Salary** | Positive number (>= 0) | "Salary must be a positive number" |
| **Joining Date** | Valid date | "Select a valid date" |
| **Address** | Text field | Required |
| **Department** | Must exist | "Select a valid department" |

#### Department Model
| Field | Validation Rules |
|-------|------------------|
| **Name** | Unique, max 100 characters |

---

##  API Endpoints

### Employee Management Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | List all employees |
| GET | `/add/` | Employee creation form |
| POST | `/add/` | Create new employee |
| GET | `/update/<id>/` | Employee edit form |
| POST | `/update/<id>/` | Update employee |
| GET | `/delete/<id>/` | Delete confirmation |
| POST | `/delete/<id>/` | Delete employee |
| GET | `/logout/` | Logout user |

### Admin Routes
| Route | Purpose |
|-------|---------|
| `/admin/` | Django admin panel |
| `/login/` | User login (auto-redirected) |

---

##  Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/sagarsai0075/Employee-Management-System.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Ensure code follows PEP 8 standards
   - Add comments for complex logic
   - Test your changes thoroughly

4. **Commit Your Changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```

5. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues

---

##  License

This project is open source and available under the [MIT License](LICENSE). Feel free to use it for personal or commercial projects.

---

##  Support

If you encounter any issues:

1. Check the [Issues](https://github.com/sagarsai0075/Employee-Management-System/issues) page
2. Review the [IMPROVEMENTS.md](IMPROVEMENTS.md) for recent changes
3. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Your environment details (OS, Python version, Django version)

---

##  Contact & Author

- **Repository**: [Employee-Management-System](https://github.com/sagarsai0075/Employee-Management-System)
- **Issues**: Report bugs and feature requests [here](https://github.com/sagarsai0075/Employee-Management-System/issues)

---

##  Future Enhancements

Potential features for future versions:
- Employee performance ratings
- Salary history tracking
- Leave management system
- PDF report generation
- Email notifications
- Advanced search filters
- Export to CSV/Excel
- Role-based access control (RBAC)
- API endpoints (Django REST Framework)
- Unit tests coverage
- Docker containerization

---

**Last Updated**: April 2026
**Version**: 1.0.0
