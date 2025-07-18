Quick Fix (Car Repair Service Near You) Web Application
=======================================================

Prerequisites:
- Python 3.6.4
- Flask 1.0.2
- Visual Studio Code (recommended IDE)
- Google Chrome (recommended browser)

Instructions to run the web application:
1. Open the command prompt and ensure it is pointing to the project directory "\5591020_Code".
2. Create a virtual environment by running the command: python -m venv .venv_flask
3. Activate the virtual environment by running: .\.venv_flask\Scripts\activate
4. Setup Requirements.txt: pip install -r requirements.txt
5. Start the application by executing: python app.py
5. Open Google Chrome and navigate to the local web address "http://127.0.0.1:5000/" to view the web application.

Video 2 will show the steps to run the web application.

Directory Structure Overview
----------------------------

Here's a detailed explanation of the main directories and their contents for the "Quick Fix" web application:

- /Quick_Fix_Components
  - /__pycache__: Contains compiled Python files that help speed up script execution.
  - /core: Contains the core Python files and modules that are essential for the backend functionality of the application.
  - /static: This directory is used to serve static files like stylesheets, JavaScript files, images, and other assets.
    - /css: Contains CSS files for styling the web application. Each .css file typically corresponds to a specific HTML page or component.
    - /img: Stores image files used throughout the application, such as logos, icons, and photographs.
    - /js: Contains JavaScript files that add interactivity to the web pages.
    - /lib: Includes libraries or third-party JavaScript or CSS frameworks that the application depends on.
    - /media: Holds additional media files like video.
  - /templates: Contains HTML template files which define the structure and layout of the web pages in the application.
  
- /__init__.py: A file that indicates the directory is a Python package. This allows the files within to be imported elsewhere in the project.

- app.py: This is the main entry point of the Flask web application. Running this file starts the web server and serves the application.

- /Screen-Captured Images: Contains images of the website that may be used in the project report.

- /Video: Contains videos that are referenced in the project report.