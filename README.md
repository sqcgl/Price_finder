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

Welcome:<br>
check price: -c<br>
change workbook: -wb<br>
quit: -q<br>

Use the following commands to navigate the menu:<br>
-c: Allows you to check prices by entering customer names and product queries.<br>
-wb: Enables changing the active Excel workbook by entering a new workbook path.<br>
-q: Quits the program and closes the workbook.<br>

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
  pip install openpyxl<br>

### Excel File Preparation:
You can use the provided test file ('test.xlsx') or prepare your Excel file from QuickBooks.<br>
For QuickBooks users:<br>
Export the "Sales by Customer Detail" report as an Excel file.<br>
Adjust the Excel columns to match the project requirements:<br>
  Delete Column A (Customer Column)<br>
  Delete Column D (Transaction Type)<br>
  Delete Column C (Invoice Number)<br>
  Delete Columns J and K (Amount Line and Balance)<br>
  Alternatively, adjust the column references in the code to match your Excel file's structure.<br>

### Running the Program:
Clone the repository or download the 'price_finder.py' file.<br>
Navigate to the project directory in your terminal or command prompt.<br>
Run the Python script price_finder.py:<br>
python price_finder.py<br>

### Interacting with the Program:
Follow the menu prompts (-c, -wb, -q) to navigate the program.<br>
Use -c to check prices for specific customers and products.<br>
Use -wb to change the active Excel workbook by providing a new file path.<br>
Input -q to exit the program.<br>

### Adjusting Excel Columns (if needed):
If you've used a different Excel file structure, adjust the column references in the code:<br>
Modify the CUSTOMER_COLUMN, PRODUCT_COLUMN, PRICE_COLUMN, QTY_COLUMN, UNIT_COLUMN, and DATE_COLUMN variables in the code to match your Excel file's column positions.<br>

### Input Data Requirements:
Ensure that the Excel file used contains relevant customer and product information to retrieve prices accurately based on user inputs.<br>

##### Following these steps will enable you to install the necessary library, prepare the Excel file, and successfully run the 'price_finder' project for streamlined price retrieval based on customer queries and product information. Adjustments to the Excel file structure or code may be required based on your specific file format or preferences.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
