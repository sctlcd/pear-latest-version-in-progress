# [Pearl](https://sctlcd-pearl3-latest-version.herokuapp.com/)

<img src="https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/design/mockups.png" alt="Pearl" width="800">
<dl>
<dd>Do you like <span class="font-weight-bold">creative activities</span>, <span class="font-weight-bold">arts and crafts</span> and <span class="font-weight-bold">making things by yourself</span> with creativity, happiness and your own two hands ?</dd>
<dd>Then this website is a <span class="font-weight-bold">pearl</span> to you!</dd>
<dd>At Pearl's you can <span class="font-weight-bold">purchase arts and crafts supplies</span> and <span class="font-weight-bold">sharing customers' work of art</span> in the meantime as <span class="font-weight-bold">getting inspiration</span> from other customers' creative work in the <span class="font-weight-bold">gallery</span>.</dd>

[Let me show you!](https://sctlcd-pearl3-latest-version.herokuapp.com/)
<br />
<br />
**Warning**
<br />
Because of an issue relative to submitting a form with an uploaded image in my deployed environment I did set up the image field in the gallery model as not required for limiting the impact of the issue which has been solved just before my project deadline submission. I set up initially the gallery image field as required. I will set it back to required in the future.

---

# Table of Contents <a name="tableOfContents"></a>

1. [About](#about)
	- [Why this project?](#whyThisProject)

1. [UX](#ux)
	- [User Stories](#userStories)
	- [Design](#design)
		- [Framework](#framework)
		- [Color Scheme](#colorScheme)
		- [Icons](#icons)
		- [Typography](#typography)
	- [Wireframes](#wireframes)

2. [Features](#features)
	- [Existing Features](#existingFeatures)

3. [Technologies Used](#technologiesUsed)
	- [Front-End Technologies](#frontEndTechnologies)
	- [Back-End Technologies](#backEndTechnologies)

4. [Relational scheme](#relationalScheme)

5. [Testing](#testing)
	- [User story validation](#userStoryValidation)
	- [Layout responsiveness](#layoutResponsiveness)
	- [Compatibility](#compatibility)
	- [Testing left](#testingLeft)
	- [Validators](#validators)
	- [Known Issues](#knownIssues)

6. [Deployment](#deployment)
	- [Deployment – Run locally](#deploymentRunLocally)
	- [Deployment – Live website](#deploymentLiveWebsite)


7. [Credits](#credits)
	- [Content](#content)
	- [Media](#media)
	- [Code](#code)
	- [Acknowledgements](#acknowledgements)

---

## About <a name="about"></a>

The primary purpose of Pearl is to **purchase arts and crafts supplies**. Its secondary purpose is to **share customers' work of art** in the meantime as **getting inspiration** from other customers' creative work in the **gallery**. And this anytime, anywhere as this application is available on various devices as desktops, tablets and mobile.

Back to [top](#tableOfContents)

---

### Why this project? <a name="whyThisProject"></a>

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, the **Full Stack Frameworks With Django** module. The objective of this milestone project is building a full-stack site based around business logic used to control a centrally-owned dataset, setting up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

My modern responsive e-commerce arts and crafts supplies site is built using HTML, CSS, Material Design for Bootstrap, JavaScript, jQuery, Django, Python, PostgreSQL.

Back to [top](#tableOfContents)

---

## UX  <a name="ux"></a>

### User Stories <a name="userStories"></a>

:heavy_check_mark: successfully implemented
<br/>
:x: not yet implemented

"***As a non authenticated user, I want to _____***"
- :heavy_check_mark: view the site from any device (mobile, tablet, desktop)
- :heavy_check_mark: be able to register
- :heavy_check_mark: be able to log in
- :heavy_check_mark: filter and search amongst all products
- :heavy_check_mark: view all products
- :heavy_check_mark: view product details
- :heavy_check_mark: view quantity in shopping bag of current product in product details page
- :heavy_check_mark: view gallery images
- :heavy_check_mark: view a gallery image (modal)
- :heavy_check_mark: add products to my bag
- :heavy_check_mark: update products in my bag / adjust product quantity
- :heavy_check_mark: remove products in my bag
- :heavy_check_mark: checkout my order
- :heavy_check_mark: send a contact request


"***As an authenticated user, I want to _____***"
- :heavy_check_mark: be able to log out
- :heavy_check_mark: filter and search amongst all products
- :heavy_check_mark: view all products
- :heavy_check_mark: view product details
- :heavy_check_mark: view quantity in shopping bag of current product in product details page
- :heavy_check_mark: view gallery images
- :heavy_check_mark: view a gallery image (modal)
- :heavy_check_mark: share a gallery image
- :heavy_check_mark: view my profile
- :heavy_check_mark: update my profile
- :heavy_check_mark: add products to my bag
- :heavy_check_mark: update products in my bag / adjust product quantity
- :heavy_check_mark: remove products in my bag
- :heavy_check_mark: save delivery info to profile while checkout
- :heavy_check_mark: checkout my order
- :heavy_check_mark: send a contact request


"***As an authenticated admin, I want to _____***"

- :heavy_check_mark: all user stories that apply to an authenticated user apply to an authenticated admin.
- :heavy_check_mark: add a gallery item with an image
- :heavy_check_mark: add a gallery item without an image
- :heavy_check_mark: edit a gallery item with an image
- :heavy_check_mark: edit a gallery item without an image
- :heavy_check_mark: delete a gallery image
- :heavy_check_mark: approved a gallery image
- :heavy_check_mark: add a product with an image
- :heavy_check_mark: add a product without an image
- :heavy_check_mark: edit a product with an image
- :heavy_check_mark: edit a product without an image
- :heavy_check_mark: delete a product

Back to [top](#tableOfContents)

---

### Design <a name="design"></a>

I did choose a warm, joyful and energetic orange ![#fc9601](https://placehold.it/15/fc9601/fc9601) `#fc9601` combined with sober and reliable colors ranging between off-white ![#fafafa](https://placehold.it/15/fafafa/fafafa) `#fafafa` and black ![#000](https://placehold.it/15/000/000) `#000` with shades of grey (more color details in [Color Scheme](#colorScheme) section).
<br />
I first selected my [logo](https://www.flaticon.com/free-icon/craft_3079199) from Flaticon(https://www.flaticon.com) which I customized in [Pearl logo](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/media/logo/pearl-min.png).
<br />
Then I chose [images](https://github.com/sctlcd/pearl-latest-version-in-progresstree/master/media) relative to arts and crafts and creative activities which fit well in my color scheme and in the space allocated.
<br />
I finally selected the main home page image, a [fire spin](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/media/home/hero_image/hero-image-background-min.jpg) picture, as I found it absolutely stunning, very eye-catchy and intriguing. Catching customers/visitors' attention and raising their interest and curiosity are, I believe, a good recipe for new visitors as much as for regular customers of an e-commerce site.  
<br />
I decided to implement a customers' gallery and offering the possibility to share your own piece of art while getting inspiration from other customers' art work. I believe this feature is a very interesting one as it involves the customers/makes the customers participate in the website building. They are actors, in a way, of the gallery page building and its content.  

Back to [top](#tableOfContents)

---

#### Framework <a name="framework"></a>

- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/)
	- I really like the modern and clean layout of Material Design and the ease of use and standards of Bootstrap so I wanted to give a try and getting familiar with Material Design for Bootstrap
- [jQuery 3.5.1](https://jquery.com/)
	- For the purpose of keeping the JavaScript minimal
- [Django 3.1.1](https://www.djangoproject.com/)

Back to [top](#tableOfContents)

---

#### Color Scheme <a name="colorScheme"></a>

- ![#fc9601](https://placehold.it/15/fc9601/fc9601) `#fc9601`
- ![#6a6a6e](https://placehold.it/15/6a6a6e/6a6a6e) `#6a6a6e`
- ![#fafafa](https://placehold.it/15/fafafa/fafafa) `#fafafa`
- ![#efefef](https://placehold.it/15/efefef/efefef) `#efefef`
- ![#6c757d](https://placehold.it/15/6c757d/6c757d) `#6c757d`
- ![#d8d8d8](https://placehold.it/15/d8d8d8/d8d8d8) `#d8d8d8`
- ![#d6d4d4](https://placehold.it/15/d6d4d4/d6d4d4) `#d6d4d4`
- ![#dee2e6](https://placehold.it/15/dee2e6/dee2e6) `#dee2e6`
- ![#000](https://placehold.it/15/000/000) `#000`

Back to [top](#tableOfContents)

---

#### Icons <a name="icons"></a>

- [Font Awesome 5.14.0](https://fontawesome.com/): It fits my needs for this project
	- [Gallery](https://fontawesome.com/icons/images?style=solid)
	- [My account](https://fontawesome.com/icons/user?style=solid)
	- [Bag](https://fontawesome.com/icons/shopping-basket?style=solid)
	- [Free worldwide delivery](https://fontawesome.com/icons/shipping-fast?style=solid)
	- [30 days](https://fontawesome.com/icons/exchange-alt?style=solid)
	- [Satisfaction guaranteed](https://fontawesome.com/icons/hand-holding-usd?style=solid)
	- [Secured payment](https://fontawesome.com/icons/credit-card?style=regular)
	- [Facebook](https://fontawesome.com/icons/facebook-f?style=brands)
	- [Pinterest](https://fontawesome.com/icons/pinterest-p?style=brands)
	- [Instagran](https://fontawesome.com/icons/instagram?style=brands)
	- [Twitter](https://fontawesome.com/icons/twitter?style=brands)
	- [YouTube](https://fontawesome.com/icons/youtube?style=brands)
	- [Location](https://fontawesome.com/icons/map-marker-alt?style=solid)
	- [Email](https://fontawesome.com/icons/envelope?style=solid)
	- [Phone](https://fontawesome.com/icons/phone?style=solid)
	- [Working hours](https://fontawesome.com/icons/building?style=solid)
	- [Copyright](https://fontawesome.com/icons/copyright?style=regular)
	- [Github](https://fontawesome.com/icons/github?style=brands)
	- [Info](https://fontawesome.com/icons/info-circle?style=solid)
	- [Exclamation mark](https://fontawesome.com/icons/exclamation-circle?style=solid)

- [Flaticon](https://www.flaticon.com/): It fits my needs for this project
	- Pearl logo: from [original version](https://www.flaticon.com/free-icon/craft_3079199) to customize in [Pearl version](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/media/logo/pearl-min.png)

Back to [top](#tableOfContents)

---

#### Typography <a name="typography"></a>

- [Google Fonts](https://fonts.google.com/) were used across the site:
	- [Open Sans](https://fonts.google.com/specimen/Open+Sans) - default font
	- [Smythe](https://fonts.google.com/specimen/Smythe) - showcase section on home page
	- [Crafty Girls](https://fonts.google.com/specimen/Crafty+Girls) - customer review section on home page

Back to [top](#tableOfContents)

---

### Wireframes <a name="wireframes"></a>

I have used Balsamiq Wireframes for my wireframes because:

- Code Institute have provided all students a free licence. I got to use this software a few years ago and I am pretty happy to get the chance to use it again.
- The simplicity, rapidity and ease of use by focusing on structure and content.
- My wireframes for this project can be found here in the [wireframes](https://github.com/sctlcd/pearl-latest-version-in-progresstree/master/design/wireframes/) sub-directory.

Remark: There is a bug at the opening of the balsamiq file: in each page on the mobile version, there are icon overlays on the right corner.

Back to [top](#tableOfContents)

---

## Features <a name="features"></a>

### Existing Features <a name="existingFeatures"></a>

#####  Navigation bar

- A top navbar with the logo and the name of the website, menu items and dropdown menu items : Gallery, My Account, Shopping bag and a product search bar.
- a navbar with the products menu items and dropdown menu items

- Common desktop/mobile:
	- Transparent navbar when
		- the window is at the top
		- the header is not hovered
		- menu/sub-menu are not opened
		- navbar collapse menu is collapsed
	- White navbar when
		- the window is scrolled down
		- the header is hovered
		- menu/sub-menu are opened
		- navbar collapse menu is pulled down
	- Orange double line on the bottom of the navbar when the page is scrolled
	- Menu item highlighted when hovered or selected/pulled down
	- Sub-menu item highlighted when hovered
	- "My account" and "Gallery" menu closes when the user clicks anywhere in the page

- Specific desktop :
	- Navbar item sub-menu closes when the user clicks anywhere in the page
	- Logo of the website
	- Favicon

- Specific mobile :
	- Search input field in the mobile top header close when the user clicks anywhere in the page
	- Navbar collapse menu closes when the user clicks on "Search", "My Account" or "Gallery" icon links

	Back to [top](#tableOfContents)

	---

##### Footer

- Social medias to get connected with Pearl
- 3 sections : Company presentation, links to other pages of the website (not implemented), contact section with a contact button redirecting to the Contact page.
- Copyright mention with my name and my gitbhub repository

##### Home page

- 6 sections: Shop now, website order feature offered, target activities, customer reviews, Share your work of art, Stay tune (newsletter subscription not implemented, for presentation purpose)

Back to [top](#tableOfContents)

---

##### Products page

- A Product collection presented in a "mosaic format"
- Possibility to sort product by price, rating, name, category
- Number of Product result from the product filter or from the Search option.
- Link back to Product home
- Product name, price, category and rating are visible
- Top/down page button to facilitate the navigation
- Edit/delete button are visible if authenticated as Admin
- Clicking on Edit/Delete opens a confirmation modal to continue to edit/delete or to cancel.
- Selecting Yes redirects to the Edit Product page or delete the product

##### Products details page

- A page with product details: name, description, price, category, rating, product image, quantity to add to shopping bag, number of current product in shopping bag is display to inform the user
- Buttons: Keep shopping, Add to bag

Back to [top](#tableOfContents)

---

##### Products management page

- Add Product page: add product form containing the fields: Category, Sku, Name, Description, Price, Image, select image button, buttons: Cancel, Add Product
- Edit Product page: edit product form containing the fields: Category, Sku, Name, Description, Price, Image, buttons: Cancel, Edit Product

##### Gallery page

- A gallery of customers' work of art presented in a "mosaic format".
- The gallery images can be filtered by All, Mosaic, Painting, Beads, other
- The author name is displayed below the images preceded by a copyright
- Clicking on the image opens a gallery image modal composed of the author name preceded by a copyright mention as title, social media links to spread the world, close button
- Top/down page button to facilitate the navigation
- Edit/delete button are visible if authenticated as Admin
- Clicking on Edit/Delete opens a confirmation modal to continue to edit/delete or to cancel.
- Selecting Yes redirects to the Edit Gallery image page or delete the gallery image

Back to [top](#tableOfContents)

---

##### Share gallery page

- A share gallery item form can be submitted containing the fields: user name, email, author name, gallery category, image, note, an info message "The author name filled in this form will be accompanied by the copyright mention when your photo will be published.", buttons: home, share

##### Gallery management page

- Add Gallery item page: add gallery item form containing the fields: user name, email, author name, gallery category, image, select image button, note, is approved,  buttons: cancel, add gallery image
- Edit Gallery item page: edit gallery item form containing the fields: user name, email, author name, gallery category, image, select image button, note, is approved,  buttons: cancel, edit gallery image

Back to [top](#tableOfContents)

---

##### Profile page

- To view and update your profile
- Default delivery information form containing: phone number, street address 1, street address 2, town or city, county state or locality, postal code, country, update information buttons
- Order history table containing: order number, date, items, order total


##### Shopping bag page

- To view and adjust your shopping bag
- Shopping bag table containing: product image, product description, price, quantity, subtotal
- update/remove links to quantity fields
- Bag total price, delivery cost and grand total price are displayed
- A message inform the user about free delivery: "You could get free delivery by spending just $XX.XX more!"
- buttons: keep shopping, secure checkout

Back to [top](#tableOfContents)

---

##### Checkout page

- Checkout form containing Full name, email address, phone number, street address 1, street address 2, town or city, county state or locality, postal code, country, payment details, buttons: adjust bag, complete order.
- A message informs the user "Your card will be charged $XX.XX"
- Order summary table containing: product image, item, product name, quantity, subtotal
- Order total, delivery and grand total prices are displayed


##### Contact us page

- Section with Pearl information details: address, phone number, working hours, email street_address
- Contact form containing: first name, last name, email, message, buttons: home, spend
- Street view map of the shop location

Back to [top](#tableOfContents)

---

##### No result found page

- Humoristic picture and message letting know the user no result have been found matching with his/her search. - [No result found page](https://sctlcd-pearl3.herokuapp.com/products/?q=aaaaa)
- Link redirecting to Products Home page

##### Error pages

- 404 page - [No page found](https://sctlcd-pearl3.herokuapp.com/products/ggggg)
	- Link redirecting to Products Home page  
- 500 page - Internal server error
	- Link redirecting to Products Home page  

	Back to [top](#tableOfContents)

	---

##### Pearl Admin Portal

- I customise the Default Django Administration in [pearl/urls.py](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/pearl/urls.py):
```
admin.site.site_header = 'Pearl Administration'
admin.site.site_title = 'Pearl Admin Portal'
admin.site.index_title = 'Welcome to Pearl Admin Portal'
admin.site.site_url = '/admin'
```

- I changed the time zone to match with the physical location of Pearl shop in New Orleans in USA and the format of time and date in [pearl/settings.py](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/pearl/settings.py)
```
# Time Zone in New Orleans, Louisiana, USA : CST — Central Standard Time
# corresponding to America/Chicago according to
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = "Y-m-d H:i"
```

Back to [top](#tableOfContents)

---

## Technologies Used <a name="technologiesUsed"></a>

- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Atom](https://atom.io/) - Used as a local IDE.
- [Compressjpeg](https://compressjpeg.com/) - Used to compress images for loading faster
- [Techsini](https://techsini.com/multi-mockup/) - Used to generate multi-device website mockup
- [Ngrok 2.3.35](https://ngrok.com/) - Expose a local web server to the public internet over secure tunnels

Back to [top](#tableOfContents)

---

### Front-End Technologies <a name="frontEndTechnologies"></a>

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/) - used as a front-end framework for building responsive, mobile-first websites and apps
- [JavaScript](https://www.javascript.com/) - Used for user interactions.
- [jQuery 3.5.1](https://jquery.com/) - JavaScript library, used to simplify some of the DOM manipulations.
- [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments
- [Amazon AWS S3](https://aws.amazon.com/) - Used to store staticfiles and media folders and files.

Back to [top](#tableOfContents)

---

### Back-End Technologies <a name="backEndTechnologies"></a>

- [Python 3.8](https://www.python.org/) - Used as the back-end programming language.
- [Django 3.1.1](https://www.djangoproject.com/) - Used as Python web framework.
- [Heroku](https://www.heroku.com/) - Used for app hosting.
- [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

Back to [top](#tableOfContents)

---

## Relational scheme <a name="relationalScheme"></a>

The Relational scheme diagram can be found [here](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/design/relational-scheme.png)

Pearl database table details:

**category**
```
_id PK int
name NULL varchar
friendly_name NULL varchar
```

**product**
```
_id PK int
sku NULL varchar
name varchar
description text
price money
category NULL int FK >- category._id
rating NULL decimal
image NULL file
created_at date
updated_at NULL date
```

**user_account**
```
_id PK int
email email
user_name varchar
password varchar
first_name NULL varchar
last_name NULL varchar
is_superuser boolean
is_staff boolean
is_active boolean
```

**user_profile**
```
_id PK int
user int FK - user_account._id
default_phone_number NULL varchar
default_street_address1 NULL varchar
default_street_address2 NULL varchar
default_town_or_city NULL varchar
default_postcode NULL varchar
default_county NULL varchar
default_country NULL country
```

**order**
```
_id PK int
order_number varchar
user_profile NULL int FK >- user_profile._id
full_name varchar
email email
phone_number varchar
country country
postcode NULL varchar
town_or_city varchar
street_address1 varchar
street_address2 NULL varchar
county NULL varchar
created_at date
updated_at NULL date
delivery_cost money
order_total money
grand_total money
original_bag text
stripe_pid varchar
```

**order_line_item**
```
order int FK >- order._id
product int FK >- product._id
quantity int
lineitem_total money
```

**contact**
```
_id PK int
first_name varchar(254)
last_name varchar(254)
email email
message text
date date
```

**gallery**
```
_id PK int(254) FK >- user_account._id
user_name varchar
email email
author_name varchar
gallery_category NULL int FK >- gallery_category._id
image NULL file
note NULL varchar
created_at date
updated_at NULL date
is_approved boolean
```

**gallery_category**
```
_id PK int
name NULL varchar
friendly_name NULL varchar
```

Back to [top](#tableOfContents)

---

## Testing <a name="testing"></a>

### User story validation <a name="userStoryValidation"></a>

:heavy_check_mark: *as expected*
<br />
:x: *not as expected*
<br />
n/a *not applicable*

| User story | authenticated as admin | authenticated as regular user | non authenticated user | note |
| :--- | :--- | :---| :--- | :--- |
| view the site from any device (mobile, tablet, desktop) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| be able to register | n/a | n/a | :heavy_check_mark: | - |
| be able to log in | n/a | n/a | :heavy_check_mark: | - |
| be able to log out | :heavy_check_mark: | :heavy_check_mark: | n/a | - |
| filter and search amongst all products | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| view all products | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| view a product details | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| view quantity in shopping bag of current product in product details page | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| add products with an image | :heavy_check_mark: | n/a | n/a | - |
| add products without an image | :heavy_check_mark: | n/a | n/a | - |
| edit products with an image | :heavy_check_mark: | n/a | n/a | - |
| edit products without an image | :heavy_check_mark: | n/a | n/a | - |
| delete products | :heavy_check_mark: | n/a | n/a | - |
| view gallery images | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| view a gallery image (modal) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| share a gallery image | :heavy_check_mark: | :heavy_check_mark: | n/a | - |
| add a gallery item with an image | :heavy_check_mark: | n/a | n/a | - |
| add a gallery item without an image | :heavy_check_mark: | n/a | n/a | - |
| edit a gallery item with an image | :heavy_check_mark: | n/a | n/a | - |
| edit a gallery item without an image | :heavy_check_mark: | n/a | n/a | - |
| delete a gallery image | :heavy_check_mark: | n/a | n/a | - |
| approved a gallery image | :heavy_check_mark: | n/a | n/a | - |
| view my profile | :heavy_check_mark: | :heavy_check_mark: | n/a | - |
| update my profile | :heavy_check_mark: | :heavy_check_mark: | n/a | - |
| add products to my bag | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| update products in my bag / adjust product quantity | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| remove products in my bag | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| save delivery info to profile while checkout | :heavy_check_mark: | :heavy_check_mark: | n/a | - |
| checkout my order | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |
| send a contact request | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - |

Back to [top](#tableOfContents)

---

### Layout responsiveness <a name="layoutResponsiveness"></a>

|  | Moto G4 | Galaxy S5 | Pixel 2 | Pixel 2 XL | iPhone 5/SE | iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | Surface Duo | iPad | iPad Pro | Desktop 1024px | Desktop > 1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| website is responsive <= 992px | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | n/a | n/a | n/a | n/a |
| website is responsive >= 992 px | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Good | Good | Good | Good |
| Navigation bar: logo / links / search / menu| Good | Good | Good  | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| Footer: text / links / buttons | Good | Good |  Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| links / urls work | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| Images work | Good | Good | Good  | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| Renders as expected | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| Back-End Functionality | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |
| Stripe payment works | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good |

The site begins to overflow-X at < 280px.
<br>
Some elements and product images are small on mobile, especially under 360px.

Back to [top](#tableOfContents)

---

### Compatibility <a name="compatibility"></a>

#### Browser compatibility

I tested the website across the 6 main browsers in both desktop and mobile configuration to ensure a large number of users can use it successfully.

- Chrome v.91.0
- Edge v.91.0
- Firefox v.89.0
- Safari v.5.1.7 for Windows 10
- Opera v.76.0
- Internet Explorer v.11

|All pages | Chrome | Edge | Firefox | Safari | Opera | IE |
| :--- | :--- | :---| :--- | :--- | :--- | :--- |
| Expected appearance | Good | Fair | Good | Poor | Good | Poor |
| Expected responsiveness | Good | Good | Good | Poor | Good | Poor |

- IE: Some CSS3 properties and HTML5 elements are not fully supported

- Safari v.5.1.7: It’s an outdated version and lacks many of the features present in the latest version of Safari. The last version of Safari for Windows was released on May 9, 2012.

#### Chrome's DevTools Audit Report

| Performance | Accessibility | Best Practices | SEO |
| :---: | :---: | :---: | :---: |
| 89% | 82% | 93% | 90% |

The Chrome DevTools Audit Report can be found in my [testing folder](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/testing/devtools-audit-report.PNG)

Back to [top](#tableOfContents)

---

### Testing left <a name="testingLeft"></a>

- There is no way to install the latest version of the Safari browser on Windows 10 as Apple stopped developing Safari for Windows operating system long ago.
For testing this website on the latest version of Safari, I will have to install the newest version of macOS on Windows 10 in a virtual machine.

Back to [top](#tableOfContents)

---

### Validators <a name="validators"></a>

**HTML**
- [W3C HTML Validator](https://validator.w3.org/)
	- Django Template elements not recognized: {{ variable }} {% for %} {% if %} etc.
	- No error

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
	- No error

**Javascript**
- [Javascript Validator](https://jshint.com/)
	- '$' is not defined. This is for jQuery. 'STRIPE' is not defined. This is for Stripe.
	- No error

**Chrome DevTools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
	- Console Navigating through the Website rendered no critical fails/errors in the console that were necessary to fix.

**Python**
- [Python validator](http://pep8online.com/)
 - No error

Back to [top](#tableOfContents)

---

### Known Issues <a name="knownIssues"></a>

- If mobile menu is collapsed and if the user scrolls down then scrolls up to the very top of the page window (window scroll = 0) then Top/Down page buttons are visible (from products page, gallery page).  
- Set image gallery back to required.
- Create products and gallery sub-directories in media folder containing respectively product images and gallery images.
- Create a Project folder at the root of Pearl repository containing the code project repositories in order to separate design and testing folders from the code project repository.

Back to [top](#tableOfContents)

---

## Deployment <a name="deployment"></a>

### Deployment – Run Locally <a name="deploymentRunLocally"></a>

It's highly recommended to work in a virtual environment, but not absolutely required.

In order to run this project locally on your own system, you will need the following installed (as a bare minimum):

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green "*Clone or download*" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
    - `git clone https://github.com/sctlcd/pearl.git`
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your own credentials.

	| **Key** | **Value** |
	|----------|:-------------:|
	| AWS_ACCESS_KEY_ID | <your_aws_access_key_id>  |
	| AWS_SECRET_ACCESS_KEY | <your_aws_secret_access_key> |
	| DATABASE_URL | <your_database_url> |
	| EMAIL_HOST_PASS | <your_email_host_pass> |
	| EMAIL_HOST_USER | <your_email_host_user> |
	| SECRET_KEY | <your_secret_key> |
	| STRIPE_PUBLIC_KEY| <your_stripe_public_key> |
	| STRIPE_SECRET_KEY | <your_stripe_secret_key> |
	| STRIPE_WH_SECRET | <your_stripe_wh_secret> |
	| USE_AWS | True |
	| DEBUG | DEVELOPMENT |

- Install all requirements from the [requirements.txt](https://github.com/sctlcd/pearl-latest-version/blob/master/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- In the IDE terminal, use the following command to launch the Django project:
    - `python manage.py runserver`
- The Django server should be running locally now on **http://127.0.0.1:8000** (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.
- When you run the Django server for the first time, it should create a new *SQLite3* database file: **db.sqlite3**
- Next, you'll need to make migrations to create the database schema:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- In order to access the Django *Admin Panel*, you must generate a superuser:
    - `python manage.py createsuperuser`
    - (assign an admin username, email, and secure password)

Once the database migrations and superuser have been successfully completed, Django should migrate the existing *migrations.py* files from each app to configure the following relational schema:

- [Relational Schema](https://github.com/sctlcd/pearl-latest-version-in-progress/blob/master/design/relational-scheme.png)

Back to [top](#tableOfContents)

---

### Deployment – Live Website <a name="deploymentLiveWebsite"></a>

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:

- Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
    - `sudo pip3 freeze --local > requirements.txt`
    - The *requirements.txt* file for this project can be found here: [requirements.txt](https://github.com/sctlcd/pearl-latest-version/blob/master/requirements.txt)
- Create a **Procfile** to tell Heroku what type of application is being deployed using *pearl-latest-version*, and how to run it:
    - `echo web: gunicorn main.wsgi:application > Procfile`
    - The *Procfile* for this project can be found here: [Procfile](https://github.com/sctlcd/pearl-latest-version/tree/master/profiles)
- Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
- In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your *.env* file with your new *database-url* details.
- In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables. You will need to copy/paste all of the *.env* key value pairs into the config variables, but please omit the *development=1* variable; this is only for local deployment.

	| **Key** | **Value** |
	|----------|:-------------:|
	| AWS_ACCESS_KEY_ID | <your_aws_access_key_id>  |
	| AWS_SECRET_ACCESS_KEY | <your_aws_secret_access_key> |
	| DATABASE_URL | <your_database_url> |
	| EMAIL_HOST_PASS | <your_email_host_pass> |
	| EMAIL_HOST_USER | <your_email_host_user> |
	| SECRET_KEY | <your_secret_key> |
	| STRIPE_PUBLIC_KEY| <your_stripe_public_key> |
	| STRIPE_SECRET_KEY | <your_stripe_secret_key> |
	| STRIPE_WH_SECRET | <your_stripe_wh_secret> |
	| USE_AWS | True |

- Your app should be successfully deployed to Heroku at this point, but you're not quite finished yet!
- Update the *settings.py* file to connect the remote database using this Python package: `dj_database_url`
- Re-build the migrations and create a superuser to your new remote database using the instructions in the *local deployment* section above.
- Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your *staticfiles* and *media* files. From the **S3 buckets** section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:

**Permissions** > **CORS configuration**:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

**Permissions** > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
```

*! IMPORTANT ! - on the **Resource** line above, be sure to replace `<x>` with your **AWS bucket arn** details, but retain the `/*` at the end.* It should look similar to this:
    - `"Resource": "arn:aws:s3:::my-bucket-name/*"`

- From here, you'll need to navigate to the **IAM** section of AWS.
    - Create a *New Group* and be sure to select your existing S3 Bucket details to attach.
    - Create a *New Policy* and a *New User* in the IAM section as well, then attach these to the Group you just built.
- In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
    - `python manage.py collectstatic`
- Sign up for a free [Stripe](https://stripe.com) account. Navigate to the **Developers** section, and click on **API Keys**. You should have two confidential keys which need to be added to your *.env* file, as well as your Heroku config vars. These keys are:
    - `Publishable Key`: **pk_test_key**
    - `Secret Key`: **sk_test_key**

Congratulations! Your project should be completely setup and ready for remote deployment!

Back to [top](#tableOfContents)

---

## Credits <a name="credits"></a>

My inspiration comes from:
- [Etsy](https://www.etsy.com/) - E-commerce website focused on handmade or vintage items and craft supplies
- [Cultura](https://www.cultura.com/) - E-commerce website specialized in cultural, arts and crafts goods and leisure activities

Back to [top](#tableOfContents)

---

### Content <a name="content"></a>

Sources of the content used on this site:
- [Baker Ross](https://www.bakerross.ie/) - E-commerce website specialized in arts and crafts supplies

Back to [top](#tableOfContents)

---

### Media <a name="media"></a>

Sources of the images used on this site:
- From media/home/hero_image sub-directory
	- [hero-image-background-min](https://pixabay.com/fr/photos/laine-d-acier-sombre-firespin-458840/) - [Pixabay](https://pixabay.com/) | copyright [463259 - Faizal Sugi](https://pixabay.com/fr/users/463259-463259/)  

- From media/home/image_showcases sub-directory
	- [create-beads-min](https://www.flickr.com/photos/woolgenie/11130456836/) - [Flickr](https://www.flickr.com/) | copyright [Heather](https://www.flickr.com/photos/woolgenie/)
	- [create-grafiti-min](https://www.flickr.com/photos/rem60/31635422637/) - [Flickr](https://www.flickr.com/) | copyright [Rosemary Miklitsch](https://www.flickr.com/photos/rem60/)
	- [create-mosaic-min](https://www.flickr.com/photos/mikecogh/43105291024/) - [Flickr](https://www.flickr.com/) | copyright [Michael Coghlan](https://www.flickr.com/photos/mikecogh/)

- From media/home/testimonials sub-directory
	- [female-2-min](https://pixabay.com/fr/photos/mod%C3%A8le-femme-portrait-336658/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [female-1-min](https://pixabay.com/fr/photos/jeune-fille-%C3%A9changisme-coiffure-1245835/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [male-1-min](https://www.pexels.com/photo/portrait-photo-of-man-in-white-crew-neck-t-shirt-with-assorted-hand-tools-in-background-1139743/) - [Pexels](www.pexels.com) | copyright [Juan Pablo Serrano Arenas](https://www.pexels.com/@juanpphotoandvideo)

- From media/home/gallery sub-directory
	- [gallery-background-1920-min](https://www.pexels.com/photo/apple-device-camera-camera-lens-desk-593325/) - [Pexels](https://www.pexels.com/) | copyright [Jessica Lewis](https://www.pexels.com/@thepaintedsquare)

- From media/logo sub-directory
	- [pearl-min](https://www.flaticon.com/free-icon/craft_3079199) - [Flaticon](https://www.flaticon.com/) | copyright [Freepik](https://www.flaticon.com/authors/freepik)

- From media/error sub-directory
	- [no-results-found-min](https://all-free-download.com/free-vector/download/exploration-job-background-searching-man-sketch-cartoon-design_6844384.html) - [Free vectors](https://all-free-download.com/free-vector/) | copyright [BSGStudio](http://buysellgraphic.com/)

- From media directory
	- all product images - [bakerross](https://www.bakerross.ie/)
	- [park-guell-887725_1920-min](https://pixabay.com/fr/photos/parc-guell-mosa%C3%AFque-carreau-gaudi-887725/) - [Pixabay](https://pixabay.com/) | copyright [LisaRedfern](https://pixabay.com/fr/users/lisaredfern-910282/)
	- [uzbekistan-196875_1920-min](https://pixabay.com/fr/photos/ouzb%C3%A9kistan-mosa%C3%AFque-mod%C3%A8le-196875/) - [Pixabay](https://pixabay.com/) | copyright [LoggaWiggler](https://pixabay.com/fr/users/loggawiggler-15/)
	- [mosaic-200866_1920-min](https://pixabay.com/fr/photos/mosa%C3%AFque-carreau-art-c%C3%A9ramique-200866/) - [Pixabay](https://pixabay.com/) | copyright [GLady](https://pixabay.com/fr/users/glady-768/)
	- [graffiti-wall-1209761_1920-min](https://pixabay.com/fr/photos/mur-de-graffiti-graffiti-1209761/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [pexels-shukhrat-umarov-2103127-min](https://www.pexels.com/photo/child-sipping-from-pipe-graffiti-2103127/) - [Pexels](https://www.pexels.com/) | copyright [Shukhrat Umarov](https://www.pexels.com/@shukran)
	- [eyasu-etsub-JlufluFHiZc-unsplash-min](https://unsplash.com/photos/JlufluFHiZc) - [Unsplash](https://unsplash.com/) | copyright [Eyasu Etsub](https://unsplash.com/@jphotography2012)
	- [nasim-keshmiri-cdXwe6nROs8-unsplash-min](https://unsplash.com/photos/cdXwe6nROs8) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [fallon-michael-DWjucw3fsaQ-unsplash-min](https://unsplash.com/photos/DWjucw3fsaQ) - [Unsplash](https://unsplash.com/) | copyright [Fallon Michael](https://unsplash.com/@fallonmichaeltx)
	- [nasim-keshmiri-CQ3xrqbV58s-unsplash-min](https://unsplash.com/photos/CQ3xrqbV58s) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [nadia-clabassi-9EiJn8OJ8wo-unsplash-min](https://unsplash.com/photos/9EiJn8OJ8wo) - [Unsplash](https://unsplash.com/) | copyright [Nadia Clabassi](https://unsplash.com/@foifezza)
	- [elsa-lilja-xlkuA0VQshU-unsplash-min](https://unsplash.com/photos/xlkuA0VQshU) - [Unsplash](https://unsplash.com/) | copyright [Elsa Lilja](https://unsplash.com/@elsa_lilja)
	- [pexels-khairul-nizam-16516-min](https://www.pexels.com/photo/doodle-comic-art-sketch-16516/) - [Pexels](https://www.pexels.com/) | copyright [khairul nizam](https://www.pexels.com/@niezam)
	- [embroidery-942255_1920-min](https://pixabay.com/fr/photos/broderie-travaux-d-aiguille-942255/) - [Pixabay](https://pixabay.com/) | copyright [bluemorphos](https://pixabay.com/fr/users/bluemorphos-1137133/)
	- [pexels-anete-lusina-4792086-min](https://www.pexels.com/photo/toy-bear-and-thread-on-table-in-room-in-daytime-4792086/) - [Pexels](https://www.pexels.com/) | copyright [Anete Lusina](https://www.pexels.com/@anete-lusina)
	- [paint-4105253_1920-min](https://pixabay.com/fr/photos/peinture-peinture-acrylique-art-4105253/) - [Pixabay](https://pixabay.com/) | copyright [stux](https://pixabay.com/fr/users/stux-12364/)
	- [mosaic-200868_1920-min](https://pixabay.com/fr/photos/mosa%C3%AFque-carreau-art-c%C3%A9ramique-200868/) - [Pixabay](https://pixabay.com/) | copyright [GLady](https://pixabay.com/fr/users/glady-768/)
	- [nasim-keshmiri-o7IsP-DbIgk-unsplash-min](https://unsplash.com/photos/o7IsP-DbIgk) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [nasim-keshmiri-lUvvRj2RzK0-unsplash-min](https://unsplash.com/photos/lUvvRj2RzK0) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [pexels-anni-roenkae-5278835-min](https://www.pexels.com/photo/art-creative-pattern-purple-5278835/) - [Pexels](https://www.pexels.com/) | copyright [Anni Roenkae](https://www.pexels.com/@anniroenkae)
	- [pexels-anni-roenkae-2832382-min](https://www.pexels.com/photo/photo-of-multicolored-illustration-2832382/) - [Pexels](https://www.pexels.com/) | copyright [Anni Roenkae](https://www.pexels.com/@anniroenkae)
	- [6367436537_e49503a3f0_b-min](https://www.flickr.com/photos/earthafricacurio/6367436537/) - [Flickr](https://www.flickr.com/) | copyright [Ian Nicholson](https://www.flickr.com/photos/earthafricacurio/)
	- [12517089325_f4eca23e67_k-min](https://www.flickr.com/photos/paullew/12517089325/) - [Flickr](https://www.flickr.com/) | copyright [Lawrence OP](https://www.flickr.com/photos/paullew/)
	- [111294390_33b9db4816_b-min](https://www.flickr.com/photos/hundreds/111294390/) - [Flickr](https://www.flickr.com/) | copyright [max_thinks_sees](https://www.flickr.com/photos/hundreds/)
	- [17888752_1562ec72fe_b-min](https://www.flickr.com/photos/3sth3r/17888752/) - [Flickr](https://www.flickr.com/) | copyright [3sth3r](https://www.flickr.com/photos/3sth3r/)
	- [toa-heftiba-D9EgMp2V85o-unsplash-min](https://unsplash.com/photos/D9EgMp2V85o) - [Unsplash](https://unsplash.com/) | copyright [Toa Heftiba](https://unsplash.com/@heftiba)

Back to [top](#tableOfContents)

---

### Code <a name="code"></a>

- Environment variables - [Igor Basuga](https://github.com/bravoalpha79) Tutor at [Code Institute](http://codeinstitute.net)
- Environment variables - Code Institute archive resources
- Ngrok - [ngrok](https://ngrok.com/)
- Using ngrok on Windows-10 - [youtube](https://www.youtube.com/watch?v=9gaaVbX0USI&ab_channel=ChuckSeverance)
- Testing our Django App to be publicly accessible using NGROK - [medium](https://medium.com/@iot24hours/testing-our-django-app-to-be-publicly-accessible-using-ngrok-9b73851c46e0)
- jQuery documentation - [jQuery](https://jquery.com/)
- Favicon in django app - [stack overflow](https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app)
- Material Design for Bootstrap documentation - [mdbootstrap](https://mdbootstrap.com/)
- How to integrate mdbootstrap with django - [mdbootstrap](https://mdbootstrap.com/articles/jquery/how-to-integrate-mdbootstrap-with-django/)
- mdbootstrap input number [mdbootstrap](https://mdbootstrap.com/docs/jquery/forms/inputs/)
- Creating a modal image gallery with bootstrap components - [css tricks](https://css-tricks.com/creating-a-modal-image-gallery-with-bootstrap-components/)
- How to - Portfolio Gallery with Filtering - [w3schools](https://www.w3schools.com/howto/howto_js_portfolio_filter.asp)
- Portfolio Filter Gallery HTML CSS & JavaScript | Image Category Filtering [web dev trick](https://webdevtrick.com/portfolio-filter-gallery/)
- How to - Lightbox - [w3schools](https://www.w3schools.com/howto/howto_js_lightbox.asp)
- Material Design Full Screen Modal - [mdbootstrap](https://mdbootstrap.com/snippets/jquery/mustafaozkaya/789907#html-tab-view)
- How to change your commit messages in Git? - [github](https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4)
- How to limit the maximum value of a numeric field in a Django model? [stack overflow](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- Python perform append at beginning of list - [geeksforgeeks](https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/)
- How to upload files with django - [simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)
- How to crop an image in css - [educative](https://www.educative.io/edpresso/how-to-crop-an-image-in-css)
- Set favicon in django admin - [stack overflow](https://stackoverflow.com/questions/34959897/set-favicon-in-django-admin)
- Change the display format of time fields - [stack overflow](https://stackoverflow.com/questions/7216764/in-the-django-admin-site-how-do-i-change-the-display-format-of-time-fields)
- Automatic datetime fields - [simple is better than complex](https://simpleisbetterthancomplex.com/tips/2016/05/23/django-tip-4-automatic-datetime-fields.html)
- Delete a git commit but keep the changes [stack overflow](https://stackoverflow.com/questions/15772134/can-i-delete-a-git-commit-but-keep-the-changes)
- You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path - [stack overflow](https://stackoverflow.com/questions/48455469/youre-using-the-staticfiles-app-without-having-set-the-static-root-setting-to-a)
- Python django error oserror winerror 123 the filename directory name or vol - [stack overflow](https://stackoverflow.com/questions/56166319/python-django-error-oserror-winerror-123-the-filename-directory-name-or-vol)
- Modify Title and Header Django Admin Interface - [medium](https://adiramadhan17.medium.com/modify-title-and-header-django-admin-interface-a6ad6e470d92)
- Customizing HTTP error web pages 404, 500, 403 and 400 in Django - [lavatech technology](http://lavatechtechnology.com/post/customizing-http-error-web-pages-404-500-403-and-400-in-django/)
- Equivalent of export command in Windows - [superuser](https://superuser.com/questions/1500272/equivalent-of-export-command-in-windows)
- Heroku Django Deploy Stripe Issue - No module named 'stripe' - [stack overflow](https://stackoverflow.com/questions/51509121/heroku-django-deploy-stripe-issue-no-module-named-stripe/51509169)
- Readme file information - [Tim Nelson](https://github.com/TravelTimN) Software Developer and Tutor at [Code Institute](http://codeinstitute.net)
- How to Rename a Local Branch in Git - [git tower](https://www.git-tower.com/learn/git/faq/git-rename-branch/)
- Sending email [django](https://docs.djangoproject.com/en/3.2/topics/email/)
- BadHeaderError with Python emails package, how to fix? [stack overflow](https://stackoverflow.com/questions/55903845/badheadererror-with-python-emails-package-how-to-fix)

Back to [top](#tableOfContents)

---

### Acknowledgements <a name="acknowledgements"></a>

- [Anthony Ngene](https://github.com/tonymontaro)
	- Thanks to my Code Institute mentor for his time, suggestions, constructive feedback and availability.  
- CI Tutor support for their help in order to understand some issues and their friendliness.

Back to [top](#tableOfContents)

---
