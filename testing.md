
This is an extension from the [README.MD](README.md) file.

[Live Link to Site](https://kyles-crittersv1.herokuapp.com/)


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
This project was my first project using the Test Driven Development(TDD) model. This model aims to write tests for the project before writing the code for that part of the project. Each test was written to fail at first as the code was not written for the tests to pass. I would then try to write the minimum code required to pass the tests. If these tests still failed I would determine if it was the tests that were written poorly or if there was an error in the code. If the tests passed I would refactor and add style to the code. Before moving on to the next test, previous tests should be passing.

Due to my inexperience with writing automated tests often I would find later that a test was written with some errors which would need to be corrected before the tests would work as intended.
To complement the automated testing, I wrote manual tests to follow the pattern of writing failing tests before writing code.  As some of the apps in the project became more complicated it became more difficult to write automated testing. The current issue with the automated testing in this project happened after I added a Rich Text field to objects(CKEditor). Now all tests that contain a Rich Text field in the object, fail. 

The TDD method helped me identify early bugs when developing the apps and helped me stay focused on one area of the project at a time.

Below is a list of the manual tests, listed by chronological order. General styling, refactoring and tidying up code were done after all these tests passed. Manual tests of the full project were then done by myself as well as others.

- [X] A superuser can navigate to */admin to login and access admin controls.
- [X] A user can login via URL naviagation */accounts/login.
    - Base template created.
    - Setup Allauth. users can signup/login by email.
- [X] A user can login via Google
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
- [X] A logged in user can add a gallery entry with a picture and basic info.
    - Gallery set up. An entry can be created and shown in the gallery. 

---
## Known Issues
---

Most errors throughout the project have been simple syntax errors that took very little time to locate and correct. Some of the larger issues/bugs can be found below.

##### Resolved

- A 404 error with no error details has been seen a few times throughout building the project. The exact reason I suspect has something to do with allauth. The current quick fix is to change the SITE_ID to '2' in the settings. After changing the id the project works again. 
- A Server Error 500 happend when a user submited a Gallery Entry with no critter type.
    - This error happened due to the 'Critter Type' badge located in entries. If no critter type was given no working link would be generated causing all pages with that entry to crash.
    - Python logic was added to the template to not generate the badge if no critter type is given.
- Negative numbers or absurdly large numbers could be used for the price of products or for quantities.
    - Number validation has been added to prevent unintened quantity/price values.
##### Unresolved

- If a product is removed from the store that is stored in a user's web browser cookies, the error of 'The requested resource was not found on this server' appears for the user. The user can not access the site while those cookies are removed. 
   
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

- One error has been found on pages that utialize the CKEditor. The message form (contact us) contains a CKEditor. When more than one CKEditor is on a page, a duplicate id of 'ckeditor-init-script' is created.
- No errors were found on code written by myself.

[JSHint](https://jshint.com/)

JSHint was used to validate the Javascript files.
- No errors found.

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

This project used [BrowserStack](https://www.browserstack.com/) to test the web app on Apple Devices.

---
## Functional Testing
---
#### Automated Testing

As mentioned in the [**TDD Documentation**](#tdd-documentation), automated tests were written before apps/features were coded. These automated tests include:
- Test that Urls function properly.
- Test the search bar.
- Test that objects can be created according to their models.
- Test string representation of models. 
- Test product filters on the product page and the home page(for featured critters).
- That that forms contain fields from their respective models.

13 tests currently fail due to the earlier mentioned issue with testing Rich Text fields in objects. These tests passed before adding CKEditor for the Rich Text fields. Manual tests were do to insure that these fields still performed as expected.

#### Manual Testing

For manual testing and debugging of this project Firefox Developer Tools, Chrome Developer Tools and BrowserStack were used. These test mainly consisted of visual and functional testing of the site.

In order to ensure the site works as required, I manually tested the these aspects of the deployed site before submitting the project for review(before full release):

**Header/Navbar and Footer**
- Check that all links, both when logged in and when logged out, work.
    - No errors
- Check that the cart updates when products are added or have updated quantites.
    - No errors
- Check the navbar resizes properly and that all links display properly.
    - No errors
- Check that Google Maps modal works. Salt Lake City is shown on the map.
    - No errors
        - *Note:* Due to this being a fictitious address no location pin on the map has been added. 
- Check that 'Send Message' Modal works. Email and phone number fields are pre-filled if a user is logged in. Full name is prefilled if a user has their first and last name saved in their profile. Emails are sent to the user's and business's email address. All relevant fields are included in the email.
    - *Fixed* No email address was included in the email. As the business does not save the form info in a database, the business has no way of knowing who to reply to.
    - No errors
- Check that Privacy Policy and Terms & Conditions modals work.
    - No errors
- Check social links. Links open a new tab/window.
    - No errors
- Check search functionality. User's query searches product names, descriptions and categories. User is informed if no search results are found.
    - No errors

**Home Page**
- Check that images resize correctly on all screen sizes. (Product Card Stack code)
    - No errors
        - *Note:* If a staff or admin user add a new product with a tall image, space is created on the other product cards located on the same row as the tall image. Cropping the image before uploading is recommended.
- Check that links and buttons on the product cards work.
    - No errors

**Critters/Products Page**
- Check that images resize correctly on all screen sizes. (Product Card Stack code)
    - No errors
        - *Note:* If a staff or admin user add a new product with a tall image, space is created on the other product cards located on the same row as the tall image. Cropping the image before uploading is recommended.
- Check that all filters work as intended.
    - No errors
- Check that buttons for 'Out of Stock' products are disabled.
    - No errors
- Check that buttons and links on product cards work.
    - No errors
        - *Note:* When a customer adds a product to the cart the customer is redirected to the All Products page. This is intentional. The button is meant to add products to the cart quickly without having to access product details. A future feature utilizing Ajax should allows customers to add to their cart without being redirected anywhere.

**Product Details Page**
- Check that the page resizes properly.
    - No errors
- Check that all links/buttons work. 'Available to Loan' button/badge appears when applicable.
    - No errors
- Check quantity input field. A user can not enter values higher than 20 or less than 1. The quantity is not accepted if the total quantity of the product exceeds 20. 
    - No errors
- Check that the gallery showcase appears for applicable gallery entries.
    - No errors

**Loan a Critter Page**
- Check that the page resizes properly.
    - No errors
- Check that the javascript works on all main web browsers.
    - No errors
- Check that the form is prefilled if a logged in user has saved info.
    - No errors
- Check that required info must be filled in.
    - No errors
- Check that a form can be submitted. The user is redirected to a loan 'receipt' with the info that was sent. Emails are sent to the user and business. The request is saved in the database.
    - *Fixed* The request number is not displayed in the sent emails.
    - No errors

**Critter Gallery**
- Check that the page resizes properly.
    - No errors
- Check that images display and a default image displays on errors.
    - Occasionally, if a default (error) image is displayed, it can cause another gallery entry to overlap the default image. A page refresh fixes this issue.
- Cards flip to show the backside info.
    - Users using Apple devices can intentionally not see the back side of the entires. Users are informed of this. I have been unable to have overflow on the y-axis become scrollable on Apple devices.
- Critter Type badges redirect to the appropriate product details page when clicked.
    - No errors

**Login/Logout & Register Pages**
- Check that the pages resize properly.
    - No errors
- Check that registration and email validation works.
    - No errors
- Check that login via Google and Facebook work.
    - No errors
- Check that the Forgot Password feature works.
    - No errors
- Check that users can log out. Users are redirected to the home page on logout and login.
    - No errors

**Cart & Checkout Pages**
- Check that the pages resize properly.
    - No errors
- Check that a user is informed if the cart is empty.
    - No errors
- Check that products can be removed and updated. Quantities stay within the range of 1-20. Subtotals and the Grand Total update properly.
    - No errors
- Check that user info is prefilled when logged in.
    - No errors
- Check that required fields are actually required to submit the checkout form.
    - No errors
- Check that a order can be submitted. The user is redirected to a 'receipt' with the info that was sent. Emails are sent to the user and business. The order is saved in the database.
    - No errors
- Check that webhooks are working as intended.
    - No errors

**User Profile(logged in user)**
- Check that the page resizes properly.
    - No errors
- Check that saved user info is prefilled in the form.
    - No errors
- Check that a user can update their info. This is updated in the database as well.
    - No errors
- Check that order history and loan request accordions work properly. Order numbers can be clicked to navigate to a copy of the order/request. A user can return to the profile instead of the products page when viewing the order/request this way.
    - No errors
- Check that a user's gallery entries display properly.
    - No errors
**Email & Social Account settings(logged in user)**
- Check that the pages resize properly.
    - No errors
- Check that all buttons work as intended.
    - No errors

**Add a Critter to the gallery(logged in user)**
- Check that the page resizes properly.
    - No errors
- Check that required fields must be filled to submit the entry.
    - *Fixed* Server Error 500 if a user submits with just critter name.
        -*Note:* Users can submit an entry with no image. This entry can be edited to add an image. Entries with the critter type 'Dirt' are intentionally not displayed.
- Check that added entries show up in the gallery and applicable product details and user profile pages.
    - No errors

**Edit a Critter Gallery entry(creator of entry or admin user)**
- Check that the page resizes properly.
    - No errors
- Check that an entry can be updated or removed. A confirmation window appears on deletion to prevent accidental clicks.
    - No errors

**Additional General User Functions**
- All gallery entries(on all pages) entered by a specific user can be edited by that specific user.  
    - No errors

**Add/Edit/Remove a Product(staff with permissions or admin user)**
- Check that the pages resize properly.
    - No errors
- Check that required fields must be filled to submit a product.
    - No errors
    - *Note:* Products can be created with a non-unique Sku code. This is not intentional and the fix for this is a high priority future feature. 
- Check that a negative numbers can not be used for the price.
    - *Fail* Negative numbers can be used for the price. The staff or admin should be aware of this and fix the price quickly.
- Check that new products show up in the product card stack, can be filtered and searched and the new critter type can be used in the Critter Gallery to add customer pictures of the critters.
    - No errors
- Check that featured, ready to loan, and out of stock options work as intended.
    - No errors
- Check that a product can be updated or removed. A confirmation window appears on deletion to prevent accidental clicks.
    - *Fail* - If a product is removed that is stored in a user's web browser cookies, the error of 'The requested resource was not found on this server' appears for the user. The user can not access the site while those cookies are removed.

**Additional Staff and Admin Functions**
- Check that admins can edit all products and all gallery entries anywhere on the site.
    - No errors

**Django Admin Site Administration(staff with permissions & admin users)**
- Check that models and database entries are easy to find, read and edit if nessecary. No spelling mistakes.
    - No errors
- Check that adding or removing categories or subcatagories also add/remove the categories as searchable filters on the Critters/Products page.
    - No errors

#### User Testing

This project has been reviewed/tested by an experienced web developer. A mentor provided by Code Institute during my studies.

This project has been reviewed/tested by friends and family.

A Full Usability test was done when all features were in place. This was done to identify possible bugs as well as ensure that the application is easy-to-use.
- Intended Test Audience - A new user interested in purchasing a pet.

**Feedback From User Test**

After this test the following feedback was given:


**Errors After User Test**
