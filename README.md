# my_django_project_october


 ## steps:
 ```
 a. create a floder in Desktop named my_django_project_october
 b. open vs code and terminal
 change powershell to cmd of vs code terminal.
 c. python -m venv venv to create virtual env
 d.venv\Scripts\Activate  to activate virtual env run
 e. pip install django djangorestframework
 
 f. django-admin startproject  my_django_project_october(root app name)
 g.cd my_django_project_october
 h.python manage.py migrate
 i. python manage,py startapp courses/tutorial/...(api app)
 j. python manage.py8 createsuperuser
 k. python manage.py runserver
```

## to run this app again in vs code: folder structure(my_django_project-october -> my_django_project-october -> courses)
```
* PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> python manage.py runserver[currently inside main folder in Desktop named my_django_project-october: need to go to main app named my_django_project-october)
* C:\Users\rahmanmuhammadmahbub\AppData\Local\Programs\Python\Python312\python.exe: can't open file 'C:\\Users\\rahmanmuhammadmahbub\\Desktop\\my_django_project-october\\manage.py': [Errno 2] No such file or directory
1. PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> python -m venv venv
2. PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> venv/Scripts/activate
3. dir(if manage.py is not there then run following commands)
4. cd my_django_project_october
5. python manage.py migrate
6. python manage.py runserver
```

## After cloning a Django app from GitHub, follow these steps to set it up and run it in your local environment:
```
1. Clone the Repository
If you haven't cloned the repository yet, use the following command:

bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies.

On Windows:

python -m venv venv
venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install the required Python packages by using the requirements.txt file:

pip install -r requirements.txt
If there's no requirements.txt file, you can manually install the necessary packages. For example:

pip install django

4. Set Up Environment Variables
If the app uses environment variables (like for database credentials or secret keys), configure them.

You can create a .env file or directly set variables in your terminal. For example, you might need to set DJANGO_SECRET_KEY, DEBUG, or DATABASE_URL.
5. Run Database Migrations
If the app has a database, you need to apply migrations to set up the database schema:

python manage.py migrate

6. Create a Superuser (Optional)
If you want to access the Django admin, create a superuser:

python manage.py createsuperuser

7. Run the Django Development Server
Start the development server using:

python manage.py runserver

You can now access the app at http://127.0.0.1:8000/.

8. Static Files (Optional)
If the app has static files (like CSS or JavaScript), you might need to collect them:

bash
python manage.py collectstatic
Once these steps are complete, your Django app should be up and running.
```

# running a django app:

```
change powershell to cmd of vs code terminal.
dir: my_django_project_october    requirementfile.txt
step1. create a venv by (python -m venv venv [outside root app]) if it is already created start from step2
dir: my_django_project_october    requirementfile.txt    venv
step2. activate venv by venv\Scripts\Activate
step3. pip install django djangorestframework
step4. check root app dir by [dir] 
step5. cd my_django_project_october(root app)
step6. python manage.py runserver 192.168.3.189:8000

```

## If needed to clear sqlite db
```
Clear the Database:

If none of the above steps work, and you're not in production, you can delete the db.sqlite3 file and re-run the migrations to reset the database:


delete 001initial.py file from migrations folder
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```
## Connect with real DB like MYSQL from default DB of sqlite3:

1. Delete initial.py file from migrations folder
Install ```https://dev.mysql.com/downloads/mysql/``` and ```https://dev.mysql.com/downloads/workbench/```

2. In settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Change this according to your database engine
        'NAME': 'MY_DJANGO_PROJECT_OCTOBER',   # DB Name
        'USER': 'root',
        'PASSWORD': '19911130',                # DB password
        'HOST': 'localhost',                   # or your database server's IP
        'PORT': '3306',                        # PORT default for MySql
        'OPTIONS': {
            'charset': 'utf8mb4'
        }      
    }
}
```
3. ```pip install mysqlclient```
4. In MySqk terminal: ```CREATE DATABASE MY_DJANGO_PROJECT_OCTOBER;``` 
5. and ```SHOW DATABASES;```
6. ```python manage.py makemigrations```
7. ```python manage.py migrate```
8. ```python manage.py createsuperuser```
9. Check the data in DB by right clikcing on the table and select Select Rows - Limit1000





 
