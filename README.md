# Fake_Data_Generator_and_Github_Integration

<img src="https://github.com/user-attachments/assets/815162a2-3601-4ca4-a78e-059a1d3a76bd" alt="Sample Output" width="800"/>

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [How to Run the Script](#how-to-run-the-script)
4. [Sample Output](#sample-output)
5. [Video Walkthrough Link](#video-walkthrough-link)

## Project Overview
In the world of data science, high-quality datasets form the foundation for insightful analysis, model training, and system testing. However, when working with sensitive information, such as personal details, privacy becomes a critical concern. Due to real-world constraints like **data protection laws**, **ethical considerations**, and **privacy regulations**, access to actual user data is often restricted. This is where synthetic (fake) data becomes a powerful and safe alternative.
This project solves that problem by using the Faker library in Python to create fake profiles that include names, phone numbers, email addresses, job titles, and cities. 

These fake records can be used to:

- Test data pipelines without risking sensitive information

- Prototype and design software interfaces that expect user input

- Practice data analysis or machine learning workflows using structured but safe data

- Learn and demonstrate key programming skills like data generation, formatting, exporting to CSV, and documentation

- The dataset can be expanded, customized, and exported as needed, making it a flexible tool for developers, analysts, and data scientists who need sample data for demos, experiments, or learning environments.

This project gave me practical experience with:
- Python scripting
- Data cleaning and formatting
- Working with CSV files
- Version control with Git and GitHub
- Documenting a project from start to finish
- Presenting a technical walkthrough


## Setup Instructions
To run this project on your computer, you need to have Python installed along with a few necessary libraries. Don’t worry if you’re new to this. I have outlined each step clearly to make it easy to follow.
- Install Python
Make sure Python (version 3.10 or later) is installed. You can download it from https://python.org. During installation, check the option that says **“Add Python to PATH.”**
- Install Required Libraries
This project uses two main libraries: Faker and CSV (which comes built-in with Python). You will also use pandas for optional viewing, though it's not required to generate the data.
To install the required libraries, open your terminal (or command prompt) and run:

            pip install faker pandas

- Clone or Download the Project from GitHub
You can either clone this repository using Git:

            git clone https://github.com/your-username/fake-data-generator.git

Or you can go to the GitHub page and click “Download ZIP” to save the project on your computer.
-  Navigate to the Project Folder
Using the terminal, navigate to the folder where your Python script is saved:

            cd fake-data-generator

- Run the Python Script
Simply run the script using:

           python fake_data_generator.py

After running, a CSV file called fake_data.csv will be created in the same folder. This file contains the generated personal data, all cleaned and formatted.


## How to Run the Script
This project is designed to be simple and accessible, whether you're working in a traditional code editor or a Jupyter Notebook. Follow these steps to run the script and generate your own set of synthetic data:

- Open Your Code Editor
You can use any Python-friendly environment. This project was developed using Visual Studio Code (VS Code), but alternatives like PyCharm, Jupyter Notebook, or even a basic terminal will work just fine.

- Locate the Script
Look for the main Python file — typically named something like:

                fake_data_generator.py** for a script file

   or              
               
                 test_libraries.ipynb** if you're working in Jupyter Notebook

This file contains the full code that generates fake data, formats it, and exports it into a CSV file.

-  Run the Script
If you're using VS Code or a terminal, simply run:

                  python fake_data_generator.py
If you're using a Jupyter Notebook, click into each code cell and press **Shift + Enter** to run them one by one.

- View the Output
Once executed, the script will create a file named fake_data.csv in the same project folder. This file contains a list of fake individuals with the following fields:
 - Full Name
 - Phone Number
 - Email Address
 - Job Title
 - City

You can open this file using Excel, Google Sheets, or any spreadsheet tool to view the data in a structured table format. I prefer using Microsoft SQL Server to open the file.
You can also open the file in VS Code by typing in:
                 
                 import pandas as pd
                 df = pd.read_csv('fake_data.csv')
                print(df.head())  # Shows the first 5 rows


Kindly access the script <a href="https://github.com/mauree155/Fake_Data_Generator_and_Github_Integration/blob/main/main.py">Here</a> 

This is the <a href="https://github.com/mauree155/Fake_Data_Generator_and_Github_Integration/blob/main/data/fake_data.csv">Dataset</a>


## Sample Output
Below is a preview of what the generated fake dataset looks like after running the script. The data is randomly generated using the Faker library and formatted to resemble real-world information without compromising any actual identities.

![Sample_Output(fake_data)](https://github.com/user-attachments/assets/b7b7250b-5039-496f-b112-0c354a18449f)

- Phone Numbers: appear as plain numeric strings, making them easy to use for testing contact fields or validating data formats in applications.

- Names and Cities: The entries use global-style names and fictional city names. This reflects Faker’s default behavior, which is suitable when your goal is to simulate general-purpose data rather than location-specific profiles.

- Job Titles and Emails: These are varied, realistic, and helpful for testing workflows such as registration systems, HR platforms, or user profile analytics.

- Customizability: The number of records and the fields generated can easily be changed in the script. You can also switch Faker’s locale settings if you need more localized data for your specific region or audience.


## Video Walkthrough Link
Watch a quick demo of this project **here**


