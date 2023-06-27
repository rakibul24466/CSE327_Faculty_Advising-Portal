# CSE327_Faculty_Advising-Portal
"This is a student portal that allows students to add, drop, and delete courses, as well as print their course schedules."


## Backend server installation  

First, install all the Python dependencies 

```bash
pip install djangorestframework
pip install django-cors-headers
pip install pandas
pip install mysqlclient
```
To run the backend
```bash
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## For Frontend 
```bash
npm install
npm run dev
```

## For ER Diagram 
```bash
pip install graphviz
pip install django-extensions
pip install pyparsing pydot
```

## Command
python manage.py graph_models api  --pygraphviz -o my_project_visualized.png

## For Class Diagram
pip install pylint
