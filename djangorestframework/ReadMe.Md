#Steps to run
1. First of all activate venv 
   
   source venv/bin/activate (for linux)

2. got back to project root folder and run migrations
  
    python manage.py makemigrations
  
    python manage.py migrate
    
3. run server :

    python manage.py runserver
  
 4. Accessible urls:
    admin/
    
    api/devices/
    
    api/devices/<str:my_id>/
    
    api/devices/<str:my_id>/readings/<str:property>/?start_on=yyyy-mm-ddTHH:MM:SS&end_on=yyyy-mm-ddTHH:MM:SS