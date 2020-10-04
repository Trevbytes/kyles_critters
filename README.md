# Kyle's Critters

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0b9aa3268c64cb696525ecf38318c8b)](https://app.codacy.com/manual/Trevbytes/kyles_critters?utm_source=github.com&utm_medium=referral&utm_content=Trevbytes/kyles_critters&utm_campaign=Badge_Grade_Settings)

<img src="https://res.cloudinary.com/chickpeas/image/upload/v1601499934/kyles_critters/screenshots/homepage_kyfy3v.jpg">
<img src="https://res.cloudinary.com/chickpeas/image/upload/v1601499963/kyles_critters/screenshots/responsive-site_grqdhq.jpg">

Kyle's Critters is my fourth and final milestone project while studying at [The Code Institute](https://codeinstitute.net/).
The purpose of the milestone project is to build an E-commerce web app. The site must use the Django framework, a relational database and use Stripe for secure payments. This is my first project using/learning the TDD(Test Driven Development) method.

Kyle's Critters is a online pet store focused on selling small animals such as mice, rats and hamsters. Kyle wants two additonal features in his store.

The first feature he wants is to promote his customer community. Customers can upload pictures of the Critters they have bought at the store, share a short story and publish this picture to the store for future customers to see.

The second feature Kyle wants is for customers to be able to loan critters from the store. As this is a new idea, not all the terms and conditions have been considered. But to start, customers can send a request to loan available critters. The store's staff can then reach out to the customer to negotiate terms.

[Live Link to Site](https://kyles-crittersv1.herokuapp.com/)
- For test purchases, use the card number 4242 4242 4242 4242, any CVC and any future experation date.

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

These [wireframes](wireframes.md) show the original idea for the web app.

Some design changes and additions to the original wireframe ideas have been made throughout the development of the project to improve the user experience. 

The site is designed for a start up pet store to begin selling product.

The optimal viewing device for the site would be a tablet sized device. By designing the site with this in mind, the store can use the web app in a physical store instead of a register.

<img src="https://res.cloudinary.com/chickpeas/image/upload/v1601500129/kyles_critters/screenshots/store_fz7hba.jpg">

Kyle's Critters has been designed with the following main features/goals in mind:

 - Sell product(animals) online.
 - Have user/member feedback about their purchases. A user should be able to leave a review, or post about the pet they purchased.
 - Users should be able to login and upload pictures of critters they have purchased from the store. 

Delivery options have not been added as the startup store has limited delivery options. Delivery can be negotiated on an order by order basis.

The color palette was chosen from [coolors.co](https://coolors.co/f7f7ff-c49991-279af1-60656f-131112). The colors used are tied to single CSS variables. This allows a color change of the web app with minimal coding. This could be useful for a future feature of individual user color customization or a general change of the stores theme colors. 

I used MDB (Material Design for Bootstrap) CSS framework in building the design of this site. Icons are provided by the framework and Font Awesome. The font used is the default font of MDB, Roboto, provided by Google Fonts.

Outside of the Django admin pages. Additonal, user friendly pages were added to allow easy management of product and gallery entires. 

### Defensive Design

All secret keys are stored in enviorment variables, with one exception. Google Maps secret key is visable in the code and can be found in the repository. To secure missue of this key, access with the key has been restricted via Google settings. 

Purchase quantites have been limited to 20 or less of each product per purchase. As most purchases will most likely be of quantities of 5 or less, 20 is set as a percaution but can be easily adjusted. Users are not allowed to add more and receive a message if they try to do so.

Features have been added to help prevent unexpected input or site tampering as well as provide privacy and security for the user. These features include:
 - User accounts
    - Allauth is used to create secure user accounts. Email verification is requried to create an account. All passwords are hashed.
 - Required input
    - Forms use required input fields in order to ensure that important data is entered.
 - Default images
    - Default images are used for missing or broken images.
 - Limited access
    - A non-logged in user can:
        - View and purchase products.
        - Request to loan a critter.
        - View the critter gallery.
    - A logged in user can additionally: 
        - Store default user information.
        - View order and loan request history.
        - Manage email addresses and social accounts tied to their account.
        - Post a gallery entry with a image and text entry.
        - Edit/Remove gallery entries tied to their account.
    - Staff can additionally:
        - Add/Edit/Remove products.
        - Edit/Remove gallery entries in order to moderate content.
        - Perform other functions granted by a Super User such as view orders and requests.
    - A Super User:
        - Has full access to the site and can grant permissions to other users.
        - Can edit and manage almost everything from the Django admin pages. Some fields in orders and entires are uneditable to prevent tampering.

### User Stories

As a User I would like to:
- Use the site on all devices from mobile to desktop.
- Be able to browse product easily.
- Be able to view information about products.
- Be able to search for products.
- Browse products by catagory.
- Add products to a cart.
- Make a secure purchase of the items in the cart.
- Make a loan request.
- View all critters in the gallery.
- Get visual feedback on interactions with the site.
- Get error messages in case of unexpected issues.
- Receive confirmation emails from the site.
- Be able to register by email, Google or Facebook.
- Be able to send an email message to the store.
- Locate the store with Google Maps.

As a Registered User I would like to additionally:
- Manage stored infomation such as default user information, email and connected social accounts.
- View previous orders and loan requests.
- Prefill forms with stored information.
- Submit galley entries.
- Edit and delete entries I have submitted.

With staff access I would like to additionally:
- Add/Edit/Remove products.
- Edit/Remove gallery entries in order to moderate content.
- Perform other functions granted by a Super User such as view orders and requests.

As a Super User I would like to additionally:
- Have full access to site and admin pages.

## Features

### Existing Features
- **Navagation Bar** - All pages contain the nav bar. It is simple and provides access to the majority of the web app(according to the user type) as well as a built in search bar.
- **Footer** - The footer is visable on all pages. It contains store information as well as:
    - Google Maps modal - A simple Google map is used with no pinpoint on a location. This is for privacy purposes. The current store address is fake, no location is specified on the map to prevent potential confusion.
    - Send Message modal - A basic message form that allows users to send an email to the stores email address without giving to stores email address explicitly. This is to prevent pesky bots sending spam mail to the stores email address.
    - Quick links to common pages as well as the privacy policy and terms & conditions modals.
    - Links to social media - Currently sending the user to the homepages of the respective sites. No social accounts have been created for the store.
- **Search Product** - This feature is designed to take a user's search request and find product that contains the search request.
- **Home Page** - The first page a new user sees. It is also a page to send users to on logout. Here a user can read about the basic idea of the site as well as view featured critters.
- **Product Catalog** - The product catalog shows all the products in the database. Filters in views.py are used to filter the products shown.
    - On each card a user can:
        - Click on the image or 'More info' to navigate to the product details page.
        - Click on the 'Add 1 to Cart' to quickly add a product to their cart. This is useful for 'in store purchases' as well as for returning customers.
        - Edit the product, if the user has the appropriate permissions.
- **Product Details** - This page shows product details. It also allows users to add a larger quantity of the product to the cart.
        - A filtered gallery is displayed on this page. This shows gallery entries that match the critter type.
            - For example - The product detail page of 'Rat' shows all gallery entires of the critter type 'Rat'.
- **Loan a Critter App** - This page contains a form for a user to fill out to request an available critter to loan. Available critters are determined by the store and are displayed as images for the user to click to add it to the form.
    - When a form is submitted a copy is sent to the user's email address as well as the store's. The information is also stored in the database.
    - If a logged in user makes a loan request the request is tied to their account and can be viewed on the profile page.
- **Critter Gallery App** - Logged in users are able to add a gallery entry to this app via the Critter Gallery page. It is intented for users who have purchased critters from the store.
    - A gallery entry consists of: the purchased critters name, the critter type, an optional short story about the critter and a user uploaded image of the critter in it's new home.
    - The main critter gallery page contains all entries. A filtered selection of the gallery can be found on product detail pages as well as a users profile page.
    - A logged in user can add/edit/remove their own gallery entry(s).
    - Users with granted permissions can edit/remove gallery entries in order to moderate content. 
- **User Profile page** - This page allows a user to easily access all the users information for the web app.
    - A user can create an account by registering with a verifified email address or via Google or Facebook.
    - A user can update their default information in order to prefill forms.
    - A user can manage their email address(s) and social accounts tied to the app.
    - A user can view thier previous orders and requests as well as view a copy of confirmation details.
    - A user can view all of their entries to the Critter Gallery.
- **CKEditor 6** - CKEditor is used throughout the site to allow users access to a Rich Text Editor. This allows users to format longer text such as descriptions, messages and critter stories.

### Features Left to Implement
- Redesign/Refactor Gallery Entries so that all entry information can be presented on all browsers. Currently Apple devices will not create overflow content on the back of entries and have therefor have been disabled for these type of devices. 
- Refactor models and code to implement Cloudinary's Upload Widget. This would allow users to view and crop their image before uploading. An attempt was made and code has been written to make this happen. Due to time constraints this feature has been moved to future development. Below you can find an image of what the upload widget looked like.

<img src="https://res.cloudinary.com/chickpeas/image/upload/v1601823226/kyles_critters/screenshots/widget_uxx2yp.jpg">
 
## Technologies Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)

  - The project uses **HTML 5** to construct the website.

- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - The project uses **CSS 3** to style the HTML elements. Most CSS is from **MDB** and is used by adding certain classes to elements.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - The project uses **Javascipt** as a source of interactivity in the website. It manipulates both the HTML and CSS elements of the site.

- [Python 3.8.2](https://www.python.org/)

  - The project uses **Python** as the base program which runs the website. It works with the database to execute CRUD functions.

- [Django](https://www.djangoproject.com/)

  - The project is built on the **Django** framework. 

- [Postgres](https://www.postgresql.org/)

  - The project uses **Postgres** for managing the SQL database. 

- [Material Design for Bootstrap](https://mdbootstrap.com/)

  - The project uses **MDB** to create the layout of the site as well as style most of the elements throughout the site.

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation in javascript files.

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

- [Stripe](https://stripe.com/)
    - The project uses **Stripe** to process secure payments. 

- [Cloudinary](https://cloudinary.com/), used for all media storage.
    - The project uses **Cloudinary** for all media storage. Cloudinary allows users to upload files directly to the Cloudinary cloud.

- [Google APIs](https://console.developers.google.com/)
    - The project uses **Google** to provide login via Google as well as access to **Google Maps** in the site.

- [Facebook for Developers](https://developers.facebook.com/)
    - The project uses **Facebook** to provide login via Facebook.

- [WhiteNoise](http://whitenoise.evans.io/en/stable/)
    - The project uses the python library **WhiteNoise** to allow the app to serve its own static files.

- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)

  - The project used **Firefox Developer Tools** for debugging the webpage during half of the development.

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - The project uses **Chrome Developer Tools** for debugging the webpage during the second half of development.

- [W3C Markup Validation Service](https://validator.w3.org)

  - The project uses **W3C Markup Validation** for validating code during development.

- [JShint](https://jshint.com/)

  - The project uses **JShint** for validating and improving JS code during development.

- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
  - The ReadME used **Responsive Viewer** for creating an images of the website on multiple displays to show responsiveness.

- [BrowserStack](https://www.browserstack.com/)
  - In order to test the web app on Apple devices, **BrowserStack** was used.

- [FreeFormatter](https://www.freeformatter.com/)
  - All HTML pages have been formatted using **FreeFormatter**.

- [PolicyMaker](https://policymaker.io/)
  - The project used **PolicyMaker** to create privacy policy and terms and conditions documents.

## Database Schema

- The application uses `Postgres` for data storage.  

The Database has 8 models: 

**Profiles**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone Number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True 
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True

**Orders**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order Number | order_number | CharField | max_length=32, null=False, editable=False 
 User Profile | user_profile | ForeignKey 'UserProfile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | full_name | CharField | max_length=50, null=False, blank=False
 Email | email | EmailField | max_length=254, null=False, blank=False
 Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
 Country | country | CountryField | blank_label='Country *', null=False, blank=False
 Street Address | street_address1 | CharField | max_length=80, null=False, blank=False
 Street Address2 | street_address2 | CharField | max_length=80, null=True, blank=True
 Town or City | town_or_city | CharField | max_length=40, null=False, blank=False
 County | county | CharField | max_length=80, null=True, blank=True
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original Cart | original_cart | TextField | null=False, blank=False, default=''
 Stripe Public ID | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

**Line Item Orders**
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems'
 Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE
 Quantity | quantity | IntegerField | null=False, blank=False, default=0
 Lineitem Total | lineitem_total | DecimalField | max_digits=8, decimal_places=2, null=False, blank=False, editable=False

**Product Categories**
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category Name | name | CharField | max_length=254
 Category Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True
 
**Product SubCategories**
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 SubCategory Name | name | CharField | max_length=254
 SubCategory Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True
 
**Products**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL)
 SubCategory | sub_category | ForeignKey 'SubCategory' | null=True, blank=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=254, null=False, blank=False
 Product Name | name | CharField | max_length=254, null=False, blank=False
 Product Description | description | RichTextField | blank=True, null=True
 Price | price | DecimalField | max_digits=6, decimal_places=2
 Image | image | CloudinaryField | 'image', null=True, blank=True
 Featured Product | featured | BooleanField | null=False, blank=False, default=False
 Ready to loan product | ready_to_loan | BooleanField | null=False, blank=False, default=False
 Out of Stock Product | out_of_stock | BooleanField | null=False, blank=False, default=False 
 Created Date | created_at | DateTimeField | auto_now_add=True, editable=False
 Edited Date | modified_at | DateTimeField | auto_now=True, editable=False

**Gallery Entries**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Entry Number | entry_number | CharField | max_length=32, null=False, editable=False
 Created By | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='entries'
 Critter Name | critter_name | CharField | max_length=50, null=False, blank=False
 Critter Type | critter_type | ForeignKey | Product, null=True, blank=True, on_delete=models.SET_NULL
 Critter Info | critter_info | RichTextField | null=True, blank=True
 Entry Image | image | CloudinaryField | 'image', null=True, blank=True
 Entry Date | date | DateTimeField | auto_now_add=True

**Loan Requests**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order Number | order_number | CharField | max_length=32, null=False, editable=False 
 User Profile | user_profile | ForeignKey 'UserProfile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | full_name | CharField | max_length=50, null=False, blank=False
 Email | email | EmailField | max_length=254, null=False, blank=False
 Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
 Country | country | CountryField | blank_label='Country *', null=False, blank=False
 Street Address | street_address1 | CharField | max_length=80, null=False, blank=False
 Street Address2 | street_address2 | CharField | max_length=80, null=True, blank=True
 Town or City | town_or_city | CharField | max_length=40, null=False, blank=False
 County | county | CharField | max_length=80, null=True, blank=True
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Critter Request | critter_request | CharField | max_length=100, null=True, blank=True
 Request Info | request_info | RichTextField | null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True


## Testing

This project as be throughly tested throughout development using the TDD model. Tests for features were created before writing the code for the features. Enough code was written to just pass the test. Then the next test would be written.

Testing documentation can be found in [Testing.md](testing.md)

## Deployment

The deployed project can be viewed on the following link: [Kyle's Critters](https://kyles-crittersv1.herokuapp.com/)

In order to have full functionality after deployment the following accounts must be set up:
- [Stripe](https://stripe.com/), used to process payments.
    - Sign up for an account. After signing up and verifiying your email you will need your API keys. A publishable key and a Secret key. Create a webhook endpoint in order get your webhook signing secret key.  
- [Cloudinary](https://cloudinary.com/), used for all media storage.
    - Create a Cloud. For more info follow step 1 in the [Cloudinary Get Started Docs](https://cloudinary.com/documentation/how_to_integrate_cloudinary). 
- [Google APIs](https://console.developers.google.com/), used for Google Maps and login via Google.
    - Create a new project. Set up a Maps API key and a OAuth2.0 Client ID.
    - The document I used to get started with the API console can be found [here](https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5). Follow step 7.
- [Facebook for Developers](https://developers.facebook.com/), used for login via Facebook.
    - Create a new app after the site is deployed, follow the Quickstart for Facebook Login
        - For more info follow the [Facebook Login Docs](https://developers.facebook.com/docs/facebook-login/).
        - For a video tutorial on setting up Facebook login watch [this video](https://www.youtube.com/watch?v=m5sHDaBwxjc&ab_channel=ParwizForogh).
### GitHub 

[My GitHub Repository](https://github.com/Trevbytes/kyles_critters)

After navigating to my repo you can download the project to a .zip file or open it in the online IDE Gitpod.

<img src="/static/images/readme/clone_repo.jpg">

For more infomation on how to clone or download the repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Local Deployment

**To run this project locally**

To run the project locally the following must be installed: 
- An IDE, such as [VS Code](https://code.visualstudio.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/), python requirements installer.
- [Python3](https://www.python.org/downloads/), chosen coding language of the app.
- [GIT](https://www.atlassian.com/git/tutorials/install-git), version control.

After, download a .ZIP file of my repository ([Master Branch](https://github.com/Trevbytes/kyles_critters)) and unzip this file. In the control line interface, with GIT installed, enter the following command: 
   
    https://github.com/Trevbytes/kyles_critters.git

- Navigate to the root path using the `cd` command. 
- Set up your enviorment variables by creating a `.env` file(Add your env.py file to .gitignore). Include the following keys and your own values:
    - "SECRET_KEY" = <'your django secret key'>
        - New keys can be generated online. [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/), is one place generate a new key.
    - "DEVELOPMENT" = 'TRUE' (set this variable to False when publishing)
    - "CLOUDINARY_CLOUD_NAME" = <'your value'>
    - "CLOUDINARY_API_KEY" = <'your value'>
    - "CLOUDINARY_API_SECRET" = <'your value'>
    - "STRIPE_PUBLIC_KEY" = <'your value'>
    - "STRIPE_SECRET_KEY" = <'your value'>
    - "STRIPE_WH_SECRET" = <'your value'>
    - "GOOGLE_MAPS_API_KEY" = <'your value'>

- All requirements from requirements.txt must be installed. Use the following command:
    
        sudo -H pip3 -r requirements.txt
- Set up your Django SQLite3 database.

        python3 manage.py makemigrations
        python3 manage.py migrate
- Create a Django super user.

        python3 manage.py createsuperuser
- You should then be able to launch your app using the following command in your terminal:

        python3 manage.py runserver
- Add '/admin' to the locally deployed project's URL and login with your new super user account. Verify your email account. After verification you can access the admin site through the navigation bar when you are logged in as a super user or staff.
### Remote Deployment

This project is hosted on Heroku with the [master branch](https://github.com/Trevbytes/kyles_critters) deployed.

In order to remotely deploy this project on Heroku the following is the method I recommend.

- Ensure an updated `requirements.txt` exsists in the project. Use the terminal command `pip freeze > requirements.txt` to quickly create/update the file.
- Ensure a Procfile exists, this essientaly lets Heroku know where to start the app. Use the terminal command `echo web: gunicorn kyles_critters.wsgi:application > Procfile` to quickly create a Procfile. 
- Using git (`git add .`, `git commit -m "<your comment>"`) will stage any created or updated files. After, push the project to GitHub using `git push`.
- Using a browser, naviagte to [Heroku](https://dashboard.heroku.com/login). Login or create a free account.
- Select the "new" button, give the project a name & set the region. 
- After, from the Heroku dashboard of the new app, click on "Deploy" > "Deployment method" and choose GitHub.
- Review and confirm the connection of your Heroku app to your GitHub repository.
- From the Heroku dashboard for the app, select "Settings" and then "Reveal Config Vars".
- Configure the following variables:

| KEY | VALUE |
--- | --- | 
SECRET_KEY | your django secret key
CLOUDINARY_CLOUD_NAME | your cloudinary cloud name
CLOUDINARY_API_KEY | your value
CLOUDINARY_API_SECRET | your value 
STRIPE_PUBLIC_KEY | your value
STRIPE_SECRET_KEY | your value
STRIPE_WH_SECRET | your value
GOOGLE_MAPS_API_KEY | your value

- In the Heroku dashboard, click "Deploy".
- Congrats, if all went well, the app is now deployed. Don't forget to configure your Stripe, Cloudinary, Google and Facebook accounts for the new site.
- Set up a Postgres database after you have connected the project to Heroku.
- Under the resources tab in Heroku you should add the addon Heroku Postgres.
- After this is set up run the following code in your IDE to set up the new database.

        python3 manage.py makemigrations
        python3 manage.py migrate
- Don't forget to configure your Stripe, Cloudinary, Google and Facebook accounts for the new site.

## Credits

### Code
- This project has many roots in the mini-project [Boutique Ado]( https://github.com/mkthewlis/boutique-ado), which was part of *Code Institute's* course material. Although many alterations have been made, the 'cart', 'checkout', 'products' and 'profiles' apps were built upon the course material.

### Media

- All images used in this site by me were from [Pixabay](https://pixabay.com/). All images used in this site or uploaded by me are free for commercial use with no attribution required.

### Acknowledgements

- For the gallery masonry these two sites were used:
    - [Masonry](https://masonry.desandro.com/), for the CSS grid layout.
    - [Images Loaded](https://imagesloaded.desandro.com/), to detect when images have been loaded.
- A [blog by Zoe Chew](https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) on how to set up Google login was very helpful in coding that part of the app. 
- When stuck with coding issues, I used the following sites to help understand/solve the issues: [W3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/)
- A big thank you to my family and friends who have helped me with testing and support throughout this course.
> **_NOTE:_** This project was created for educational purposes only