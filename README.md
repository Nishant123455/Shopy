# Shopy

## Introduction

Shopy is a fully functional e-commerce platform designed to enhance the online shopping experience for users while providing powerful management tools for administrators. Built using Flask, this application combines simplicity, scalability, and a user-friendly interface.

[Visit Shopy](https://shopy-8nyc.onrender.com)

---

## Features

### User Features:

- **Browse Products**: Seamlessly view products across various categories.
- **Search and Filter**: Locate items using search functionality and apply filters.
- **User Authentication**: Secure sign-up and log-in functionality for customers.
- **Cart Management**: Add, update, or remove items from the shopping cart.
- **Order Management**: Place, track, and cancel orders with ease.

### Admin Features:

- **Product Management**: Add, update, or delete product listings.
- **Order Tracking**: View and update the status of user orders.
- **User Management**: Monitor and manage user accounts.

---

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite for lightweight data management
- **Payment Integration**: IntaSend API

---

## Project Structure

```
Shopy
├── instance
│   └── database.sqlite3        # SQLite database file
├── media                       # Media assets (e.g., uploaded files)
├── website                     # Main application package
│   ├── __pycache__             # Compiled Python files
│   ├── static                  # Static assets (CSS, images, JavaScript)
│   ├── templates               # HTML templates
│   ├── admin.py                # Admin functionalities
│   ├── api.py                  # API endpoints
│   ├── auth.py                 # User authentication logic
│   ├── forms.py                # Flask forms for validation
│   ├── models.py               # Database models
│   ├── views.py                # Application views and routes
├── templates                   # HTML templates for pages
│   ├── base.html               # Base template
│   ├── home.html               # Homepage
│   ├── login.html              # Login page
│   ├── signup.html             # Signup page
│   ├── cart.html               # Shopping cart
│   ├── orders.html             # User orders
│   ├── admin.html              # Admin dashboard
│   ├── 404.html                # Error page
│   └── other pages...          # Additional pages for features
├── main.py                     # Entry point of the application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── Procfile                    # Deployment configuration (Heroku)
└── README.md                   # Project documentation
```

---

## Installation

1. **Clone the Repository**

```bash
$ git clone https://github.com/Nishant123455/Shopy.git
$ cd Shopy
```

2. **Set Up Virtual Environment**

```bash
$ python -m venv venv
$ source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
$ pip install -r requirements.txt
```

4. **Configure Environment**

Create a `.env` file in the root directory and add the following:

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/database.sqlite3
INTASEND_API_KEY=your-intasend-api-key
```

5. **Run the Application**

```bash
$ flask run
```

6. **Access the Application**

visit the deployed application at [Shopy Live Demo](https://shopy-8nyc.onrender.com).

---

## API Endpoints

### **Authentication**

#### **Login**

- **POST** `/auth/login`
- **Request Body:**

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

- **Response:**

```json
{
  "message": "Login successful",
  "token": "your-auth-token"
}
```

#### **Signup**

- **POST** `/auth/signup`
- **Request Body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

- **Response:**

```json
{
  "message": "User registered successfully"
}
```

### **Products**

#### **Get All Products**

- **GET** `/api/products`

- **Response:**

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 20.00,
    "description": "Product description",
    "stock": 10
  },
  ...
]
```

### **Cart Management**

#### **Add to Cart**

- **POST** `/api/cart`
- **Request Body:**

```json
{
  "product_id": 1,
  "quantity": 2
}
```

- **Response:**

```json
{
  "message": "Product added to cart"
}
```

---

## Deployment

1. **Prepare for Deployment**

Ensure all dependencies are listed in `requirements.txt` and configure the `Procfile` for Heroku deployment.

2. **Deploy to Heroku**

```bash
$ heroku create
$ git push heroku main
$ heroku config:set SECRET_KEY=your-secret-key
$ heroku config:set INTASEND_API_KEY=your-intasend-api-key
$ heroku open
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

For any queries or feedback, feel free to reach out:

- **Email**: nishnatmishra7909\@gmail.com
- **GitHub**: [Nishant123455](https://github.com/Nishant123455)

