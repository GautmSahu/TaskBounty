## Overview
This project provides a RESTful API and GUI for managing apps and user points using Django and Django REST Framework. It includes authentication, app management (CRUD), and user points tracking for completed tasks.

---

## 📌 Features
- **Authentication** using Django Allauth (Token-based)
- **Admin Panel for managing apps**
- **User Panel for tracking points & submitting task proofs**
- **API Endpoints for creating, reading, updating, and deleting apps**
- **Task submission with screenshot upload (drag and drop support)**

---

##  ✅ Technologies Used
-  **Backend**: Django, Django REST Framework (DRF), Django-Allauth
-  **Database**: PostgreSQL (or SQLite for local dev)
-  **Authentication**: Django-Allauth (Session-based authentication)
-  **Frontend**: Jinja2, HTML, CSS, JavaScript (for UI)
-  **Security**: Custom permissions to restrict access

---

## 🔒 Permissions:

- **Admin**: Can create, update, delete apps but cannot access user points.
- **User**: Can view apps, submit screenshots for points, but cannot modify apps.
- If a user tries to perform an unauthorized action, they will receive
  ```json
  {
    "detail": "You do not have permission to perform this action."
  }
  ```

## 📌 Installation

## **Installation & Setup on local system without docker (ubuntu)**

1. Clone git repo
    - git clone repository-url
2. Create virtual environment(python=3.11)
    - python3 -m venv venv
3. Activate the environment
    - . venv/bin/activate
4. Go to project path
    - cd TaskBounty/
5. Install required packages
    - pip install -r requirements.txt
6. Setup postgres and create database
    - open postgres shell and paste below cmds
        - CREATE DATABASE db_name; 
        - CREATE USER db_user WITH PASSWORD 'secure_password';
        - ALTER ROLE db_user SET client_encoding TO 'utf8'; 
        - ALTER ROLE db_user SET default_transaction_isolation TO 'read committed'; 
        - ALTER ROLE db_user SET timezone TO 'UTC'; 
        - GRANT ALL PRIVILEGES ON DATABASE db_name TO db_user; 
7. Open .env file and do the necessary changes like DB configuration etc.
8. Export the environment variables
    - source .env
9. Run migrations
    - python manage.py makemigrations
    - python manage.py migrate
10. Run the django server
    - python manage.py runserver
    - Check the api's with the help of postman collection providedd above
11. That's it.

---

## 📌 Authentication

- **Auth Type**: `Token Authentication`
- **Header**:  
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Get Token**:
  - **Endpoint**: `POST /auth/login/`
  - **Body (JSON)**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Success Response (`200 OK`)**:
    ```json
    {
      "key": "your_generated_token"
    }
    ```

---

## API Collection
The API endpoints and their details can be found in the following collection:
[Click here](https://drive.google.com/file/d/1ELU6Hz5pv_oQr0LYh3_4gZSbDMO2wiFP/view?usp=sharing)

---

## 📌 API Documentation

### 1️⃣ App API

#### Create an App (Admin Only)
- **Method**: `POST`
- **URL**: `/bounty/apps/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  Content-Type: multipart/form-data
  ```
- **Parameters**:
- Field	        Type	Required	 Description
- name	        string	✅ Yes	  Name of the app
- link	        string	✅ Yes	  App download link
- category	    string	✅ Yes	  Category (Entertainment or Social)
- sub_category	string	✅ Yes	  Sub-category (Videos or Engagement)
- logo	        file	  ✅ Yes	  App logo (image file)
- points	      integer	✅ Yes	  Points rewarded
- **Body (Multipart Form-Data)**:
  ```json
  {
    "name": "My App",
    "link": "https://example.com",
    "category": "Entertainment",
    "sub_category": "Videos",
    "points": 50,
    "logo": (file)
  }
  ```
- **Success Response (`201 Created`)**:
  ```json
  {
    "id": 1,
    "name": "My App",
    "link": "https://example.com",
    "category": "Entertainment",
    "sub_category": "Videos",
    "points": 50,
    "logo": "http://127.0.0.1:8000/media/logo/pp-218849_11zon.jpg"
  }
  ```
- **Error Response (`400 Bad request`)**:
  ```json
  {
    "sub_category": [
        "This field is required."
    ],
    "logo": [
        "No file was submitted."
    ],
    "points": [
        "This field is required."
    ]
  }
  ```

#### List All Apps
- **Method**: `GET`
- **URL**: `/bounty/apps/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Response (`200 OK`)**:
  ```json
  [
    {
      "id": 1,
      "name": "My App",
      "link": "https://example.com",
      "category": "Entertainment",
      "sub_category": "Videos",
      "points": 50,
      "logo": "http://127.0.0.1:8000/media/logo/pp-218849_11zon.jpg"
    }
  ]
  ```

#### Retrieve a Single App
- **Method**: `GET`
- **URL**: `/bounty/apps/{id}/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Response (`200 OK`)**:
  ```json
  {
      "id": 1,
      "name": "My App",
      "link": "https://example.com",
      "category": "Entertainment",
      "sub_category": "Videos",
      "points": 50,
      "logo": "http://127.0.0.1:8000/media/logo/pp-218849_11zon.jpg"
  }
  ```
- **Error Response (`404 Not Found`)**:
  ```json
  {
    "detail": "No App matches the given query."
  }
  ```

#### Update an App (Admin Only)
- **Method**: `PUT`
- **URL**: `/bounty/apps/{id}/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  Content-Type: multipart/form-data
  ```
- **Body (Multipart Form-Data)**:
  ```json
  {
    "name": "My App",
    "link": "https://example.com",
    "category": "Entertainment",
    "sub_category": "Videos",
    "points": 50,
    "logo": (file)
  }
  ```
- **Success Response (`200 OK`)**:
  ```json
  {
    "id": 1,
    "name": "My App",
    "link": "https://example.com",
    "category": "Entertainment",
    "sub_category": "Videos",
    "points": 50,
    "logo": "http://127.0.0.1:8000/media/logo/pp-218849_11zon.jpg"
  }
  ```
- **Error Response (`400 Bad request`)**:
  ```json
  {
    "logo": [
        "No file was submitted."
    ],
    "points": [
        "A valid integer is required."
    ]
  }
  ```

#### Delete an App (Admin Only)
- **Method**: `DELETE`
- **URL**: `/bounty/apps/{id}/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  Content-Type: multipart/form-data
  ```
- **Success Response (`204 No Content`)**:
  ```json
  ```
- **Error Response (`400 Bad request`)**:
  ```json
  {
    "detail": "No App matches the given query."
  }
  ```
---

### 2️⃣ User Points API

#### List User Points
- **Method**: `GET`
- **URL**: `/bounty/points/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Response (`200 OK`)**:
  ```json
  [
    {
        "id": 5,
        "points": 100,
        "screenshot": "http://127.0.0.1:8000/media/screenshots/view-icon-614x460_xeFOtPe.png",
        "user": 1,
        "app": 7
    }
  ]
---

#### Add a Task (User Only)
- **Method**: `POST`
- **URL**: `/bounty/points/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  Content-Type: multipart/form-data
  ```
- **Body (Multipart Form-Data)**:
  ```json
  {
    "user": "2",
    "app": "2",
    "points": 50,
    "logo": (file)
  }
  ```
- **Success Response (`201 Created`)**:
  ```json
  {
    "id": 3,
    "points": 50,
    "screenshot": "http://127.0.0.1:8000/media/screenshots/new.png",
    "user": 2,
    "app": 2
  }
  ```
- **Error Response (`400 Bad request`)**:
  ```json
  {
    "screenshot": [
        "No file was submitted."
    ]
  }
  ```


#### Retrieve All Tasks for User
- **Method**: `GET`
- **URL**: `/bounty/points/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Response (`200 OK`)**:
  ```json
  [
    {
      "id": 5,
      "points": 100,
      "screenshot": "http://127.0.0.1:8000/media/screenshots/view-icon-614x460_xeFOtPe.png",
      "user": 1,
      "app": 7
    }
  ]
  ```

#### Retrieve a Specific User Task
- **Method**: `GET`
- **URL**: `/bounty/points/{id}/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  ```
- **Response (`200 OK`)**:
  ```json
  {
    "id": 5,
    "points": 100,
    "screenshot": "http://127.0.0.1:8000/media/screenshots/view-icon-614x460_xeFOtPe.png",
    "user": 1,
    "app": 7
  }
  ```
- **Error Response (`404 Not Found`)**:
  ```json
  {
    "detail": "No UserPoints matches the given query."
  }
  ```

#### Delete a Task (User Only)
- **Method**: `DELETE`
- **URL**: `/bounty/points/{id}/`
- **Headers**:
  ```
  Authorization: Token YOUR_AUTH_TOKEN
  Content-Type: multipart/form-data
  ```
- **Success Response (`204 No Content`)**:
  ```json
  ```
- **Error Response (`400 Bad request`)**:
  ```json
  {
    "detail": "No UserPoints matches the given query."
  }
  ```
---

## Thank you! 😊