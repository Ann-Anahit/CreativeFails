# Creative Fails Website - Testing

![Creative Fails](documentation/images/am-i-responsive.png)

Visit the deployed website here → [Creative Fails](https://creativefails-b08c6c63e317.herokuapp.com/)

## Content

- [Testing User Stories](#testing-user-stories)
- [Manual Testing](#manual-testing)
  - [Browser Testing](#browser-testing)
- [Automated Testing](#automated-testing)
  - [HTML Validator](#html-validator)
  - [CSS Validator](#css-validator)
  - [JavaScript Validator](#javascript-validator)
  - [Python Validation](#python-validation)
  - [Lighthouse](#lighthouse)

## Testing User Stories

- First time visitors

| Expectation                                              | Result                                                                                                                                        |
| :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| I want to share my experiences and read other about other projects.                                    |  The user gets to informations really quickly. |
|I want to Receive and Give Feedback.                                        | The User can only read the other posts, he can't give feedback yet.
| I want to Signe up and Sign in. | The User can sign up and sign in easily.                                                  |
| I want responsiveness from my website.                   | The website has full responsiveness.                                                                                                          |
|I want to Connect with the Community.                                        | The User can comment and like the other posts 
<br>
- Returning Visitors

| Expectation                                          | Result                                                                                  |
| :--------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| I want to edit my posts | The user can edit and delete the own posts.
| I want to Explore New art Projects.                | The user can see the posts and read them.              |
| I want to write new articles.                  | The user can write new articles.|


[Back to top](#content)

## Manual Testing

| Feature                                                                     | Expectation                                                                   | Action                                                        | Result |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------- | ------ |
| Logo                                                                   | If you click on the Logo, the posts is supposed to open     | Click the arrows                                              | Passed |
| Navbar buttons                                                              | Take the user to the respective section                                       | Click buttons                                                 | Passed |
| Write article                                                           | Go to the write article page. If user not signed in, ask to sign in                 | Click on the button                                           | Passed |
| Top bar                                                                     | Change the menu when a user signs in/out                                      | Sign in/out                                                   | Passed |
| Write article Page                                                               | You can write an  article and the date and time of your post will be printed also the author                                                 |write article and submit                                         | Passed |
| Logout                                                                      | Signs out of the account                                                      | Click the button                                              | Passed |
| Account creation                                                            | Create account                                                                | Fill out the form                                             | Passed |
| User knows they're signed in                                                | Display user name on the screen after sign in                                 | Look at the screen                                            | Passed |
| Empty, false or wrong values                                                | Forms don't allow empty or false values                                       | Try to submit a form with empty inputs, wrong characters, etc | Passed |
| Footer links open externally                                                | Footer links open externally                                                  | Click on the links in the footer                              | Passed |
| Success message                                                             | User get a sucess message after submit any form (login, signup, booking, etc) | Submit a form                                                 | Passed |
| Admin panel                                                                 | Admin can manage and edit informations, images and delete things              | Edit informations, update images, delete things               | Passed |

<br>

### Browser Testing

I tested the website in different browsers, both on computer and mobile. iOS tests were made on [Appetize.io](https://appetize.io/).

| Browser         | Result                     |
| :-------------- | :------------------------- |
| Google Chrome   | The website is responsive. |
| Microsoft Edge  | The website is responsive. |
| Mozilla Firefox | The website is responsive. |
| Opera           | The website is responsive. |

[Back to top](#content)

## Automated Testing

### HTML Validator

[W3C](https://validator.w3.org/) checked the HTML of the website and it passed the validation. An error message shows up.
![HTML Validation](documentation/images/html_validator.png)

### CSS Validator

The CSS was validated by [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) and passed the test. To see the full result, click on the name below.

- [CSS](documentation/pdf/css_validator.pdf)


### Python Validation

[PEP8](https://pep8ci.herokuapp.com/) found some issues and I fixed them all.

### Lighthouse

I used [PageSpeed Insights](https://pagespeed.web.dev/) to test the full performance of the website.<br><br>

- Mobile

[Home](documentation/images/home_m.png)<br>

[Posts](documentation/images/posts_m.png)<br>

[Sign in](documentation/images/signin_m.png)<br>

[Registration](documentation/images/registration_m.png)<br>

[Write article](documentation/images/write_article_m.png)<br><br>

- Desktop

[Home](documentation/images/home_d.png)<br>

[Posts](documentation/images/posts_d.png)<br>

[Sign in](documentation/images/signin_d.png)<br>

[Registration](documentation/images/registration_d.png)<br>

[Write article](documentation/images/write_article_d.png)<br><br>

[Back to top](#content)