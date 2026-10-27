Little Lemon Restaurant API (Django REST Framework + MySQL)
To run without MySQL, set USE_SQLITE=1 before running the commands.
API paths to test:
/auth/users/              (POST: register a user)
/auth/token/login/        (POST: get auth token)
/api/menu-items/          (GET, POST)
/api/menu-items/<id>/     (GET, PUT, PATCH, DELETE)
/api/bookings/            (GET, POST)
/api/bookings/<id>/       (GET, PUT, PATCH, DELETE)

How to test with Insomnia:
1. POST /auth/users/ with JSON: {"username": "reviewer", "password": "Lemon@12345", "email": "r@example.com"}
2. POST /auth/token/login/ with JSON: {"username": "reviewer", "password": "Lemon@12345"}
   The response contains "auth_token".
3. In Insomnia open the Auth tab, choose Bearer Token, set the Prefix to "Token"
   and paste the auth_token value. Now call /api/menu-items/ or /api/bookings/.

Run locally:
pip install -r requirements.txt
Create a MySQL database named littlelemon, set your password in LittleLemon/settings.py
python manage.py migrate
python manage.py runserver

Run unit tests:
python manage.py test
