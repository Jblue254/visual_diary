#  Visual Diary

A simple and modern **Visual Diary web application** built with Django. Visual Diary allows users to create, manage, and explore personal diary entries using images, descriptions, and tags.

The project is designed to provide a simple way of documenting memorable moments, experiences, places, and events in a visual format.

##  Live Demo

**Live Application:** https://visual-diary-udu8.onrender.com/

---

##  Features

###  User Authentication

* User registration
* User login and logout
* Protected diary functionality for authenticated users

###  Visual Diary Entries

* Create diary entries
* Add images to entries
* Add titles and descriptions
* Add tags to organize entries
* View individual diary entries

###  Search

* Search diary entries using tags
* Quickly find entries based on their category or keywords

###  Home Page

* Displays diary entries in an easy-to-browse layout
* Provides navigation to the main sections of the application

###  Responsive Design

* Designed to work across desktop and mobile screen sizes
* Clean and simple user interface

---

##  Technologies Used

### Backend

* **Python**
* **Django**

### Frontend

* **HTML5**
* **CSS3**
* **Tailwind CSS**
* **JavaScript**

### Database

* **SQLite** for local development
* Database configuration can be changed for production environments

### Deployment

* **Render**

### Version Control

* **Git**
* **GitHub**

---

##  Project Structure

```text
visual-diary/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── diary/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── ...
```

> The exact folder names may vary depending on the final project structure.

---

##  Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/visual-diary.git
```

Move into the project directory:

```bash
cd visual-diary
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Admin Panel

Django's built-in administration panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser account created with:

```bash
python manage.py createsuperuser
```

The admin panel can be used to manage users and diary-related data.

---

## 📝 How It Works

The application follows the standard Django **Model-View-Template (MVT)** architecture.

### Models

Django models are used to represent diary data and store information in the database.

A diary entry can contain information such as:

* Title
* Description
* Image
* Tags
* Date created
* User/owner

### Views

Views handle application logic, including:

* Displaying diary entries
* Creating entries
* Viewing entry details
* Searching by tags
* Handling authentication

### Templates

HTML templates are responsible for displaying the application interface to users.

The frontend uses HTML, CSS, Tailwind CSS, and JavaScript to create the user interface.

---

##  Tag Search

Visual Diary includes tag-based searching.

For example, diary entries can be categorized with tags such as:

```text
animals
travel
wildlife
nature
adventure
```

A user can search for a tag to find related diary entries.

---

## 🖼️ Example Diary Entries

The deployed application currently demonstrates entries such as:

*  **Lions** — `manes`
*  **Amboseli Big** — `big tuskers`
*  **Maasai Mara Crossing** — `crossing`

These demonstrate how images, titles, descriptions, and tags can be combined to create visual diary entries.

---

##  Deployment

The application is deployed using **Render**.

### Production URL

https://visual-diary-udu8.onrender.com/

For deployment, the project requires the production environment to be configured with the appropriate:

* Environment variables
* Django settings
* Allowed hosts
* Static files configuration
* Database configuration
* Gunicorn/WSGI configuration

---


##  Testing

Django's testing framework can be used to test important parts of the application.

Run the tests with:

```bash
python manage.py test
```

Tests can be used to verify:

* User authentication
* Diary entry creation
* Diary entry listing
* Individual entry pages
* Tag searching
* Access restrictions
* Database behavior

---

##  Future Improvements

Possible improvements for future versions include:

*  Like/favourite diary entries
*  Comments
*  Multiple tag filtering
*  Entries grouped by date
*  Location information for diary entries
*  User profile pages
*  Image galleries
*  Edit and delete entries
*  Notifications
*  Dark mode
*  Personal diary statistics
*  Progressive Web App (PWA) support

---

##  Project Goals

The main goals of Visual Diary are to:

1. Provide a simple platform for recording memorable experiences.
2. Combine images and written descriptions into meaningful diary entries.
3. Make diary entries easy to organize using tags.
4. Demonstrate practical Django web development.
5. Demonstrate authentication, database management, templates, and deployment.

---

##  Author

**Japheth Kiprono**

 **Email:** [japhethkiprono2020@gmail.com](mailto:japhethkiprono2020@gmail.com)

 **GitHub:** @jblue254

---

##  License

This project is licensed under the **MIT License**.

Copyright © 2026 **Japheth Kiprono**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions of the MIT License.

The software is provided **"as is"**, without warranty of any kind.

For the complete license terms, see the [`LICENSE`](LICENSE) file included in this repository.

---

###  Contact

For questions, suggestions, or collaboration:

**Japheth Kiprono**
 [japhethkiprono2020@gmail.com](mailto:japhethkiprono2020@gmail.com)
 **@jblue254**
