# PROJECT TITLE: NewEgg Scrapper
## Video Demo:  https://youtu.be/thGjLkWSwMU
## Github Repo: https://github.com/ApostolosVarvatis/CS50P-Final-Project
## Description
My final project for CS50P is a terminal-based web scrapper (developed locally in vs code and saved in the cloud using git and GitHub) using Python (3.11.2) and the Beautiful Soup (4.12.2) library!

## Usage

- My software is a web scrapper that gathers real-time information on any item requested on NewEgg such as PC parts, laptops, and electronic devices.
  It has two main options. The basic search efficiently displays the top 4 best-selling products of your query with their current pricing and the advanced search, that lets the user customize your search with a limit of how many results you want to be displayed and the order in which you want to sort them by. It also provides you with the current pricing of each product as well as a link to NewEgg's website for more information!

- When you first run the app using 'python project.py' you are introduced to the main menu. There you can see the three main options for [0]Exiting the program, [1]Basic searching, and [2]Advanced searching.
  The menu fully supports error checking for 'user misbehavior' at all levels. It also supports re-prompting at the end of each query for additional querying!

- Choosing option [0] effectively quits the program with an error message displayed.

- Choosing option [1] starts the basic search by prompting the user for an item. Then it automatically sets the displayed result limit to '4' and the sort order to 'Best Selling'.
  Immediately after, it creates an HTML file ("newegg.html") identical to NewEgg's website to further analyze data if the user wants to. Following comes the data, first by price in dollars and then by name.
  
- Choosing option [2] starts the advanced search by prompting the user for an item. Then the program proceeds by prompting again, for the limit and the sort order the user wants the items to be displayed.
  Pressing Enter on both prompts sets the basic search deafults. The options for the item sorting are displayed in a menu for more readability. Subsequently, the data are displayed first by price, then by name, and then with the NewEgg URL for the product.

- After option [1] or [2] the program re-prompts with the main menu again for additional querying if wanted.

- That's it! You can now search for any item, compare prices, reviews and make buying smarter!

## Contents

To begin with, my project contains a main folder called project in the root of the directory:

- The project.py file is the main Python file of the project. It contains all the Python code written for the program to work.

- The requirements.txt file lists all the modules that need to be downloaded with pip for the application to function correctly.

- Then the newegg.html that is created when you do your first query and contains all the HTML code from your latest search either basic or advanced!

- Next, the test_project.py file is a file used to test the correctness of the project.py file. It can be used with pytest to ensure that the functions of project.py work as intended.

- And lastly, this README.md file that tries to best explain this project!


All in all, I am proud of my final project and my progress all these weeks and I want to thank, one last time, the CS50 team, for this amazing experience!

# THANK YOU CS50P!