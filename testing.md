
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
- [ ] A user can navigate to diffrent pages via the nav bar.    

---
## Known Issues
---

Most errors throughout the project have been simple syntax errors that took very little time to locate and correct. Some of the larger issues/bugs can be found below.

##### Resolved

##### Unresolved

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