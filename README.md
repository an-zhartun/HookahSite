## Project Description

This project is a website for hookah rental, offering various features for users. It provides options for renting hookahs for home use and hookah catering services. The site includes several sections such as the homepage, services, contact information, company details, rental terms, and delivery.

Payments on the website are integrated with the Stripe payment system, ensuring secure and convenient transactions. Users can make payments for hookah rentals, delivery services, and hookah master services directly on the site using their credit cards.


## Main Sections of the Website:

### Homepage:
 The main entry point to the website, from which the user can navigate to other sections such as services, contact information, the "About Us" section, delivery, and rental terms.

### Services Section: 
This section includes two key options: hookah rental for home and catering services.

- **Catering**: 
  - The user can fill out a form to rent hookahs for catering, specifying the number of hookahs, hours, and whether delivery is needed.
  - Automatic cost calculation based on the selected parameters.
  - Filling in contact details (phone, name, address) to complete the order.

- **Home Rental**: 
  
  - **For unregistered users**:
    - A full list of products (hookahs and tobaccos) is available, with filtering options by name and category (hookah/tobacco). Tobacco products also have flavor-based filtering.
    - Ability to view product details.
  - **For registered users**:
    - Ability to add products to favorites, with filtering available in the favorites section.
    - Option to add products to the cart, select a rental date, and choose available time slots based on the company's working hours. 


- **Cart**:
  - Ability to change the quantity of products, add or remove items, and view the total order cost.
  - Checking for items from both categories (hookahs and tobaccos). If one is missing, a modal window pops up, warning the user and asking to confirm the absence of the product.
  - Option to proceed with the order without adding a product from a specific category.
  
- **Checkout Page**:
  - Choosing a delivery address from the saved ones or creating a new one.
  - Order details: all selected items, with the option to choose self-pickup or delivery with an additional charge.
  - Total cost calculation: order cost, delivery cost, hookah master's services, total 
  - Ability to specify the number of people (each will receive a free mouthpiece).
  - Payment via Stripe, providing a secure and convenient card payment option.


- **User Profile**:
  - Ability to edit the email address, add or delete delivery addresses.
  - Viewing all addresses with the option to edit or delete them, implemented through modal windows.


# Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Postgresql
- **Payment system**: Stripe
- **Authentication**: Django Authentication
- **Libraries**: SQLAlchemy, django-filter

<br><br><br>

# Instructions for running the project
## Steps to run the project

### 1. Cloning the repository
Clone the repository using the Git command:

```bash
git clone https://github.com/an-zhartun/HookahSite.git
```
### 2. Building Docker containers
```bash
docker-compose build
```

### 3. Starting the containers
```bash
docker-compose up
```
If you need to run the containers in the background, use the command:

```bash
docker-compose up -d
```

### 4. Opening the application

After the project has been successfully launched, the application will be available at the following address:

```bash
http://localhost:8000
```
### 5. Stopping the containers
```bash
docker-compose down
```
This command will stop all running containers and remove them, while preserving any data created in persistent storage (volumes).
#### To run the project, it is necessary to create a .env file.

<br><br>
