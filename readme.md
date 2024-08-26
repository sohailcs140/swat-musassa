## Requirements

- Python 3.12.4
- Django 5.1

## Installation

1. **Clone the repository:**

   ```
    https://github.com/sohailcs140/swat-musassa.git
   
   ```

2. **Create a virtual environment:**

```
python -m venv venv
```


3. **Activate the virtual environment:**

```
venv\Scripts\activate
```


4. **install the requirements**

```
pip install -r requirements.txt
```

5. **Apply the migrations**

```
python manage.py migrate
```


6. **Create a superuser:**

```
python manage.py createsuperuser
```

7. **Run the server**

```
python manage.py runserver
```


# Xampp Server Setup

```

# Django Project

LoadFile "C:/Users/LAPTOP~1/AppData/Local/Programs/Python/Python312/python312.dll"
LoadModule wsgi_module "C:/Users/LAPTOP~1/AppData/Local/Programs/Python/Python312/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp312-win_amd64.pyd"

# Set the Python environment home
WSGIPythonHome "C:/Users/Laptop Valley/AppData/Roaming/Python/Python312"

# Map the WSGI script alias to your Django project's wsgi.py file
WSGIScriptAlias /test_django "C:/xampp/htdocs/testDjango/testDjango/wsgi.py"

# Set the Python path for your Django project
WSGIPythonPath "C:/xampp/htdocs/testDjango"

# Directory configuration for Django project
<Directory "C:/xampp/htdocs/testDjango/testDjango">
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>



# Alias for static files
# Alias /static/ "C:/xampp/htdocs/testDjango/static/"

# Directory configuration for static files
# <Directory "C:/xampp/htdocs/testDjango/static">
#    Require all granted
# </Directory>
```