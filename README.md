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
4. As a first-time user, I want to be able to see other user reviews on the site.
5. As a first-time user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

#### **Returning User Goals**
  
1. As a returning user, I want to be able to navigate the website with ease.
2. As a returning  user, I want to know what type of games are listed on the site quickly and easily.
3. As a returning  user, I want to be able to review the site's latest games quickly and easily 
4. As a returning  user, I want to be able to see my current and old reviews on the site, and be able to edit if needed.
4. As a returning user, I want to be able to see other user reviews on the site.
5. As a returning  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

#### **Frequent User Goal**
  
1. As a frequent user, I want to be able to navigate the website with ease.
2. As a frequent user I want easy access to the site's games and reviews, as well as any additional information.
3. As a frequent user, I want to be able to see other user reviews on the site.
3. As a frequent  user, I want to be able to locate the site's social media links to see their followings and find any future updates to the site.

### **Research**

- Online research

I Researched other gaming review websites available online such as [metacritic](https://www.metacritic.com/) and [Den of Geek](https://www.denofgeek.com/games/reviews/). This helped me to understand what is feasible, the aesthetics of other site's in this sector and how they provide a service and user accessibilty.

### **Project Goals**

The project goal is to provide an interactive back end website, based on a simple CRUD design which will allow a user to create, read, update/edit and delete game reviews on the site. It should be accessible, easy to navigate, and the service provided, clear and unambiguous.

### **User Goals**

The target audience for this website is primarily gamers and game critics, however, the site should be easily accessible for all, providing clear intent and site content.

Specifically:

- People who require information on the latest games on the market.
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
|  D. Username function      |      4     |     5     |
|  E. Blog page              |      3     |     4     |
|  E. Social Media links     |      3     |     5     |


[Back to top](#think-in-space)

### 2. **Scope Plane**

Based on the mapping in Strategy Plane, I decided to include these contents below in the website:

- Games page; introduces the user to the site, and will display the games in a carousel.
- Reviews page; will display the completed reviews to the user, and will also include an edit and delete review function.
- Add review page; accessed via the game page, and will give the user the ability to create and read reviews based on any game on the site.
- Username function; will give a level of security to the site. This will prevent tampering of other reviews, as well as protecting personal reviews.
- Blog page; will add to the site's usability, providing further gaming info etc.
- Social media links; gives the user the ability to contact the owner of the site, and gain further info on the site itself, such as any future updates etc.

### 3. **Structure Plane**

The website's front-end will have a simple structure with a user friendly navigation element to reach each html page. Each page will also utilise template inheritance, sharing a consistant template utilising the web framework Flask. The content specific to each page/child template will be controlled using Flask specific block tags. Layout on child templates will also be controlled using Flask for loop tags.

[Back to top](#the-cb-suite)

### 4. **Skeleton Plane**

The initial layout and interface of the Website was created using Balsamiq Wireframes. The design/layout and feel of the site was created with UI in mind, which allows immediate interaction in first-time use, and meets the needs of the intended audience.

![Balsamiq-wireframes]()

### 5. **Surface Plane**

#### **Color Scheme**

The colors used are primarily derived from the [Clean Blog](https://startbootstrap.com/theme/clean-blog) Theme provided by [Start Bootstrap](https://startbootstrap.com/).

#### **Typography**

The fonts I used for the website were sourced from [Start Bootstrap]().

#### **Imagery**

I have utilised a mix of free to use images sourced online, and the Coach's personal pictures of local green space/blue space etc. I have used a fallback color if the main body image doesn't load.

[Back to top](#think-in-space)

## **Features**

### **Current Features**

#### 1. **Header**

- The header consists of a website logo which sits on the left hand side of the page, navigation bar and title. The nav-bar includes three nav-links on the right hand side that link to each site page. The header occupies 100% width of the site.

- The navigation bar is fully responsive on all device sizes. On desktop view, the user can see all nav-links, while on a smaller device, these collapse to a [Bootstrap Hamburger](https://getbootstrap.com/docs/5.3/components/navbar/#toggler) menu.

- The main logo is not displayed on a small device to create more space for content and features. This is done using a CSS Media Query.

- The Nav-links have a subtle hover state when the user hovers over each link, and includes a [Bootstrap](https://getbootstrap.com/docs/5.3/components/list-group/#active-items) .active class to show which page the user is on.

#### 2. **About me page**

- The About me page includes three sections which give a brief introduction of the Coach;

- The Coach, Background and Tried and Tested sections include information about the Coach's life experience and qualifications, as well as how the Coach has already helped others.

#### 3. **Coaching Page**

- The Coaching Page includes three sections which inform the user about Life Coaching;

- The Why Life Coaching, What to Expect, and Testimonials sections include information and reviews based on what would normally be involved if a user decides to book a coaching session, and help them decide whether this coaching/journey is right for them.

- A Bootstrap Carousel has been added to display testimonials/reviews and is fully responsive on all devices.

#### 4. **Contact Page**

- The Contact Page is divided into three sections, which allows the user to contact the Coach or book a session;

- The Get in Touch and FAQs sections contain a contact form, map and answers to frequently asked questions to assist the user.

- All sections are 75% width of the screen size and fully responsive on different sized devices.

#### 5. **Footer**

The Footer uses the same color as the Navigational Menu and provides social media links that all open in new tabs. The Footer also contains the site logo which takes the user back to the About Me Page.

#### 6. **Learn more Page**

A Learn More link was added to the Footer, which gives the user access to a list of educational links to external sites. This give the user the opportunity to find out more about Life Coaching and associated subjects.

### **Features to be added in the future**

These features will be added where possible during further development phases:

- A time/date picker to book available coaching sessions automatically. This is likely to be created/added to the site once Elwyn can establish set operating times for his business in the future.
  
- A Legitimate form url address where the user's details can be stored and utilised by the Coach.

- An option to have the website translated to Welsh if the user prefers.

- More FAQs and Reviews as the business progresses.

[Back to top](#think-in-space)

## **Technologies Used**

### **Main Languages used**

[HTML5](https://en.wikipedia.org/wiki/HTML5) was used to create the front end framework of the website.

[CSS3](https://en.wikipedia.org/wiki/CSS) was used to design the layout and aesthetics of the website, including using effective typography and complimentary colors that would improve UX.

### **Additional Languages Used**

[Javascript](https://en.wikipedia.org/wiki/JavaScript) was used to implement functions that allowed the Hamburger menu in Navbar, and a carousel to display several testimonials. Both were applied for a better UX.

### **Frameworks, Libraries and Programs Used**

1. [Bootstrap 5.3](https://getbootstrap.com/) was used to assist with the responsiveness and styling of the website, as well as adding components.

2. [Google Fonts](https://fonts.google.com/) was used to import the “Roboto” and “Lexend” fonts into the html file, and were used on all parts of the site.

3. [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.

4. [Codeanywhere](https://app.codeanywhere.com/) IDE was used for creating the website and using the built in terminal to push the site to GitHub.

5. [GitHub](https://github.com/) was used to store the project's code after being pushed from Codeanywhere.

6. [Balsamiq Wireframes](https://balsamiq.com/wireframes/) were used to design the general layout and feel of the website and the high fidelity mock up during the design process.

7. [Autoprefixer CSS](https://autoprefixer.github.io/) was used to add vendor prefixes to the CSS rules, to ensure that they work across all browsers.

8. [Am I Responsive](https://ui.dev/amiresponsive?url=https://8002-coder4916-ci-milestone-ylxy4w9e48.us2.codeanyapp.com/index.html) was used to preview the website across a variety of popular devices.

9. [Squoosh](https://squoosh.app/) was used to reduce the file size of the images, and change from .jpg to .AVIF. This helped to improve the overall performance of the website.

10. [Coolors](https://coolors.co/) was used to create a cohesive color scheme for the website.

[Back to top](#think-in-space)

## **Issues and Bugs**

- Issue: Bootstrap navbar toggler would not collapse correctly, once expanded on a small device.

Solution - After some tutoring, it was noticed that I had an additional Javascript bundle link included in the HTML. Once deleted, the toggler was tested, and worked.

- Issue: Gaps still appearing around .row and .col classes when importing from Bootstrap whilst using the no gutters class:

Solution - Understanding Bootstrap 5, and being aware of updates. Eg. the class ".no gutters", to remove automatic padding that Bootstrap provides with .div rows and columns, became ".g-0". The solution to this was found on [Stack Overflow](https://stackoverflow.com/questions/21254889/how-to-remove-the-gutter-spacing-between-columns-in-bootstrap)

- Issue: Bootstrap color automatically added when using it's .active class for the navigation bar.

Solution - Resorted to using an !Important color in navbar CSS to overide.

- Issue: Navigation menu was not responsive when changing to different devices.

Solution - When trying to make the NavBar responsive via CSS, it was found that this could be done via a Bootstrap .fluid class.

- Issue: Ports not working/updating several times on Codeanywhere IDE.

Solution - I regularly had to change the Port or reset to make the updates to the site work, so I could see the Website's progress.

- Issue/Bug: README.md automatically began deleting itself while updating, when laptop was plugged into a smart TV.

Solution - README.md had to be copied and pasted from Github repository. Some of the Readme had to be re-written.

## **Deployment**

The Website was developed using Codeanywhere as the IDE, commited to Git as a local repository and finally pushed/stored to GitHub.

### **Deployment to GitHub Pages**

The website was deployed to Github pages using the following steps:

1. Log in to GitHub.
2. Navigate to the main page of GitHub Repository that will be deployed.
3. At the top of the Repository, locate the "Settings" button on the menu and click it.
4. Inside the Settings, on the left side of the page, there’s a list of tab menu. Locate the “Pages” tab, and click it.
5. Under "Source", click the dropdown called "None", select "Master", and then click the “Save” button.
6. The page will automatically refresh.
7. Click on Actions and then 'Deploy Static Content to Pages'
8. There’s a notification message, your site is live at [https://coder4916.github.io/ci_milestone/], that provides the now published website on the pages tab in Github settings.

### **Forking the Github Repository**

By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:

1. Log in to GitHub.
2. Navigate to the main page of the GitHub Repository that you want to fork.
3. At the top right of the Repository just below your profile picture, locate the "Fork" Button.
4. You should now have a copy of the original repository in your GitHub account.  

Changes made to the forked repository can be merged with the original repository via a pull request.

### **Making a Local Clone**

By cloning a GitHub Repository you can create a local copy on your computer of the remote repository. This allows you to make all of your edits locally rather than directly in the source files of the origin repository, by using the following steps:

1. Log in to GitHub.
2. Navigate to the main page of the GitHub Repository that you want to clone.
3. Above the list of files, click the dropdown called "Code".
4. To clone the repository using HTTPS, under "HTTPS", copy the link.
5. Open Git Bash.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type git clone, and then paste the URL you copied in Step 4.
8. Press Enter. Your local clone will be created.

[Back to top](#think-in-space)

## **Testing**

### **User Stories Testing**

#### **First Time User Goal**

1. As a first-time user, I want to be able to find the information I'm looking for quickly and easily and be able to navigate the website with ease.

- The navigation bar is clearly defined, with an .active attribute to display to the user which page they are on. A subtle hover function when the user moves the cursor over the menu items increases user friendliness, and icons are attached to each option to assist the user with their choice.
- A logo on the top of the page and in the footer leads the user back to the Home page increasing accessibility further.
- A 'Back to Top' button is included on every page so the user can return to the navigation bar where required.
- Links to further information can be easily accessed via each of the page's footer menu.

![Navigation Bar Screenshot](/assets/images/navigation-screenshot.png)

2. As a first-time user, I want to learn about the Coach/Owner and find out about their previous qualifications/experience.

- The Home page contains three sections; The Coach, Background and Tried and Tested, which include information about the Coach's experience, background, qualifications and people he has helped. This is where the user will begin when arriving at the Website.

![Home Page Screenshot](/assets/images/home-page-screenshot.png)

3. As a first-time user, I want to know what type of coaching services the Owner/Website offers.

- A second page has a 'What to Expect' section which includes a step by step guide based on an initial coaching session. A carousel also informs the reader of previous client experiences.

![Coaching Page Screenshot](/assets/images/coaching-page-screenshot.png)

4. As a first-time user, I want to be able to locate the owner's social media links to see their followings and find any potential reviews etc.

- The Coach's LinkedIn profile is attached to the footer. There is also a carousel on the coaching page which displays previous client reviews.

![Footer Screenshot](/assets/images/footer-screenshot.png)

5. As a first-time user, I want to have the option to contact the owner further if required.

- A contact form and the Coach's contact details are available on a Contact page on the website. A link to this is included in the footer of each page, as well as via the navigation bar.

![Contact Page Screenshot](/assets/images/contact-screenshot.png)

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
- The Code Institute tutors who helped me with some of the issues I had when building the site, and for supporting me with the testing element of my Readme.md file.
- My friend and mentor Elwyn Davies, for the site features and his continued support throughout, as well as his insight into the coaching world.
- My wife Beth for her constant support throughout the first module, and for proof reading and testing my site material.

[Back to top](#think-in-space)
