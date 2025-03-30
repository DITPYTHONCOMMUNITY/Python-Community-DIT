# DIT Python Community

This is a Django project template for a university website, designed for the DIT Python Community. It features a responsive design using Tailwind CSS and DaisyUI. Also uses Wagtail CMS for content management.

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Node.js and npm (required for Tailwind CSS compilation via Django-Tailwind)
- Git (optional, for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/DITPYTHONCOMMUNITY/Python-Community-DIT.git
cd Python-Community-DIT
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Compile Tailwind CSS

```bash
python manage.py tailwind start
```

### 5. Run the Django Development Server (Open in a New Terminal)

```bash
python manage.py runserver
```

Open your browser and go to `http://localhost:8000/` to view the app.

## Contributing

Contributions are welcome! To contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page to create your own copy.

2. **Create a New Branch**:

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make Changes**: Implement your feature or fix the issue.

4. **Commit Your Changes**:

   ```bash
   git commit -m "Add your feature"
   ```

5. **Push to Your Branch**:

   ```bash
   git push origin feature/your-feature
   ```

6. **Open a Pull Request**: Navigate to the original repository and submit a pull request describing your changes.

Thank you for contributing to the DIT Python Community project!

## License

This project is licensed under the MIT License.
