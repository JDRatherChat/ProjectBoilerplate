# Django Production-Ready Boilerplate

A production-ready Django boilerplate with best practices for security, testing, and deployment. This project serves as
a solid foundation for building scalable Django applications.

## 📚 Documentation

- [Project Context and History](docs/CONTEXT.md) - **Start Here!** Comprehensive guide to understand the project
- [VS Code Setup Guide](docs/VSCODE_SETUP.md) - Development environment configuration

## Features

- 🔒 Production-grade security settings
- 🧪 Comprehensive test setup with pytest
- 📊 Monitoring and logging configuration
- 🚀 Performance optimizations
- 🛠 Development tools and debugging
- 📝 Code quality and linting (black, ruff)
- 🔄 CI/CD with GitHub Actions
- 🐳 Docker support
- ⚡ Optimized VS Code configuration
- 🔑 Django-allauth integration for authentication
- 📱 Modern responsive templates

## Project Structure

```
base/
├── config/              # Core project configuration
│   ├── __init__.py
│   ├── asgi.py         # ASGI application config
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI application config
├── settings/           # Settings module
│   ├── __init__.py
│   ├── base.py        # Base settings
│   ├── local.py       # Local development settings
│   ├── test.py        # Testing settings
│   └── production.py  # Production settings
├── src/               # Application source code
│   ├── accounts/      # User authentication app
│   ├── static/        # Project-wide static files
│   └── templates/     # Project-wide templates
├── environments/      # Environment variables
│   ├── local.env
│   └── production.env
└── requirements/      # Dependencies
    ├── base.txt      # Base requirements
    ├── development.txt # Development requirements
    └── production.txt # Production requirements
```

## Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd base
```

2. Run the setup script to generate a new secret key:

```bash
python setup.py
```

3. Create and activate a virtual environment:

```bash
python -m venv ../.base
source ../.base/Scripts/activate  # Windows
# OR
source ../.base/bin/activate     # Unix/macOS
```

4. Install dependencies:

```bash
pip install -r requirements/development.txt
```

5. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your settings
```

6. Run migrations:

```bash
python manage.py migrate
```

7. Create a superuser:

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

## Testing Strategy

### Test-Driven Development (TDD)

We follow a strict TDD approach for all new feature development:

1. Write failing tests first (Red)
2. Implement minimum code to pass tests (Green)
3. Refactor while maintaining passing tests (Refactor)

### Test Coverage Requirements

- Minimum 80% code coverage required
- All new features must include tests
- Both success and failure cases must be tested

### Testing Tools and Organization

Tests are organized following the Django app structure:

```
src/
└── app_name/
    └── tests/
        ├── __init__.py
        ├── test_models.py
        ├── test_views.py
        └── test_forms.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov

# Run specific test file
pytest path/to/test_file.py
```

## Development Workflow

1. Create a new feature branch:

```bash
git checkout -b feature/name
```

2. Make changes and run tests:

```bash
pytest
```

3. Format code and check quality:

```bash
black .
ruff check .
```

4. Commit changes:

```bash
git add .
git commit -m "feat: description"
```

## VS Code Integration

This project includes optimized VS Code settings for:

- Python linting and formatting (black, ruff)
- Django template support
- Testing with pytest
- Debugging configuration
- Git integration
- Editor consistency

## Security

- Production-grade security settings
- Environment-based configuration
- Secure secret management
- CSRF, XSS, and clickjacking protection
- Security middleware configuration

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
