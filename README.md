# Portfolio API

A Django REST API for managing portfolio content including projects, skills, achievements, and contact form submissions.

## Features

- **Projects API**: CRUD operations for portfolio projects
- **Skills API**: CRUD operations for skills with categorization
- **Achievements API**: CRUD operations for achievements and certifications
- **Contact Form API**: Handle and manage contact form submissions
- **Admin Interface**: Custom admin interface for content management
- **Authentication**: Secure endpoints with token-based authentication
- **Email Notifications**: Automated email notifications for contact form submissions

## API Endpoints

### Projects
- `GET /api/projects/`: List all projects
- `POST /api/projects/`: Create a new project (admin only)
- `GET /api/projects/{slug}/`: Retrieve a project
- `PUT /api/projects/{slug}/`: Update a project (admin only)
- `DELETE /api/projects/{slug}/`: Delete a project (admin only)

### Skills
- `GET /api/skills/`: List all skills
- `POST /api/skills/`: Create a new skill (admin only)
- `GET /api/skills/{id}/`: Retrieve a skill
- `PUT /api/skills/{id}/`: Update a skill (admin only)
- `DELETE /api/skills/{id}/`: Delete a skill (admin only)
- `GET /api/skills/categories/`: List all skill categories

### Achievements
- `GET /api/achievements/`: List all achievements
- `POST /api/achievements/`: Create a new achievement (admin only)
- `GET /api/achievements/{id}/`: Retrieve an achievement
- `PUT /api/achievements/{id}/`: Update an achievement (admin only)
- `DELETE /api/achievements/{id}/`: Delete an achievement (admin only)

### Contact Form
- `POST /api/contacts/`: Submit a contact form
- `GET /api/contacts/`: List all submissions (admin only)
- `GET /api/contacts/{id}/`: Retrieve a submission (admin only)
- `DELETE /api/contacts/{id}/`: Delete a submission (admin only)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd portfolio-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root and add your configuration:
```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

5. Run migrations:
```bash
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

Visit http://127.0.0.1:8000/admin/ to access the admin interface.

## Usage

### Authentication

Most endpoints require authentication for write operations. Use the following:

1. Admin interface login at `/admin/`
2. API authentication at `/api-auth/login/`

### Making Requests

Example using curl:

```bash
# List projects
curl http://127.0.0.1:8000/api/projects/

# Create a project (requires authentication)
curl -X POST http://127.0.0.1:8000/api/projects/ \
    -H "Content-Type: application/json" \
    -d '{"title":"My Project","description":"Description"}'
```

## Security

- All write operations (POST, PUT, DELETE) require admin authentication
- CORS is configured for frontend integration
- Input validation and sanitization implemented
- File upload restrictions in place

## License

This project is licensed under the MIT License - see the LICENSE file for details. 