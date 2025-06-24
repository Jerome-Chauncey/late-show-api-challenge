# Late Show API Challenge

A Flask-based RESTful API for managing guests, episodes, and their appearances on the Late Show.

---

## 🔧 Setup Instructions

### 1. Install PostgreSQL

* **Ubuntu**:

  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```
* **macOS (Homebrew)**:

  ```bash
  brew update
  brew install postgresql
  ```
* **Create the database** (as `dbadmin`):

  ```bash
  psql -U dbadmin -h localhost -d postgres \
    -c "CREATE DATABASE late_show_db OWNER dbadmin;"
  ```

### 2. Clone & Install Python Dependencies

```bash
# Clone the repository
git clone https://github.com/Jerome-Chauncey/late-show-api-challenge.git
cd late-show-api-challenge

# Install dependencies and activate Pipenv shell
pipenv install
pipenv shell
```

### 3. Environment Variables

Create a `.env` file in the project root:

```env
# PostgreSQL connection
DATABASE_URL=postgresql://dbadmin:your_password@localhost/late_show_db

# JWT secret for token signing
JWT_SECRET_KEY=your_super_secret_key
```

---

## ▶️ How to Run

1. **Database migrations**

   ```bash
   export FLASK_APP=server/app.py
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

2. **Seed the database**
   Navigate into the `server/` directory and run:

   ```bash
   cd server
   python seed.py
   ```

3. **Start the server**
   Navigate into the `server/` directory and run:

   ```bash
   cd server
   python app.py
   ```

---

## 🔑 Auth Flow

1. **Register** a new user:

   ```http
   POST /register
   Content-Type: application/json

   {
     "username": "ash",
     "password": "pikachu"
   }
   ```

   **Response**:

   ```json
   { "message": "User created successfully" }
   ```

2. **Log in** with credentials:

   ```http
   POST /login
   Content-Type: application/json

   {
     "username": "ash",
     "password": "pikachu"
   }
   ```

   **Response**:

   ```json
   { "access_token": "<JWT_ACCESS_TOKEN>" }
   ```

3. **Access protected routes** by including the token:

   ```http
   Authorization: Bearer <JWT_ACCESS_TOKEN>
   ```

---

## 📋 Route List & Examples

| Method | Endpoint             | Description                            | Sample Response                              |
| ------ | -------------------- | -------------------------------------- | -------------------------------------------- |
| POST   | `/register`          | Create a new user                      | `{ "message": "User created successfully" }` |
| POST   | `/login`             | Obtain JWT access token                | `{ "access_token": "<token>" }`              |
| GET    | `/episodes`          | List all episodes                      | `[{ ...episode objects... }]`                |
| GET    | `/episodes/<int:id>` | Retrieve a specific episode            | `{ ...episode object... }`                   |
| DELETE | `/episodes/<int:id>` | Delete an episode (JWT required)       | `{ "message": "Episode deleted" }`           |
| GET    | `/guests`            | List all guests                        | `[{ ...guest objects... }]`                  |
| POST   | `/appearances`       | Create a new appearance (JWT required) | `{ ...appearance object... }`                |

---

## 📬 Postman Usage Guide

1. **Import Collection**
   Open Postman, click **Import**, select `challenge-4-lateshow.postman_collection.json`.

2. **Set Environment Variables**

   * `base_url`: `http://127.0.0.1:5000`
   * `jwt_token`: (empty at first)

3. **Register & Login**

   * Send `POST {{base_url}}/register`, then `POST {{base_url}}/login`.
   * Copy `access_token` into the `jwt_token` variable.

4. **Call Protected Endpoints**
   Add header: `Authorization: Bearer {{jwt_token}}`.

---

## 🔗 GitHub Repository

[https://github.com/Jerome-Chauncey/late-show-api-challenge](https://github.com/Jerome-Chauncey/late-show-api-challenge)
