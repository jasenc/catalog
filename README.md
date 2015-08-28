# Catalog

This application can be seen live at [Catalog Application](https://fathomless-cove-4387.herokuapp.com/).

This Web App was developed to create a catalog of various items throughout various categories. Development was done in Flask along with various extensions, SQLite3, and Bootstrap assisting for style.

This Web App has the following features:

* An index page that shows all categories, the 10 most recently added items and what category they belong to.
* Third-Party user Authentication using Google+
* The ability to create new items, with images, for users who are logged in.
* The ability to update and delete items for users who are logged in and the item's original author.
* API endpoints for JSON and XML.
* Protection from cross-site request forgeries.

## Installation

If one should choose to use this Web App for their own personal use please follow these guides to ensure proper functionality.

* Clone this repository.
* Download necessary packages in to your working directory using `pip freeze > requirements.txt`.
* Run `python database_setup.py`.
* Run `python lotsofitems.py`.
* Run `python runserver.py`.
* Navigate to `localhost:5000` in your favorite browser.

Note: the client information for Google Oauth has been removed from this repository and will not work locally without the missing information.

## Authors
Jasen Carroll  
jasen.c@icloud.com  
August 21st, 2015

## Issues and Feature Requests

* Depending on your Chrome configuration and the number of active users, this application may need to be opened Incognito in order for the authentication to work properly.

Please use GitHub to notify me of any issues or feature requests.

Navigate to the repository on GitHub.
Click the Issues link on the menu towards the right.
Then click New issue.
Pull Requests are encouraged! Please do no hesitate.
