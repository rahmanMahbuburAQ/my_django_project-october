# my_django_project_october

```
 steps:
 a. create a floder in Desktop named my_django_project_october
 b. open vs code and terminal
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
```
to run this app again in vs code: folder structure(my_django_project-october -> my_django_project-october -> courses)
* PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> python manage.py runserver[currently inside main folder in Desktop named my_django_project-october: need to go to main app named my_django_project-october)
* C:\Users\rahmanmuhammadmahbub\AppData\Local\Programs\Python\Python312\python.exe: can't open file 'C:\\Users\\rahmanmuhammadmahbub\\Desktop\\my_django_project-october\\manage.py': [Errno 2] No such file or directory
1. PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> python -m venv venv
2. PS C:\Users\rahmanmuhammadmahbub\Desktop\my_django_project-october> venv/Scripts/activate
3. dir(if manage.py is not there then run following commands)
4. cd my_django_project_october
5. python manage.py migrate
6. python manage.py runserver
```
```
After cloning a Django app from GitHub, follow these steps to set it up and run it in your local environment:

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





 
