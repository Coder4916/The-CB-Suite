# **The CB Suite**

![The CB Suite image]()

## **Table of Contents**

- [**The CB Suite**](#the-cb-suite)
  - [**Table of Contents**](#table-of-contents)
  - [**Introduction**](#introduction)
  - [**UX Development**](#ux-development)
    - [**1. Strategy Plane**](#1-strategy-plane)
    - [**User Stories**](#user-stories)
      - [**First Time User Goals**](#first-time-user-goals)
      - [**Returning User Goals**](#returning-user-goals)
      - [**Frequent User Goal**](#frequent-user-goal)
    - [**Research**](#research)
    - [**Project Goals**](#project-goals)
    - [**User Goals**](#user-goals)
    - [**Other Considerations**](#other-considerations)
    - [**Strategy Table**](#strategy-table)
    - [2. **Scope Plane**](#2-scope-plane)
    - [3. **Structure Plane**](#3-structure-plane)
    - [4. **Skeleton Plane**](#4-skeleton-plane)
    - [5. **Surface Plane**](#5-surface-plane)
      - [**Color Scheme**](#color-scheme)
      - [**Typography**](#typography)
      - [**Imagery**](#imagery)
  - [**Features**](#features)
    - [**Current Features**](#current-features)
      - [1. **Header**](#1-header)
      - [2. **About me page**](#2-about-me-page)
      - [3. **Coaching Page**](#3-coaching-page)
      - [4. **Contact Page**](#4-contact-page)
      - [5. **Footer**](#5-footer)
      - [6. **Learn more Page**](#6-learn-more-page)
    - [**Features to be added in the future**](#features-to-be-added-in-the-future)
  - [**Technologies Used**](#technologies-used)
    - [**Main Languages used**](#main-languages-used)
    - [**Additional Languages Used**](#additional-languages-used)
    - [**Frameworks, Libraries and Programs Used**](#frameworks-libraries-and-programs-used)
  - [**Issues and Bugs**](#issues-and-bugs)
  - [**Deployment**](#deployment)
    - [**Deployment to GitHub Pages**](#deployment-to-github-pages)
    - [**Forking the Github Repository**](#forking-the-github-repository)
    - [**Making a Local Clone**](#making-a-local-clone)
  - [**Testing**](#testing)
    - [**User Stories Testing**](#user-stories-testing)
      - [**First Time User Goal**](#first-time-user-goal)
      - [**Returning User Goal**](#returning-user-goal)
      - [**Frequent Visitor Goal**](#frequent-visitor-goal)
  - [**Manual Testing**](#manual-testing)
    - [**Responsiveness**](#responsiveness)
    - [**Links Testing**](#links-testing)
    - [**Forms Testing**](#forms-testing)
  - [**Autoprefixer CSS**](#autoprefixer-css)
  - [**W3C Validator Testing**](#w3c-validator-testing)
  - [**Lighthouse Testing**](#lighthouse-testing)
  - [**Further Testing**](#further-testing)
  - [**Credits**](#credits)
    - [**Code**](#code)
    - [**Images**](#images)
    - [**Additional contents**](#additional-contents)
  - [**Acknowledgements**](#acknowledgements)

## **Introduction**

The-CB-Suite is a Games Review website designed to give gamers/critics the opportunity to leave reviews based on a selection of games in the current market which are hosted on a variety of consoles/platforms. 

The site will also provide a service to the user, helping them to gain a better understanding of the gaming market, assisting a user when making a decision based on game purchases.

There will also be a blog element to the website, where users will have access to external resources and further information to bolster the sites appeal.

The main requirement of this Code Institute project was to build a responsive and interactive back-end site based around a simple CRUD concept, with the primary objective of making the website simple and easy to use. All information and reviews will be stored in a simple Relational Database.

## **UX Development**

### **1. Strategy Plane**

### **User Stories**

#### **First Time User Goals**

1. As a first-time user, I want to be able to navigate the website with ease.
2. As a first-time user, I want to know what type of games are listed on the site quickly and easily.
3. As a first-time user, I want to be able to review the site's games quickly and easily 
4. As a first-time user, I want to be able to see my review on the site, and be able to edit if needed.
5. As a first-time user, I want to be able to see other user reviews on the site.
6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

#### **Returning User Goals**
  
1. As a returning user, I want to be able to navigate the website with ease.
2. As a returning  user, I want to know what type of games are listed on the site quickly and easily.
3. As a returning  user, I want to be able to review the site's latest games quickly and easily 
4. As a returning  user, I want to be able to see my current and old reviews on the site, and be able to edit if needed.
5. As a returning user, I want to be able to see other user reviews on the site.
6. As a returning  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

#### **Frequent User Goal**
  
1. As a frequent user, I want to be able to navigate the website with ease.
2. As a frequent user I want easy access to the site's games and reviews, as well as any additional information.
3. As a frequent user, I want to be able to see other user reviews on the site.
4. As a frequent  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

### **Research**

- Online research

I Researched other gaming review websites available online such as [metacritic](https://www.metacritic.com/) and [Den of Geek](https://www.denofgeek.com/games/reviews/). This helped me to understand what is feasible, the aesthetics of other site's in this sector and how they provide a service and user accessibilty.

### **Project Goals**

The project goal is to provide an interactive back end website, based on a simple CRUD design which will allow a user to create, read, update/edit and delete game reviews on the site. It should be accessible, easy to navigate, and the service provided, clear and unambiguous.

### **User Goals**

The target audience for this website is primarily gamers and game critics, however, the site should be easily accessible for all, providing clear intent and site content.

Specifically:

- People who might be looking for information on the latest games on the market.
- Anyone interested in gaming.
- Anybody looking to make a game purchase and may need guidance.
- The site can also provide a platform for game critics to indirectly communicate with game developers.

User goals when accessing this website include gaining information about the site's games and allow gamers to have the ability to critic the games on offer in the current market. 

[Back to top](#the-cb-suite)

### **Other Considerations**

The CB Suite is a Customer-To-Customer (C2C) product, where people can share reviews and ideas, and discuss the games in the current market, which has considerations as below:

- Calming and friendly presence
- Minimal, to the point content
- Simple design/aesthetics
- Adds a social element

### **Strategy Table**

Based on the research, goals, and the considerations above, I considered what should be implemented on the website. I mapped the ideas based on their importance based on user needs and viability (given limited time and resources), to determine which ideas were going to be included and which were not:

| Features/Ideas             | Importance | Viability |
| -------------------------- |:----------:| ---------:|
|  A. Games page             |      5     |     5     |
|  B. Reviews page           |      5     |     5     |
|  C. Add review page        |      5     |     5     |
|  D. Edit review page       |      5     |     5     |
|  E. Delete review function |      5     |     5     |
|  F. Username function      |      4     |     3     |
|  G. Blog page              |      3     |     3     |
|  H. Social Media links     |      2     |     3     |

### 2. **Scope Plane**

Based on the mapping in Strategy Plane, I decided to include these contents below in the website:

- Games page; displays several games in the current gaming market, allowing a user to leave a review for each.
- Reviews page; will display any reviews to the user, and will also include an edit and delete review function.
- Add review page; accessed via game cards on the games page, and will give the user the ability to create and read reviews based on any game on the site.
- Edit review page; accessible once a review has been created on the site.
- Username function; will give a level of security to the site. This will prevent editing/deleting of other reviews, as well as protecting personal reviews.
- Blog page; will add to the site's usability and appeal, providing further gaming info etc.
- Social media links; gives the user the ability to contact the owner of the site, and gain further info on the site itself, such as any future updates etc.

### 3. **Structure Plane**

The website's front-end will consist of a simple structure with a user friendly navigation element to reach each html page. Each page will also share a consistant base template utilising the web framework Flask. The content specific to each page/child template will be controlled using Flask specific extend/block content tags. Layout on child templates will also be controlled using Flask loop tags. A POSTGRES Database will contain game and review content, which the site will also display via Flask template loops.

[Back to top](#the-cb-suite)

### 4. **Skeleton Plane**

The initial layout and interface of the Website was created using Balsamiq Wireframes. The design/layout and feel of the site was created with UI in mind, which allows immediate interaction in first-time use, and meets the needs of the intended audience.

![Balsamiq-wireframes Blog/Home page](/my_suite/static/img/balsamiq-blog.png)

![Balsamiq-wireframes](/my_suite/static/img/balsamiq-game.png)

![Balsamiq-wireframes](/my_suite/static/img/balsamiq-review.png)

### 5. **Surface Plane**

#### **Color Scheme**

The aesthetics used are primarily derived from the [Clean Blog](https://startbootstrap.com/theme/clean-blog) Theme provided by [Start Bootstrap](https://startbootstrap.com/).

#### **Typography**

The fonts I used for the website were all included within the [Start Bootstrap](https://startbootstrap.com/), [Clean Blog](https://startbootstrap.com/theme/clean-blog) package, which includes Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif for all titles and navigation bar text, and Lora, Times New Roman and serif for body text.

#### **Imagery**

I have used an image by [Athena](https://www.pexels.com/@athena/) of [computer gadets on a table](https://www.pexels.com/photo/set-of-modern-gadgets-on-table-5861322/) for the main image. A fallback color is included in the [Start Bootstrap](https://startbootstrap.com/) package, which will be added to the body if the main image doesn't load.

[Back to top](#the-cb-suite)

## **Features**

### **Current Features**

#### 1. **Header**

- The header consists of a [main image](https://www.pexels.com/photo/set-of-modern-gadgets-on-table-5861322/), title and navigation bar. The nav-bar includes three nav-links on the right hand side that link to each site page. The header occupies 100% width of the site.

- The navigation bar is fully responsive on all device sizes. On desktop view, the user will be able to see all nav-links, while on a smaller device, these collapse to a [Bootstrap Hamburger](https://getbootstrap.com/docs/5.3/components/navbar/#toggler) menu.

- The Nav-links have a subtle hover state when the user hovers over each link, and include a [Bootstrap](https://getbootstrap.com/docs/5.3/components/list-group/#active-items) .active class to show which page the user is on.

#### 2. **Home Page**

- The Home Page includes a title and sub-title to introduce the user, and a blog element to complement the site's game theme. The template is taken from a base.html file within the CB-Suite project package, and [Routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) is used to render the each site page in the browser.

#### 3. **Games Page**

- The Games Page contains all games that the user will have the option to review, each set within a [Bootstrap card](https://getbootstrap.com/docs/5.3/components/card/#about) and housed within a [Bootstrap Carousel](https://getbootstrap.com/docs/5.3/components/carousel/#how-it-works). Information about each game is stored in a POSTGRES Database and displayed using [Flask](https://flask.palletsprojects.com/en/3.0.x/). The page template will taken from a base.html file within the project file package, and [routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) is used to render the page in the browser.

#### 4. **Reviews Page**

The Reviews Page will display any reviews added to the site by a user. Reviews will be stored in a table in a POSTGRES database, my_suite, and displayed to the page using [Flask](https://flask.palletsprojects.com/en/3.0.x/). The page template will also be taken from a base.html file within the CB-Suite file package, and [routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) will be used to render the template in the browser.

#### 5. **Footer**

The Footer provides social media links that all open in new tabs. The Footer also contains a copyright image with creation date using [Javascript](https://www.w3schools.com/jsref/jsref_getfullyear.asp) which will automatically update accordingly.

### **Features to be added in the future**

These features will be added where possible during further development phases:

- Adding CRUD function to the blog element, where users can leave their own content on the page for others to digest/share.

- Increasing the number of games on the site, allowing users to add their own too.

- A search feature to divide the games into groups/classes using their card info i.e. genre etc, if somebody was interested in something in particular.

- As the site grows, a generic search engine within the games/review pages navbar would be helpful to increase accessibilty.

- A function to take the average of the total number of star ratings and output an overall game review score, which could be added to the game cards.

[Back to top](#the-cb-suite)

## **Technologies Used**

### **Main Languages used**

[HTML5](https://en.wikipedia.org/wiki/HTML5) was used to create the front-end, base template of the website. A [Start Bootstrap](https://startbootstrap.com/) design theme was used for this.

[CSS3](https://en.wikipedia.org/wiki/CSS) was used to design the layout and aesthetics of the website. Again, most of the CSS was included in the [Start Bootstrap](https://startbootstrap.com/) theme file package.

[Python](https://www.python.org/) was used to create the back-end Relational Database, declaring tables used to store game/review data using Python database Models. [Routing](https://www.tutorialspoint.com/python_network_programming/python_routing.htm) was used to render each page's content based around route functions, in order to manage the the structure of the website. Python also provided an __init__ and environment variable elements to the site.

### **Additional Languages Used**

[Javascript](https://en.wikipedia.org/wiki/JavaScript) controls the function of the navigation bar, and scripts are added to control [date output](https://www.w3schools.com/jsref/jsref_getfullyear.asp) in the footer of each page

### **Frameworks, Libraries and Programs Used**

1. [Start Bootstrap](https://startbootstrap.com/) provided the [Clean Blog](https://startbootstrap.com/theme/clean-blog) template for each site page.

2. [Bootstrap 5.3](https://getbootstrap.com/) was used to assist with the responsiveness and styling of the website, as well as adding components, such as a [card](https://getbootstrap.com/docs/5.3/components/card/) for each game, and [accordion](https://getbootstrap.com/docs/5.3/components/accordion/#how-it-works) for reviews.

3. [Flask](https://flask.palletsprojects.com/en/3.0.x/) reduced repitition when building the html/css site framework, and allowed back-end material to be injected into the front-end design.

4. [SQLAlchemy](https://www.sqlalchemy.org/) was utilised to create each table that made up the site's back-end database. SQL commands could be used to ALTER, ADD and DROP parts of the database as required, when used in conjunction with Python Models.

5. [Google Fonts](https://fonts.google.com/) provided Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif fonts for the header and titles and Lora, Times New Roman and serif fonts for the body of the site.

6. [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.

7. [Gitpod](https://gitpod.io/workspaces) IDE was used for creating the website and back end database in the terminal, and using the built in terminal to push the site to GitHub for version control.

8. [GitHub](https://github.com/) was used to store the project's code after being pushed from [Gitpod](https://gitpod.io/workspaces).

9. [Balsamiq Wireframes](https://balsamiq.com/wireframes/) were used to design the initial general layout and feel of the website.

10. [Autoprefixer CSS](https://autoprefixer.github.io/) was used to add vendor prefixes to the CSS rules, to ensure that they work across all browsers.

11. [Am I Responsive](https://ui.dev/amiresponsive?url=https://8002-coder4916-ci-milestone-ylxy4w9e48.us2.codeanyapp.com/index.html) was used to preview the website across a variety of popular devices.

12. [Squoosh](https://squoosh.app/) was used to reduce the file size of the images, and change from .jpg to .AVIF. This helped to improve the overall performance of the website.

13. [Heroku](https://www.heroku.com/home) was used to deploy the project

[Back to top](#the-cb-suite)

## **Issues and Bugs**

- Issue: During the initial stages of the project I encountered a server error when trying to test the site.

Solution - After some tutoring, it was noticed that I had mistakenly placed my env.py file in my_suite directory instead of the root dir.

- Issue: I encountered an exe. issue when trying to test my site:

Solution - After researching what may have been the problem, making use of the information in the Slack channels, I found that my requirements.txt needed updating and syncing with my project.

- Issue: When trying to begin work on my project I found that Gitpod would not allow connection to my_database via the terminal. Tried several times to connect, and double checked project files for any obvious problems.

Solution - Slack channel suggested restarting Gitpod, but this did not fix the problem. I had to open a brand new workspace, and transfer everything over from Github. The requirements.txt and env.py files had to be recreated/updated. All imports needed re-initialisng. my_database also had to be built from scratch.

- Issue: Wrestled with the task of storing url images in my_database, and then injecting them into my project. I had first tried to add in the images and data from a JSON file, but wanted to find a much simpler solution.

Solution - I tried adding the images as urls as suggested by a tutor, and also as files to the database, but couldn't output the images from the database. After some more research (BLOBS, BYTEA etc) and getting some help from my mentor Koko, I added the urls as .Text data in my form and Model.py file. This solved the problem. I could then display the game images correctly.

- Issue: Tried to work out how to make the Bootstrap Accordion open one review at a time, rather than all, when clicking on the displayed dropdown buttons.

Solution - After a bit of research online, I found that loop.index could be utilised on the accordion buttons, giving more control over opening and closing each review.

- Issue: The list of site games would not show correctly in the select/dropdown box on my edit_review form when editing a review.

Solution - After re-writing my html code to make sure it was ok, as well as going back over the CI tutorials, I eventually found that I'd missed some code from the routes.py file, and hadn't declared the games variable properly when rendering the edit_review page. Once added, the edit_review form worked correctly.

- Issue: Creating the star rating in edit_review. Ratings were stored in the database as opposites, 1 star was 5, 5 was 1 and so on.

Solution - After some research online, I found that the values had to be written the opposite way round to reverse this. Once done, this fixed the issue.

## **Deployment**

The Website was developed using [Gitpod](https://gitpod.io/workspaces) as the IDE, committed to Git as a local repository and finally pushed/stored to [GitHub](https://github.com/). The website was then deployed to [Heroku](https://www.heroku.com/home) using the following steps:

### **Preparing my_database for deployment

1. Navigate to ElephantSQL.com and click “Log in”
2. Select “Sign in with GitHub”
3. Authorise ElephantSQL with a selected GitHub account
4. Create a new team form
5. Click “Create New Instance”
6. Select “Select Region”
7. Then click “Review”
8. Check your details are correct and then click “Create instance”
9. Return to the ElephantSQL dashboard and click on the database instance name for this project
10. In the URL section, clicking the copy icon will copy the database URL to your clipboard

### **Project deployment to Heroku**

1. Generate a requirements.txt file
2. Inside the root directory of your project, create a Procfile
3. Inside the file, add the following command: python3 run.py
4. Open your __init__.py file
5. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
6. To ensure that SQLAlchemy can read an external database, its URL should start with “postgresql://”, changes should not be made to this in the environment variable. Instead, make an addition to the else statement from the previous step to adjust the DATABASE_URL in case it starts with postgres://:
7. Save all files and then add, commit and push changes to GitHub
8. Log into Heroku.com and click “New” and then “Create a new app”
9. Choose a unique name for the app, select a region and click “Create app”
10. Go to the Settings tab of your new app
11. Click Reveal Config Vars
12. Return to your ElephantSQL tab and copy your database URL
13. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
14. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var.
15. Navigate to the “Deploy” tab of your app
16. In the Deployment method section, select “Connect to GitHub”

[Back to top](#the-cb-suite)

## **Testing**

### **User Stories Testing**

#### **First Time User Goal**

1. As a first-time user, I want to be able to navigate the website with ease.

- The navigation bar is clearly defined, with a subtle hover function when the user moves the cursor over the menu items.
- The title in the navbar leads the user back to the Home page increasing accessibility.
- Links to further information/social media can be easily accessed via the footer.

![Navigation Bar Screenshot]()

2. As a first-time user, I want to know what type of games are listed on the site as required.

- Visitors to the site are greeted with a Home page that contains an introductory game blog; and navbar allows the user access straight to the games page. All games are displayed in a card, with a button to review for each game. A Bootstrap Carousel was initially used both in the design phase, and in initial development, however this was removed as it was slowing access to all games. This was considered to have added some frustration to UX when displaying/reviewing the site's games.

![Game Page Screenshot]()

3. As a first-time user, I want to be able to review the site's games quickly and easily 

- A user can navigate easily to the games page via the navigation bar. All games are displayed in a card, with a button to review for each game.

![An example of a game card]()

4. As a first-time user, I want to be able to see my review on the site, and be able to edit if needed.

- A reviews page holds all submitted reviews, and displays all reviews in a Bootstrap Accordion. The page is easily accessed via the navigation bar. Each review has an editing option available.

![Reviews page and reviews accordion]()

5. As a first-time user, I want to be able to see other user reviews on the site.

- Other user reviews can be accessed via the reviews page, in the reviews accordion.

![Reviews accordion; unopened]()

6. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

- Social media links are stored in the footer.

![Links]()

#### **Returning User Goal**

1. As a returning user, I want to know if there's an FAQs page for any questions I may have.

- The FAQ section on the Contact page provides the answers to some of the questions that the user might have.
- The contact form also functions as one of the options for the user to ask questions.

2. As a returning user, I want access to different ways of contacting the owner further if required.

- The contact form functions as the main means of communication for the user to contact the Coach.
- The Coach's phone number is provided in the Get In Touch section.
- The Coach's email address is also provided in the Get In Touch section if the user prefers not to use the contact Form.
- A social media link can also can be used as an option to contact the Coach via LinkedIn. The social media link is located in the Footer.

![Returning User Screenshot](/assets/images/returning-user-stories.png)

3. As a returning user I want to easily access further information as required.

- For any users that want to know more about Life Coaching, there are further external links to coaching material contained in the learn-more page via a learn more link in each page's footer.

![Useful Links Screenshot](/assets/images/useful-links.png)

#### **Frequent Visitor Goal**

1. As a frequent user, I want to know if there will be chance to give feedback on the website.

- A link to a feedback form is available in the footer.

![Feedback Link Screenshot](/assets/images/feedback.png)

2. As a frequent user I want to access information easily.

- Access to further information is available via a learn more link in each page footer. 
- The Contact Form can also be used to contact the Coach to find out more.

3. As a frequent user I want to be able to contact the owner easily.

- The Coach can be contacted via a contact form, or by phone, email, or via LinkedIn. This gives the user options, depending on what's preferable for them.

![Frequent User Screenshot](/assets/images/contact-screenshot.png)

## **Manual Testing**

### **Responsiveness**

I used web developer tools extensively throughout the project to update and correct code, adjust website aesthetics, and check/improve and confirm responsiveness accross all devices, using a Bootstrap 'Mobile First' approach.

Below are some examples of sections that I have tested and checked for full responsiveness on all devices. These images show the sections at each [Breakpoint](https://getbootstrap.com/docs/5.3/layout/breakpoints/#core-concepts).

![Header](/assets/images/header-responsive.png)

![Form](/assets/images/form-responsive.png)

![Background Section](/assets/images/background-responsive.png)

![Footer](/assets/images/footer-responsive.png)

### **Links Testing**

Once deployed, the website links were tested to ensure that:

All navigation external/internal links are working correctly.
The social media button and the learn more page links are working and opening in a new tab. All links were working and set to a relative filepath.
Hovering and Active states are working.

### **Forms Testing**

The Think-In-Space Form was also tested to make sure that
the required fields are working, and the form sends the input data correctly.

![Input Data sent to CI mock server](/assets/images/ci-confirm-form.png)

## **Autoprefixer CSS**

Autoprefixer CSS was used to add CSS vendor prefixes to the CSS rules after the developing process was done and the CSS was validated, to ensure that they work across all browsers.

## **W3C Validator Testing**

The [W3C Markup Validator](https://validator.w3.org/) and W3C CSS Validator Services were used to validate the website to ensure there were no syntax errors in the project.

The images below are snapshots of each page of the website after the code has been put through the Validator.

![W3C Markup Validator](/assets/images/index.html-checked.png)

![W3C Markup Validator](/assets/images/coaching.html-checked.png)

![W3C Markup Validator](/assets/images/contact.html-checked.png)

![W3C Markup Validator](/assets/images/style.css-checked.png)

## **Lighthouse Testing**

Chrome Lighthouse testing was used to check the performance, accessibility, best practices, and SEO. After applying some changes to make the performance faster, including resizing all of the images, compressing image/changing the file size and adding a rel=noopener to all external links, the results below were achieved:

- Desktop:

![Think-In-Space Lighthouse testing](/assets/images/lighthouse-testing.png)

- Mobile:

![Think-In-Space Lighthouse testing](/assets/images/lighthouse-testing-mobile.png)

## **Further Testing**

The Website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox. Microsoft Edge required extensions to run the site images correctly.

The website was viewed on a variety of devices such as:

Windows Laptop
Mobile: Samsung Galaxy S12
Web developer tools devices

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## **Credits**

### **Code**

1. [Bootstrap 5.3](https://getbootstrap.com/): Bootstrap was used extensively throughout the project, including the following components:

- [A collapsible and expandable navigation bar](https://getbootstrap.com/docs/5.3/components/navbar/#toggler)
- [A Carousel](https://getbootstrap.com/docs/5.3/components/carousel/)
- [A Bootstrap grid system](https://getbootstrap.com/docs/5.3/layout/grid/#example)

2. [stackoverflow](https://stackoverflow.com/questions/21254889/how-to-remove-the-gutter-spacing-between-columns-in-bootstrap): Was used to find solutions to problems/issues when building the website, for example, finding out more information about an update when removing Bootstrap padding in a grid system.

3. [w3Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp): Was used to get assitance with creating the website, for example when creating the 'back to top' button using pure CSS.

4. [Autoprefixer CSS](https://autoprefixer.github.io/):
Was used to add different vendor prefixer to CSS.

### **Images**

The Coach created the Website Logo using [Hatchful by Shopify](https://www.shopify.com/tools/logo-maker?syclid=ckaok3ausvis73ecc1gg&utm_campaign=Hatchful&utm_content=Onboarding_1&utm_medium=email&utm_source=mozart).

I used the following image, sourced from [Pexels](https://www.pexels.com/) for the background of each site page:

[Close up photo of pebbles image; by Ave Calvar Martinez](https://www.pexels.com/photo/close-up-photo-of-pebbles-3010168/)

The following images Elwyn and I sourced from [Burst](https://www.shopify.com/stock-photos/photos/senior-teaching-young-man?c=teacher) and [Pexels](https://www.pexels.com/) to populate each page section:

[Senior teaching young man; by Shopify](https://www.shopify.com/stock-photos/photos/senior-teaching-young-man?c=teacher)

[Hiker climbing mountains; by Brodie](https://www.shopify.com/stock-photos/photos/hiker-climbing-mountains?c=landscape)

[Question Marks; by Leeloo TheFirst](https://www.pexels.com/photo/question-marks-on-paper-crafts-5428836/)

All other photos/images used were sourced from Elwyn's photo gallery. They are images of local available Blue/Green space, which Elwyn is planning on using for his clientele.

### **Additional contents**

All external links/additional content was sourced via YouTube and Google Books.

## **Acknowledgements**

- My mentor, Oluwaseun Owonikoko, for her guidance and helpful feedback on all aspects of the Website.
- The Code Institute tutors who helped me with some of the issues I had when building the site.
- My wife Beth for her constant support throughout, and for proof reading and testing my site material.

[Back to top](#the-cb-suite)
