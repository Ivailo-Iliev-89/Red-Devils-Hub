# Red Devils Hub
### A Dynamic Fan Engagement Platform & Content Management System

***Red Devils Hub***  is a comprehensive fan platform that transitioned from a static frontend to a robust Django-driven ecosystem.
This project demonstrates the ability to manage complex UI components (Swiper.js, Intersection Observer),
while architecting a scalable backend for club news and squad management.


## Key Technical Features

- ***Static to Dynamic Migration*** :  ***Successfully refactored*** 500+ lines of monolithic HTML/CSS into a modular Django architecture with reusable templates and dynamic models.
- ***Real-time Search Engine*** :  ***Integrated***  a custom search functionality in the Navigation Bar to filter the squad and database content via GET requests.
- ***Interactive UI/UX*** :  ***Implemented***  Intersection Observer API for high-performance scroll animations and ***Swiper.js*** for touch-responsive galleries.
- ***Asset Management*** :  ***Architected***  a fragmented CSS structure (`layout.css`, `home.css`, `pages.css`) to ensure maintainability and ***prevent*** style conflicts.
- ***Administrative Control*** :  ***Developed***  a "Club Hub" backend allowing admins to manage news, coach profiles, and team rosters without touching the code.


## Tech Stack

- ***Backend*** :  Python , Django
- ***Frontend*** :  JavaScript (ES6+), CSS3 (Grid and Flexbox), Swiper.js
- ***Database*** :  PostgreSQL ( for Production ) / SQLite ( for Development )
- ***Security*** :  ***Integrated*** `python-dotenv` for secure environment variable management.


## What I Learned

- ***Code Refactoring*** :  The process of breaking down large, monolithic files into manageable, logic-driven Django components.
- ***State Performance*** :  Using the ***Intersection Observer API*** as a lightweight alternative to heavy animation libraries.
- ***Data Presentation*** :  ***Optimizing 300+ lines*** of static code into dynamic Django Views and Models for better scalability.
- ***Brand Identity in Design*** :  ***Customizing*** third-party library styles (Swiper.js) to align perfectly with a specific brand's (Manchester United) visual identity.


## Instructions to setup

- Clone or downloadn the repository:
- ```bash
- git clone https://github.com/Ivailo-Iliev-89/Red-Devils-Hub.git
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


## Usage

- ***News Feed*** :  Stay updated with the latest club news, managed dynamically through the Django Admin dashboard.
- ***Squad Exploration*** :  Use the interactive search bar in the Navbar to instantly find information about your favorite players.
- ***Interactive Journey*** :  Scroll through the platform to experience custom-built "fade-in" transitions and responsive trophy galleries.
- ***Admin Management*** : Leverage the pre-configured `/admin` interface to update the Head Coach profile or add new "Club Hub" entries.


## Future Improvements

- ***Live Score Integration*** :  ***Connecting*** to a Sports API to display real-time match results and upcoming fixtures.
- ***Fan Comments Section*** :  ***Implementing*** a secure discussion area for registered fans to debate match performances.
- ***Player Stats Dashboard*** :  ***Expanding*** the database to include detailed performance metrics for each squad member.

