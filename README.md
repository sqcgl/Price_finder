# Final Project Report

* Student Name: Fan Chen
* Github Username: sqcgl
* Semester: FW23
* Course: CS5001



## Description 
I developed the 'price_finder' project to streamline the process of checking product prices for different customers. Working in a wholesale company, I frequently encounter varying prices for items depending on the customer. This program is aimed at easing the invoice creation process by quickly retrieving and displaying the last three purchased products for a specific customer from an Excel sheet exported from QuickBooks.


## Key Features
Customer-Centric Pricing: Allows the user to find prices based on customer names.
Product Price Retrieval: Fetches and displays the last 3 purchased products for a customer.
Excel Integration: Utilizes the 'openpyxl' library to interact with Excel files, enabling easy data extraction.
User-Friendly Interface: Offers a simple command-line interface for easy interaction.

## Guide
Running the Project

Launch the Program:
  Run the Python script price_finder.py in your terminal or preferred Python environment.

User Menu:
  Upon running the program, a menu will be displayed:
     Welcome:
    check price: -c
    change workbook: -wb
    quit: -q
  Use the following commands to navigate the menu:
  -c: Allows you to check prices by entering customer names and product queries.
  -wb: Enables changing the active Excel workbook by entering a new workbook path.
  -q: Quits the program and closes the workbook.

Check Price (-c Option):
  Enter -c to check prices.
  Input the customer's name when prompted.
  Enter the product names or type done to conclude product entries.
  The program will display the last three purchased products for the specified customer.

Change Workbook (-wb Option):
  Use -wb to change the active Excel workbook.
  Enter the new workbook file path when prompted.
  The program will switch to the specified workbook for further operations.



## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

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
