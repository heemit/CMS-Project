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

Access the admin dashboard here: [CMS Website](http://ec2-3-110-188-209.ap-south-1.compute.amazonaws.com:8000/admin/)

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

![image](https://github.com/user-attachments/assets/26dea587-912f-48ff-92df-dd4f9ea74061)

![image](https://github.com/user-attachments/assets/a11d79a7-55ca-4670-9df3-8616e3e7a46e)

![image](https://github.com/user-attachments/assets/cb1c33c9-49a4-4d05-85ae-4d7ca089e1d2)

![image](https://github.com/user-attachments/assets/5ca68749-0236-4a92-9caf-5b7eab5fd527)

![image](https://github.com/user-attachments/assets/854c784b-0bc3-4402-b3ce-a9b763d12924)

![image](https://github.com/user-attachments/assets/46862966-04d8-4644-8e4d-7cc6219e4a29)

![image](https://github.com/user-attachments/assets/f0707841-b629-4110-ab2a-32e963f391ef)

![image](https://github.com/user-attachments/assets/bf5c8271-66a3-4a67-8b08-9871e4e7d43f)

![image](https://github.com/user-attachments/assets/cdb75f5b-f6cf-48ac-a626-dc2efb72ff23)

![image](https://github.com/user-attachments/assets/f280c412-be28-49e5-83d0-c9695d226cb9)

![image](https://github.com/user-attachments/assets/887fc8c1-5ac4-4fa6-895b-f62e44548ac3)

![image](https://github.com/user-attachments/assets/dda718ac-87bf-4894-a1ba-dc032d764fc1)
