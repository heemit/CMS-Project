# **Django CMS with GrapeJS - Drag-and-Drop Page Builder**

A modern **Django-based CMS** with **GrapeJS integration** that allows users to create and manage dynamic web pages using a visual **drag-and-drop builder**. This CMS enables **database-driven content rendering**, **media file uploads**, and a **customizable header/footer display** per page.

## **Features**
**GrapeJS Integration** – Drag-and-drop page builder for easy page creation  
**Pages Model** – Stores page URLs and HTML content, allowing dynamic rendering  
**Database-Driven Content** – Supports rendering content from the Django admin  
**Media Uploads in GrapeJS** – Uploaded files can be used within the page editor  
**Custom Header/Footer** – Option to show on all pages or only selected ones  
**Django Admin Support** – Manage pages, media, and settings via the admin panel  

## Requirements

Before starting, make sure you have the following installed:

- **Python 3.x**: The project is built with Python 3.
- **Django>=4.0,<5.0**: The Django framework for web development.
- **Additional Libraries**: 
  - `django-tinymce==3.4.0`: For rich text editing.
  - `django-simple-history==3.0.0`: To track changes to models.
  - `django-model-utils==4.1.1`: For additional model utilities.
  - `whitenoise==6.5.0`: To serve static files in production.
  - `gunicorn==23.0.0`: A WSGI HTTP server for running the app.

## Live Demo

Access the admin dashboard here: [CMS Website](https://jittery-winonah-heemit-cfa0b49d.koyeb.app/admin/)

## Using the CMS

Before starting, make sure you have the following installed:

- **Navigate to the Pages model in the Django admin**
- **Use GrapeJS Editor to visually design pages**
- **Upload and manage media files from the admin**
- **Choose to display header/footer on selected pages**

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment**

    If you don't have a virtual environment already, create one:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    Install the required dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**

    Run the migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**

    To access the Django admin panel, create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser.

6. **Run the development server**

    Start the development server:

    ```bash
    python manage.py runserver
    ```

    Access the site by going to:

    ```
    http://127.0.0.1:8000/
    ```

    The admin panel is available at:

    ```
    http://127.0.0.1:8000/admin/
    ```

7. **Access the website**

    Go to `http://127.0.0.1:8000/` to view the homepage and browse the blogs.

## Images
