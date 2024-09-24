## Project Description

This project is a web application for renting hookahs for home use and events. The site offers various services such as hookah rentals, catering, and order and delivery address management. The platform includes user registration and authentication, product filtering, and a convenient payment system.


## Key Features:

### Authentication and Registration
 - User login and registration are implemented.
 - During registration, the user first enters their email and receives a confirmation code. This operation is handled through Redis.
 - After confirming the code, the registration process continues, and the user provides additional details.

### User Dashboard
 - Ability to add and edit email addresses.
 - Option to add and manage delivery addresses.
 - Viewing and adding delivery addresses is done through modal windows.
 - Unnecessary addresses can be deleted.
  
### Homepage:
From the homepage, users can navigate to the following sections:
- Services
- Contacts
- About Us
- Delivery
- Terms and Conditions
  

### Services: 
This section includes two key options: hookah rental for home and catering services.

**Home Rental**: 
  - For unregistered users, a full list of products (hookahs and tobacco) is available with filters by name and category (hookah/tobacco).
  - For tobacco, an additional filter by flavor is implemented.
  - Product details are available for viewing.
  - For registered users:
    - Ability to add products to favorites.
    - Filtering options within the favorites section.
    - When viewing a product or adding it to the cart, users can select the rental date and time (considering the company's operating hours).

**Catering**: 
  
- A form to fill in details such as the number of hookahs, rental hours, and the need for delivery.
- Real-time automatic cost calculation.
- Fields for entering contact details (phone, name, address).
- The form is submitted after all required information is filled in.

**Cart**:
- In the cart, users can increase or decrease the product quantity by ±1.
- If the product quantity reaches 0, the item is removed from the cart.
- Displays the total order cost.
- Checks if both a hookah and tobacco are in the cart before placing the order.
- If a product from one category is missing, a modal window is displayed when the user tries to place the order, requesting confirmation to proceed without the required product.

  
**Checkout Page**:
- On the checkout page, the user can select an existing delivery address or create a new one.
- Displays order details: all items selected by the user and the option to choose delivery method (pickup or delivery for an additional fee).
- The total cost is calculated based on the following parameters:
  - Order cost
  - Delivery cost
  - Hookah master's service fee
- The total order amount is displayed for user convenience.
- The user is also prompted to specify the number of guests in the pricing section.
- An additional service, "Hookah Master" (€10), can be added if desired.
  
**Payment**:
- The platform supports payment via credit card through the Stripe payment system.

# Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Postgresql, Redis
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

## Screenshots

### 1. Home Page:
A screenshot displaying the homepage of the site with the main menu and sections: "Services," "Contacts," "About Us," "Delivery," and "Terms."
![Home](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/main.png?raw=true)

### 2. Menu for Unregistered Users:
The menu for unregistered users. It shows the sections for "Rental," "Catering," and "Login."
![Unregistered](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/servishamb.png?raw=true)

### 3. Login Page:
A screen with the login form, containing fields for entering the username and password. There is also a button to register a new user.
![Login](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/login.png?raw=true)

### 4. Registration: Email and Code Input::
A registration page where the user enters their email and receives a confirmation code. It displays a field for entering the code and a button to submit it.
![Registration](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/regredis.png?raw=true)

### 5. Registration: Entering Other Details:
The next step of the registration process, where the user fills in additional information (name, password, and password confirmation) to complete the registration.
![Registration2](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/registr.png?raw=true)

### 6. User Dashboard:
The user’s profile displaying their email, added delivery addresses, and buttons to add new addresses or manage existing ones.
![User](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/user.png?raw=true)

### 7. Modal Window for Adding an Address:
A modal window with a form for adding a new delivery address. The fields include first name, last name, phone number, address, and a save button.
![Modal](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/modaladd.png?raw=true)

### 8. Modal Window for Viewing Addresses:
A window displaying all saved delivery addresses with the option to delete an address.
![Modal](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/modalliast.png?raw=true)

### 9. Services Page with Catering and Rental:
A page showcasing two main services: home hookah rental and catering. Each service has a button to access more detailed information.
![Services](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/serv.png?raw=true)

### 10. Catering Cost Calculation Form:
A page with a form where the user inputs the number of hookahs, rental hours, and selects if delivery is needed. Real-time cost calculation is displayed.
![Catering](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/keit.png?raw=true)

### 11. Rental Page with All Products and Filters:
A page listing all products (hookahs and tobacco), with filters for sorting by category (hookah/tobacco) and a search field for product names.
![Rental](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/list.png?raw=true)

### 12. Example of Tobacco Filters:
A page displaying the applied filters for tobacco flavors and a list of products matching the selected criteria.
![Filters](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/listfilt.png?raw=true)

### 13. Favorites:
A page displaying the applied filters for tobacco flavors and a list of products matching the selected criteria.
![Favorites](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/favorites.png?raw=true)

### 14. Product Detail Page with Date and Time Selection:
A detailed page for a specific product (e.g., a hookah), showing fields for selecting the rental date and time. There are buttons to add the product to the cart.
![Detail](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/%20detail.png?raw=true)
![Detail](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/detailtime.png?raw=true)

### 15. Cart:
A page displaying the items added to the cart, with the ability to adjust the quantity using "+" and "-" buttons. The total order cost and a button to proceed with the order are also shown.
![Cart](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/cart.png?raw=true)

### 16. Modal Window Warning if No Required Items in Cart:
A modal window that appears when attempting to place an order without items from one of the required categories (e.g., no tobacco). The window prompts the user to confirm proceeding without the necessary product.
![Modal](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/cartmodal.png?raw=true)

### 17. Checkout Page:
An order checkout screen displaying all the items in the order, options for delivery or pickup, the total order cost, a field to input the number of guests, and payment details.
![Checkout](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/checkout.png?raw=true)


### 18. Modal Window for Changing Delivery Address at Checkout:
A modal window that allows the user to select a different delivery address or add a new address during the checkout process.
![Modal](https://github.com/an-zhartun/an-zhartun/blob/images/screnhookah/checkoutadress.png?raw=true)
