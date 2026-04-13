# Flask Projects

**Flask Projects** is a web application created with Flask for managing users, projects and tasks.

### Requirements 📋

- Python 3.12.10. It’s recommended to use [pyenv](https://github.com/pyenv/pyenv) to easily install the desired Python version.
- A `.env` file created at the project root containing the required environment variables.
- Docker compose installed.

---

### Architecture ⚙️

The architecture follows the principles of Clean Architecture, where the database and API layers are isolated from the business logic and each entity is isolated to maintain the code clear and maintainable.
Therefore, each entity has its own model, repository, resources and database table, allowing for single responsibility, easier testing and safer modifications. 

---

### Stack 🛠️

Main frameworks and libraries:

- Flask
- Pytest
- Pydantic
- SQLAlchemy

---

### Application 💻

It is recommended to create a virtual environment to isolate the application dependencies. With the virtual environment created and activated, run the following command to install the dependencies:
```jsx
pip install -r requirements.txt
```

Start the docker container with the following command:
```jsx
docker compose up -d
```

To run the application on http://127.0.0.1:5000/ and create the database tables automatically, run the following command:

```jsx
python main.py
```

To run unit tests and integration tests, run the following command on the root folder in a different terminal or with the application stopped:

```jsx
pytest
```

---

### Documentation ️📖

The documentation for the available endpoints were created using `Sphinx` and can be generated with the following commands:
```jsx
cd docs
```
```jsx
make html
```

The documentation can be viewed by opening the file `docs/build/html/index.html` with a browser.

---

### Endpoints 🔁

The endpoints with the `GET` method can be executed by any user and do not require a logged user.

The endpoints with the `POST`, `PUT` and `DELETE` methods can only be executed by a user with the user type `manager`. Therefore, they require a manager to be logged in.

The Postman project with all the endpoints of the application can be accessed with the URL:

- https://www.postman.com/bruno-9497913/projects-apis/overview

With the application running after the command `python main.py`, all the endpoints in Postman will be executed at http://127.0.0.1:5000/.

A manager user is automatically created on the database when the application is started for the first time, therefore the first login can be done with the endpoint `POST /auth/login` with the following credentials:
```jsx
{
    "email": "admin@admin.com",
    "password": "admin"
}
```

With the manager user logged in, a new user can be created with the create user endpoint `POST /users/` with the following body request structure:
```jsx
{
    "email": "new_user@email.com",
    "password": "password",
    "username": "new_user",
    "name": "New User",
    "user_type": 1
}
```

After the creation of this user, the password will be safely stored in the database with encryption. Therefore, the manager user can be logged out with the endpoint `POST /auth/logout` and the new created user can perform the login to start using the application with its own user.
