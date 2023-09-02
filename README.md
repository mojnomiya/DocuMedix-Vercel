# DocuMedix : Docu-Management for Medical Excellence

## Live Link:
https://documedix.pythonanywhere.com/

## Project Description

The DocuMedix is a web-based platform designed to meet the specific needs of doctors in managing patient records. It provides doctors with the ability to create accounts, log in securely, and log out when they are done. Once logged in, doctors can input and save patient details, including information such as name, age, and address. The system allows doctors to view and manage their patients' information on their profile pages. Patient records are displayed on the main page of the website, and doctors can use a search bar to quickly find specific patient information. Additionally, doctors can sort patient records into categories such as "Cardiology" and "Neurology."

## Features

### User Accounts

- Doctors can securely create accounts.
- A login and logout system is implemented for easy access.

### Patient Details Entry

- Doctors can input and save details about their patients.
- Patient information includes attributes like name, age, address, and more.

### Doctor Profile Page

- Display all patient records associated with a specific doctor on their profile page.
- Doctors can easily review and manage their patients' information, including the ability to edit and delete records.

### Data Display

- The homepage showcases all the records entered by doctors.
- Patient information is displayed in a structured and organized format.

### Search and Sort Functionality

- A search bar allows doctors to quickly locate specific patient records.
- Doctors can sort patient records by categories, such as "Heart Patients" and "Liver Patients."



## Technologies Used

- **Django:** The web framework used for backend development.
- **HTML/CSS:** Frontend development for user interfaces.
- **JavaScript:** Used for dynamic functionality.
- **SQLite:** Database for storing patient records.
- **Bootstrap:** Database for storing patient records.


## Project Structure

- **`patient` App:** Contains models, views, and templates related to patient management.
- **`doctor` App:** Manages doctor accounts and profiles.
- **`templates` Directory:** Contains HTML templates for rendering pages.
- **`static` Directory:** Stores static files such as CSS and JavaScript.
- **`media` Directory:** Stores media files such as images and docs.

## Usage

1. Visit the website's homepage.
2. Create a doctor account or log in if you already have one.
3. Once logged in, you can add patient details, review patient records on your profile page, and use the search and sort functionality on the main page.
4. Log out when done.

## Installation

To run the project locally:

1. Clone this repository to your local machine.
2. Set up a virtual environment for the project.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Apply migrations using `python manage.py migrate`.
5. Create a superuser account using `python manage.py createsuperuser` for admin access.
6. Run the development server with `python manage.py runserver`.

## Deployment

The DocuMedix can be deployed to a web hosting platform for online access. Ensure you have a reliable hosting service and follow their deployment guidelines.

## Authors

- Md Mojno Miya

## Acknowledgments

- This project was developed as part of of the final project [Project No: 12](#project-no-12) for [CSE Fundamentals With Phitron/Phitron].


## Credits
- Theme : Inspired from themeforest.net, ProClinic - Bootstrap4 Hospital Admin Template
---
