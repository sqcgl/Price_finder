# Final Project Report

* Student Name: Fan Chen
* Github Username: sqcgl
* Semester: FW23
* Course: CS5001



## Description 
I developed the 'price_finder' project to streamline the process of checking product prices for different customers. Working in a wholesale company, I frequently encounter varying prices for items depending on the customer. This program is aimed at easing the invoice creation process by quickly retrieving and displaying the last three purchased products for a specific customer from an Excel sheet exported from QuickBooks.


## Key Features
Customer-Centric Pricing: Allows the user to find prices based on customer names.<br>

Product Price Retrieval: Fetches and displays the last 3 purchased products for a customer.<br>

Excel Integration: Utilizes the 'openpyxl' library to interact with Excel files, enabling easy data extraction.<br>

User-Friendly Interface: Offers a simple command-line interface for easy interaction.

## Guide
Running the Project

### Launch the Program:
  Run the Python script price_finder.py in your terminal or preferred Python environment.

### User Menu:
Upon running the program, a menu will be displayed:<br>

```
Currently open workbook: test.xlsx
Welcome:
check price: -c
change workbook: -wb
quit: -q
What would you like to do?
```

Use the following commands to navigate the menu:<br>
- -c: Allows you to check prices by entering customer names and product queries.<br>
- -wb: Enables changing the active Excel workbook by entering a new workbook path.<br>
- -q: Quits the program and closes the workbook.<br>

### Check Price (-c Option):
1. Enter -c to check prices.<br>
2. Input the customer's name when prompted.<br>
3. Enter the product names or type done to conclude product entries.<br>
4. The program will display the last three purchased products for the specified customer.<br>

### Change Workbook (-wb Option):
1. Use -wb to change the active Excel workbook.<br>
2. Enter the new workbook file path when prompted.<br>
3. The program will switch to the specified workbook for further operations.<br>

### Quit (-q Option):
1. Input -q to exit the program gracefully.<br>
2. The workbook will be closed, and the program will terminate.<br>

## Installation Instructions
### Install Required Library:
Ensure you have Python installed on your system.<br>
Install the 'openpyxl' library by executing the following command:<br>
```
pip install openpyxl
```
### Excel File Preparation:
You can use the provided test file ('test.xlsx') or prepare your Excel file from QuickBooks.<br>

For QuickBooks users:<br>
1. Export the "Sales by Customer Detail" report as an Excel file.<br>
2. Adjust the Excel columns to match the project requirements:<br>
 - Delete Column A (Customer Column)
 - Delete Column D (Transaction Type)
 - Delete Column C (Invoice Number)
 - Delete Columns J and K (Amount Line and Balance)
3. Alternatively, adjust the column references in the code to match your Excel file's structure.<br>

### Running the Program:
1. Clone the repository or download the 'price_finder.py' file.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the Python script price_finder.py.
```
python price_finder.py
```
### Interacting with the Program:
Follow the menu prompts (-c, -wb, -q) to navigate the program.
- Use -c to check prices for specific customers and products.
- Use -wb to change the active Excel workbook by providing a new file path.
- Input -q to exit the program.

### Adjusting Excel Columns (if needed):
If you've used a different Excel file structure, adjust the column references in the code:
- Modify the CUSTOMER_COLUMN, PRODUCT_COLUMN, PRICE_COLUMN, QTY_COLUMN, UNIT_COLUMN, and DATE_COLUMN variables in the code to match your Excel file's column positions.<br>

### Input Data Requirements:
Ensure that the Excel file used contains relevant customer and product information to retrieve prices accurately based on user inputs.

## Code Review

### get_info() Function:
Purpose: Retrieves detailed information about a product from the Excel sheet.
```python
def get_info(product_name, row, product):
    '''
    Function get_info:
    Retrieves information about a product.
    Args:
        product_name(str): The name of the product.
        row(str): The row where the product information is located.
        product(str): The product information.
    Returns:
        info(str): Information about the product.
    '''
    # Extracts product details such as customer, price, quantity, unit, and date
    # Constructs and returns a formatted string containing product information
```
Key Points:
- Extracts data from specified columns corresponding to the product.
- Formats the retrieved information into a string.
- Provides details about the product, including customer, price, quantity, unit, and date.

### find_price_for_all_products() and find_price_for_customer() Functions:
find_price_for_all_products() Purpose: Locates prices for a specific product across all customers.<br>

find_price_for_customer() Purpose: Finds prices for a specific product for a given customer.<br>

```python
def find_price_for_all_products(product_name):
    '''
    Function find_price_for_all_products
    Finds prices for a specific product across all customers.
    Args:
        product_name(str): The name of the product.
    Returns:
        price_list(list): List containing product info for all customers.
    '''
    # Searches for prices of a particular product across all customers
    # Uses get_info() to gather product details
    # Constructs and returns a list containing information of the product for all customers
```

```python
def find_price_for_customer(customer_name, product_name):
    '''
    Function find_price_for_customer
    Finds prices for a specific product for a given customer.
    Args:
        customer_name(str): The name of the customer.
        product_name(str): The name of the product.
    Returns:
        price_list(list): List containing product info for the customer.
    '''
    # Searches for prices of a specific product for a given customer
    # Uses get_info() to gather product details
    # Constructs and returns a list containing information of the product for the customer
```
Key Points:
- Utilizes get_info() to gather specific product information.
- Constructs and returns a list containing product information based on the search criteria (all customers or a specific customer).

### find_price() Function:
Purpose: Gathers and prints the last three purchased products' details for the specified customer based on user input.

```python
def find_price(customer_name, product_names):
    '''
    Function find_price
    Finds prices for specific products and customers.
    Args:
        customer_name(str): The name of the customer.
        product_names(list): List of product names.
    Returns:
        None
    '''
    # Orchestrates find_price_for_all_products() or find_price_for_customer() based on user input
    # Gathers and prints the last three purchased products' details for the specified customer
```

Key Points:
- Based on user input, choose between searching for prices for all customers or a specific customer.
- Retrieves the last three purchased product details using find_price_for_all_products() or find_price_for_customer() and then prints them.

### Major Challenges
#### Challenges: Refactoring a huge Function into Smaller Functions

- Initial State: Initially, the code might have had a single large function responsible for tasks like retrieving product information, searching prices for all products across customers, finding prices for specific customers, and displaying results- .

- Refactoring Process: The challenge involved breaking down this huge function into smaller, more specialized functions, such as get_info(), find_price_for_all_products(), find_price_for_customer(), find_price(), and more. Each smaller function took on a specific responsibility related to its name, making the code modular and easier to comprehend.

#### Proud Aspects: Successfully restructuring the code into smaller functions that increased code clarity, readability, and maintainability. 

- Outcome: The refactored code comprised several smaller functions, each handling a specific task, leading to a more modular and maintainable codebase. This made future enhancements, bug fixes, and understanding of the code easier for developers.


## Example Runs
Video demo for price_finder.py:<br>
https://youtu.be/ZvHmQ3C1c0Q<br>

Key Aspects:
- Utilizes openpyxl for Excel file handling.
- Modular design with functions for different tasks.
- Validates customer existence in the Excel sheet.

## Testing
### Testing Approach:
#### Automated Testing:
- Test Program: Developed a comprehensive test program covering each function within the code.
- Purpose: Systematically validates the functionality of every function and method.
- Result: Ensures that each function performs as expected and handles various scenarios correctly.
#### Manual Testing:
- Real-world Usage: Actively using the program for daily tasks, creating over 50 invoices daily.
- Purpose: Verifies the program's performance, reliability, and stability in a production environment.
- Result: No errors observed during manual usage, indicating the program's stability and suitability for real-world usage scenarios.
#### Outcome:
- Successful Functionality: All functions have been systematically tested through an automated test program, ensuring their correctness and reliability.
- Real-world Application: The program has been used extensively in daily tasks without encountering errors, proving its stability and suitability for production use.
- 
Added Testing (if necessary): Further tests can be added to the 'test_price_finder.py' file to cover more scenarios, edge cases, and potential areas for improvement.


## Missing Features / What's Next
### Integration with QuickBooks API:
- Missing Feature: Integration with QuickBooks API to fetch real-time data, ensuring up-to-date information retrieval directly from QuickBooks.
- Importance: Enhances the program's functionality by allowing real-time data updates without manual file imports.
- Future Development: Consider adding QuickBooks API integration to automate data retrieval for updated and current information.
### User Interface Enhancements:
- Missing Feature: Lack of user interface features to adjust columns or customize the number of prices displayed per item (currently set to 3).
- Potential Enhancement: Incorporate user settings to adjust column configurations and the number of prices displayed, providing user customization options.
- Future Development: Implement user-friendly adjustments directly accessible within the program's interface for enhanced flexibility.
### Time Constraints and Future Plans:
- Time Constraints: Limited time availability due to prioritizing code refactoring and function decomposition, preventing the addition of advanced features like API integration and UI enhancements.
- Future Consideration: Despite the current limitations, these features are easily adjustable within the codebase and can be included in future iterations or by contributors.

## Final Reflection
Creating this project was a rewarding experience as it marked my first meaningful application of programming skills to solve a real work-related challenge. It significantly reduced the time spent on daily invoicing tasks, saving at least 50% of my time compared to manual Excel checks. While Excel has a search function, finding specific products across multiple stores remained cumbersome, motivating me to create this tool.

Interacting with Excel through Python taught me valuable skills in breaking down complex functions. This project fulfills my goal of streamlining the invoicing process, improving efficiency, and minimizing errors. Although I couldn't integrate real-time data retrieval from QuickBooks due to time constraints, I aim to explore enhancements in the future.

Overall, this project has been an enlightening learning experience, blending programming knowledge with practical application, significantly benefiting my daily work tasks and exceeding my initial objectives.
