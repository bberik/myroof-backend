![image](https://drive.google.com/uc?export=view&id=1rnywhz0X1kbrmjKlTDRiEgbNdv4dbHx1)
# MyRoof. Real Estate: Backend

This project is deployed at Vercel [myroof.vercel.app](https://myroof.vercel.app). 
Backend Server is deployed at AWS EC2 instance using Nginx and Gunicorn

[Link to the Frontend Repository](https://github.com/bberik/myroof-frontend)


## Project Overview
MyRoof is an intuitive web app where users can view and list real estate properties. 

## Project Architecture 
This project is built by following MVC design pattern. (Model/Database: PostgreSQL, View/Frontend: React.js, Controller/Server: Django)
 - The communication between Model and Controller is based on Django's built in support for models and serializers.
 - The communication between Controller and View is via RESTful API endpoints. 

### Classes
![image](https://drive.google.com/uc?export=view&id=1uy_MC7AMmPN8JLHNkzSBTIYLCp0D_ddF)

### API Endpoints
- GET ("api/) : Properties List View
- GET ("api/<id>) : Property Detail View
- POST ("api/create") : Property Create View
- POST ("api/register") : Create User View
- POST ("api/login") : Login User View
- POST ("api/refresh")  : Refresh Token Update View
- GET ("api/my-properties") : Listed Properties View (Requires Authorization)
- PUT ("api/update-profile") : Edit User View (Requires Authorization)
- GET ("api/buildings") : Buildings List View
  
### To be implemented
- PUT ("api/add-fav) : Add Property to favorites View
- PUT ("api/<id>) : Property Edit View
- DELETE ("api/<id>") : Property DELETE View
- POST ("api/contract) : Sign contract View
- GET ("api/my-contracts") : Get previous and on-going contracts view
  
### User Authorization
  Implemented with "djangorestframework-simplejwt" package. Refresh tokens are blacklisted after being rotated. 

## Run on local environment
To run this project, follow steps below:
  1. Clone this repository
  2. Create virtual environment 
  3. Install packages: ```pip install -r requirements.txt```
  4. Create .env file with following code (database connection):
    ```
    NAME=
    PGUSER=
    PASSWORD=
    HOST=
    PORT=
    ```
  4. Run the server: ```python manage.py runserver ```
  
 
