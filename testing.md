
This is an extension from the [README.MD](README.md) file.

Future Live Application link


# Table of Contents
1. [**TDD Documentation**](#tdd-documentation)

2. [**Known Issues**](#known-issues)
    - [**Resolved**](#resolved)
    - [**Unresolved**](#unresolved)

3. [**Pre-Release Testing**](#pre-release-testing)
    - [**Code Testing**](#code-testing)
        - [**Validator Testing**](#validator-testing)
        - [**Compatibility Testing**](#compatibility-testing)
    - [**Functional Testing**](#functional-testing)  
        - [**Automated Testing**](#automated-testing)
        - [**Manual Testing**](#manual-testing)
        - [**User Testing**](#user-tests)

---
## TDD Documentation
---
- [X] A superuser can navigate to */admin to login and access admin controls.
- [X] A user can login via URL naviagation */accounts/login.
    - Base template created.
    - Setup Allauth. users can signup/login by email.
- [ ] A user can login via Google
    - Added home app to be redirected to when logged in.
    - Google sign in connected. Cannot use the redirect function until the site is deployed on Heroku. Other login accounts will be added at this time.
- [X] A user can navigate to different pages via a url.
    - Set up basic sturcture all apps to allow for navigation to the pages. All tested urls return a 200 response.    
- [X] A user can navigate to the different pages via the navbar.
- [X] A product can be registered into the store.
    - Product models and catagories set up.
- [X] Products can be seen on the products page.
    - Connected products to the html page.
- [X] Featured products display on the homepage.
    - Featured option added to product model. Featured products are shown on the homepage.
- [X] Products are sorted and filtered on the products page. Products can be searched.
    - Working search bar added to navbar.
- [X] Products can be filtered by catagories and subcatagories.
    - Nav bar and search bar can be used to filter products by catagories.
- [X] A single product with details can be viewed.
    - A details page product added.
- [X] Products can be added to a cart and be viewed on a page.
    - Started to write automated tests. Due to the simplicity of the add to cart forms, I removed the automated tests. Products can be added from the view products detail page. The cart can be viewed by clicking on the paw on the navbar.
- [X] Products can be updated and removed from the cart page.
    - Quantity update and remove item buttons added.
- [X] Alert messages are shown when the cart is modified.
    - Alerts added when adding, updating, and removing items from the cart.
- [X] A user can 'checkout'. Providing checkout infomation such as billing address, delivery address and order details.
    - Created a form for shopper information and finished first draft of the checkout template.
- [X] A user can pay via secure checkout by Stripe. 
    - Orders can be processed using a test card. Webhooks are attached but not fully functional.
- [X] A user can view their order history as well as save their user information.
    - User profile page added. Added a form to store default profile information. Added order history to the profile page.
- [X] An admin can add, remove, and edit products.
    - Added pages to add and edit products. Added view and url to delete products.
- [X] A user can request to loan available critters.
    - Added models and forms to handle a user sending in a request form.
- [ ] A logged in user can add a gallery entry with a picture and basic info. 

---
## Known Issues
---

Most errors throughout the project have been simple syntax errors that took very little time to locate and correct. Some of the larger issues/bugs can be found below.

##### Resolved

##### Unresolved

- A 404 error with no error details has been seen a few times throughout building the project. The exact reason I suspect has something to do with allauth. The current quick fix is to change the SITE_ID in the settings. After changing the id the project works again. 

---
## Pre-Release Testing
---
These other tests were done when the original project was complete but not ready for full release. 
---
### Code Testing
---
#### Validator Testing

[W3C Markup Validation](https://validator.w3.org/)

W3C was used for HTML and CSS validation.
- No errors were found.

[JSHint](https://jshint.com/)

JSHint was used to validate the Javascript files.

[JSesprima](https://esprima.org/demo/validate.html)

JSeprima was used to validate JS formatting.

[PEP8online](https://pypi.org/project/autopep8/)

PEP8online was used to validate formatting of python code. 

#### Compatibility Testing

This project has been tested for display responsiveness throughout development. : 
 - Browsers
    - Firefox Developer Edition
    - Chrome
    - Firefox
    - Opera
    - Microsoft Edge
    - Samsung Internet
 - Screen Sizes
    - 27-inch display
    - 17-inch display
    - 15-inch display
    - 13-inch display
    - 10-inch display
    - 6-inch display
    - 5-inch display    



---
## Functional Testing
---
#### Automated Testing

#### Manual Testing

The manual testing and debugging of this project was done with Firefox Developer Tools throughout the project. These test mainly consisted of visual testing of the site.

In order to ensure the site works as required, I manually tested all aspects of the deployed site.

**Placeholder text**
- Check that all links in navbar, both when logged in and when logged out, work.
    - No errors


#### User Testing

This project have been reviewed/tested by an experienced web developer. A mentor provided by Code Institute during my studies.

This project have been reviewed/tested by friends and family.

A Full Usability test was done when all features were in place. This was done to identify possible bugs as well as ensure that the application is easy-to-use.
- Test Audience - A new user interested in purchasing a pet.

    User Actions:


**Feedback From User Test**

After this full test the following feedback was given:


**Errors After User Test**