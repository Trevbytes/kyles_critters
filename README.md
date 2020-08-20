# Kyle's Critters

Future site preview image

Kyle's Critters is my fourth and final milestone project while studying at [The Code Institute](https://codeinstitute.net/).
The purpose of the milestone project is to build an E-commerce website. The site must use the Django framework, a relational database and use Stripe for secure payments. This is my first project using/learning the TDD(Test Driven Development) method.

Kyle's Critters is a online pet store focused on selling small animals such as mice, rats and hamsters.

Future Live Link to Site

## Table of Contents

- [**UX**](#UX)
  - [User Stories](#User-Stories)
- [**Features**](#Features)
    - [Existing Features](#Existing-Features)
    - [Features Left to Implement](#Features-Left-to-Implement)
- [**Technologies Used**](#Technologies-Used)
- [**Database Schema**](#Database-Schema)
- [**Testing**](#Testing)
- [**Deployment**](#Deployment)
    - [GitHub](#GitHub)
    - [Local Deployment](#Local-Deployment)
    - [Remote Deployment](#Remote-Deployment)
- [**Credits**](#Credits)

## UX

These [wireframes](https://github.com/Trevbytes/Chickpeas/blob/master/wireframes/chickpeas_wireframes.pdf) show the original idea for the pages throughout the site.

A user should be able to see if there are substitutes for ingredients in a recipe. This has great value for users with cooking for people with allergies and/or food restrictions.

This project has been created using the TDD Software development model. 

Design changes and additions to the original wireframe ideas have been made throughout the development of the project to improve the user experience. 

Kyle's Critters has been designed with the following main features/goals in mind:

 - Sell product(animals) online.
 - Have user/member feedback about their purchases. A user should be able to leave a review, or post about the pet they purchased.

The color palette was chosen from [coolors.co](https://coolors.co/f7f7ff-c49991-279af1-60656f-131112).
I used MDB (Material Design for Bootstrap) CSS framework in building the design of this site. Icons are provided by the framework and Font Awesome. The fonts used are _, provided by Google Fonts.

### Defensive Design

Features have been added to help prevent unexpected input or site tampering as well as provide privacy and security for the user. These features include:
 - User accounts
    - 
 - Required input
    - Forms use required input fields in order to ensure that data is entered.
 - Default images
    - Default images are used when a user does not enter a URL for an image. If the URL does not work a the default image is also displayed.
 - Privacy
    - 
 - Limited access
    - A non-logged in user can:
        - _
    - A logged in user can: 
        - _
    - An admin can:
        - _

### User Stories

*Work in Progress*

As a User I would like to:
- Use the site on all devices from mobile to desktop.
- Be able to register
- Be able to browse product easily.
- Be able to view information about product.
- Be able to search for products.
- Browse products by catagory.
- Submit my own reviews and posts(when logged in).
- Register or log in to the site simply. 
- Edit and delete posts I have submitted.
- Get visual feedback on interactions with the site.
- Get error messages in case of unexpected issues.
- Receive emails from the site.

With admin access I would like to do everything above as well as:
- .

## Features

### Existing Features

### Features Left to Implement

- **Navagation Bar** - All pages contain the nav bar. It is simple and provides access to the whole site(according to the user type) as well as a built in search bar.
- **Search Product** - This feature is designed to take a user's search request and find product that contain the search request.
- **Home Page** - The first page a new user sees. It is also a page to send users to on logout. Here a user can read about the basic idea of the site.
- **Browse Public Recipes** - This page allows a user to view all public recipes. It is sorted into 4 catagories for easier navigation. A logged in user can edit or delete their submitted recipes or create-and-edit a copy of another's recipe to add to their personal cookbook.
- **Ingredients** - This page allows a user to search through all ingredients in the database. When an ingredient is selected the user can learn more about that ingredient and see common subsitutes, if any have been added.
    - A logged in user can add new ingredients to the database. The user can also fully edit or delete an ingredient created by the user. A user can partially edit ANY ingredient by adding a common subsitute to the selected ingredient.
- **Login/Register** - These two pages are used to handle the simple login and registration process.
- **Dashboard** - The users personal cookbook. Here a user can create a new recipe and view all recipes created by the user, including copied recipes.
- **Create Recipe or Ingredient** - These modals are used to provide the user a form to submit new a recipe or ingredient to the database.  
- **Edit/Copy Recipes** - This modal allows a user to edit their recipes or create and edit a copy of another users recipe. 
- **Delete Recipe/Ingredient** - A user can delete their own recipe or ingredient but not others.  
- **Edit Ingredient** - This modal allows users to edit an ingredient. As mentioned earlier, all ingredients can be edited by users. However, full editing access is granted only to the creator (or admin) of the ingredient.
- **Loading Page** - A simple loading page shown when the site is loading.
- **Error Pages** - In case of unforseen errors these pages will help the user return to the site.
- Implement [Cloudinary](https://cloudinary.com/). Users should be able to upload their own images and the urls should be stored in the database with the recipe.
- Power the search by using Google.
- Add a Rich Text editor, possibly [CKEditor 4 or 5](https://ckeditor.com/), to enable users to format their input text.
- Add a page to email me (or an admin) about site issuses or suggestions.
- Add video tutorials for the features of the site.
- Add metrics to the site. Such as: Total user recipes added and "Liking" of recipes.
- Add the ability to sign in using a third party such as Google or Facebook.
- Add the ability to grant admin access to users.
- Add the ability to reset a forgotten password.
- Pagination.
- Redesign the landing page so that featured product are displayed and selectable.

## Technologies Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)

  - The project uses **HTML 5** to construct the website.

- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - The project uses **CSS 3** to style the HTML elements.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - The project uses **Javascipt** as a source of interactivity in the website. It manipulates both the HTML and CSS elements of the site.

- [Python 3.8.2](https://www.python.org/)

  - The project uses **Python** as the base program which runs the website. It works with the database to execute CRUD functions.

- Postgres

  - The project uses **Postgres** for managing the database. 

- [Material Design for Bootstrap](https://mdbootstrap.com/)

  - The project uses **MDB** to create the layout of the site as well as style most of the elements thorughout the site.

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation in javascript files.

- [Google Fonts](https://fonts.google.com/)

  - The project uses **Google Fonts** for fonts used in the website.

- [Font Awesome](https://fontawesome.com/icons?d=gallery)

  - The project uses **Font Awesome** for icons in the website.

- [Favicon.io](https://favicon.io/)

  - The project uses **Favicon.io** to create favicon icons for the website.

- [Balsamiq Wireframes](https://balsamiq.com/)

  - The project used **Balsamiq Wireframs** to create the initial wireframes of pages.

- [Git](https://git-scm.com/)

  - The project uses **Git** for tracking changes in code during development.

- [GitPod](https://www.gitpod.io/)

  - The project used **GitPod** as the online IDE/workspace during development .

- [GitHub](https://github)

  - The project uses **GitHub** for hosting the webpage and the repository.
  - In this project I learned how create new branches of a repository for development of the project. The landing page of this project was developed in a seperate branch and then merged with the main branch when finished. A development branch was then created to work out remaining bugs and add the final polish to the project before being submitted for assesment.

- [Heroku](https://www.heroku.com/platform)

  - The project uses **Heroku** for hosting the python app/webpage.

- [Cloudinary](https://cloudinary.com/)

  - The project uses **Cloudinary** for storing media outside of app and database.  

- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)

  - The project used **Firefox Developer Tools** for debugging the webpage during development.

- [W3C Markup Validation Service](https://validator.w3.org)

  - The project uses **W3C Markup Validation** for validating code during development.

- [JShint](https://jshint.com/)

  - The project uses **JShint** for validating and improving JS code during development.

- [Am I Responsive](http://ami.responsivedesign.is/)
  - The ReadME used **Am I Responsive** for creating an image of the website on multiple displays to show responsiveness.

- [FreeFormatter](https://www.freeformatter.com/)
  - All HTML pages have been formatted using **FreeFormatter**.

## Database Schema

- The application uses `Postgres` for data storage.  

The Database has _ models: 

**Products**

| Title | Field in db | Form validation type | Data type |
--- | --- | --- | --- 
Product ID | _id | None | Id 

**Ingredients**

| Title | Field in db | Form validation type | Data type | Core Ingredient Field | User Ingredient Field |
--- | --- | --- | --- | --- | ---
MongoDB Ingredient ID | _id | None | ObjectId | Yes | Yes  

**Users**

| Title | Field in db | form validation type | Data type |
--- | --- | --- | --- 
User ID | _id | None | ObjectId 
Username | username | text | string
Hashed Password | user_password | text | string

## Testing

This project as be throughly tested throughout development using the TDD model. Tests for features were created before writing the code for the features. Enough code was written to just pass the test. Then the next test would be written.

Testing documentation can be found in [Testing.md](testing.md)

## Deployment

### GitHub 

[My GitHub Repository](https://github.com/Trevbytes/kyles_critters)

After navigating to my repo you can download the project to a .zip file or open it in the online IDE Gitpod.

<img src="/static/images/readme/clone_repo.jpg">

For more infomation on how to clone or download the repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Local Deployment

*Work in progress*

**To run this project locally**

To run the project locally the following must be installed: 
- An IDE, such as [VS Code](https://code.visualstudio.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/), python requirements installer.
- [Python3](https://www.python.org/downloads/), chosen coding language of the app.
- [GIT](https://www.atlassian.com/git/tutorials/install-git), version control.
- Django


After, download a .ZIP file of my repository ([Master Branch](https://github.com/Trevbytes/kyles_critters)) and unzip this file. In the control line interface, with GIT installed, enter the following command: 
   
    https://github.com/Trevbytes/kyles_critters.git

- Navigate to the root path using the `cd` command. 
- Set up your enviorment variables by creating a `.env` file. Include _ values.
- All requirements from requirements.txt must be installed. Use the following command:
    
        sudo -H pip3 -r requirements.txt
- Create Database
- You should then be able to launch your app using the following command in your terminal:

        python app.py

### Remote Deployment

*Work in progress*

This project is hosted on Heroku with the master branch() deployed.

In order to remotely deploy this project on Heroku the following is the method I recommend.

- Ensure an updated `requirements.txt` exsists in the project. Use the terminal command `pip freeze > requirements.txt` to quickly create/update the file.
- Ensure a Procfile exists, this essientaly lets Heroku know where to start the app. Use the terminal command `echo web: python app.py > Procfile` to quickly create a Procfile. 
- Using git (`git add .`, `git commit -m "<your comment>"`) will stage any created or updated files. After, push the project to GitHub using `git push`.
- Using a browser, naviagte to [Heroku](https://dashboard.heroku.com/login). Login or create a free account.
- Select the "new" button, give the project a name & set the region. 
- After, from the Heroku dashboard of the new app, click on "Deploy" > "Deployment method" and choose GitHub.
- Review and confirm the connection of your Heroku app to your GitHub repository.
- From the Heroku dashboard for the app, select "Settings" and then "Reveal Config Vars".
- Configure the following variables:

| KEY | VALUE |
--- | --- | 
IP | 0.0.0.0|


- In the Heroku dashboard, click "Deploy".
- Congrats, if all went well, the app is now deployed.

## Credits

### Media

- Images 

### Acknowledgements

- When stuck with coding issues, I used the following sites to help understand/solve the issues: [W3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/)
