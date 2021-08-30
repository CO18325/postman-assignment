## Public APIs List Crawler - Assignment - Inderpreet Singh
<hr>

<!-- TABLE OF CONTENTS -->

## Table of Contents
- [Project Statement](#problem-statement)
- [About the Project](#about-the-project)
  - [Technical Stack](#technical-stack)
- [Database Schema](#database-schema)
- [Getting Started (Instructions)](#getting-started)
  - [Crawler](#crawler-program)
  - [Flask App](#flask-web-portal)
- [Further Improvements](#further-improvements)
- [Output Snapshots](#output-images)
- [References](#references)

<!-- Project Breakdown -->
## Problem Statement
<hr>

On the landing page of the above repo, you can see some list of categories for e.g. Animals, Art & Design, Business etc.

In the next section you can find some API details for each one of the categories for e.g. under Animals section we have 
API:  Cat Facts, Link: https://alexwohlbruck.github.io/cat-facts/
Description: Daily cat facts, Auth: No, HTTPS: Yes, CORS: No

We need to crawl the above list of all APIs and store it in a database. You can find the public API here with Postman documentation. Do not use any other APIs or scraping method to get the data. 
Note: You just need to fetch and store a list of all API in the database and NOT data from each API.

<!-- ABOUT THE PROJECT -->

## About The Project
<hr>

Based on the problem statement. Two modules are built:

- A python program to scrap all the data and save it in a relational database.
- A Flask based basic web prtal to display all the data stored in the database.

### Technical Stack
- Python 
- SQL (SQLite)
- Flask & Basic Frontend



## About The Project
<hr>

Following obectives were achieved<br>
- **Number of Categories Crawled: 45**
- **Number of APIs Crawled: 525** 
- **Support for handling authentication requirements & token expiration of server** :<br> 
Multi-Threading was used to ensure that the the token is regenerated. The maximum time a session could be active is 300 seconds. Thus, after every 250 seconds a new token is generated to avoid any error in response from postman api. 
- **Support for pagination to get all data** :<br>
Based on the **count** parameter, the number of apis per category was available. A single page consisted of 10 entries. Thus, a loop was made for **ceil(count)** number of pages. In this way all the pages were crawled.
- **Develop work around for rate limited server** :<br>
The server api call was limited to 10 requests in a minute. Thus, we need to ensure that the program only make 1 request in 6 seconds. Thus, after every API call, the program is on sleep mode for 6 seconds. Since, multithreading is used, this sleep doesn't have any effect on the token regeneration process.

- **Crawled all API entries for all categories and stored it in a database** :<br>
With the logic for pagination and limited server, the program was able to crawl over all the apis. Each api was further saved in SQL databse. SQLite is used for the interaction with python program. Schema of database is defined in detail in further section.**No data of the api was stored in the Database as mentioned in the assigment**

- Optimal Object Oriented Program Structure Not Achieved

<br>

## Database Schema
<hr>

- Relation Database is used in this project. Two tables are formed, one for the categories and one for the products. 
- Coded Schema could be found in the file  **schema.sql**.
- The constructor of the **Database Class** recreates the database. So, to recreate the databse you just need to call the object of the Databse class.<br>

### category Table
id                      | category_name
-------------           | -------------
INTEGER                 | TEXT
PRIMARY (AUTOINCREMENT) | NOT NULL

This table will consist of all the names of the categories.<br>

## products Table
prod_id                 | category      | apiName       | link 
-------------           | ------------- | ------------- | -------------
INTEGER                 | INTEGER       | TEXT          | TEXT
PRIMARY (AUTOINCREMENT) | NOT NULL      | NOT NULL      | NOT NULL

This table will consist of all the APIs. The category in this the id from the category table. Thus, **category acts as a foreign key**. id is used against the catgory_name, as it saves memory and integer processing is more efficient the text processing. 


## Getting Started
<hr>

Follow the following steps to run the crawler. And visit the web portal link to view the flask app 

```
Pre-requiste : Python 3 should be installed on your Computer
```
<br>

### Crawler Program
All the relevant data for the crawler program is in the crawler directory



```
git clone https://github.com/CO18325/postman-assignment.git
pip install -r requirements.txt
python crawler/crawler.py

```
Data will be saved in database1.db when the crawler is initiated.

<br>

### Flask Web Portal

Please review the website deployed on Heroku:<br>
**https://postmantestinderpreet.herokuapp.com/**<br>
This flask app displays all the APIs from various categories in a web portal. <br>


To run the App on Local Computer

```
git clone https://github.com/CO18325/postman-assignment.git
pip install -r requirements.txt
flask run
```





<br>

## Further Improvements
<hr>

- Further better developed Object Oriented Program. Current system cannot be considered completely under OOP.
- Better Web UI Interface to view the stored database
- More optimized technique to work around the server limitation and token regeneration
- GUI Interface for Scrapper


<br>




## OUTPUT IMAGES
<hr>

### START OF THE CRAWLER

![GitHub Logo](/output_images/initialize_crawl.png)

### TOKEN REGENERATION

![GitHub Logo](/output_images/Token_Renewal.png)

### END OF CRAWLER

![GitHub Logo](/output_images/last_cat_res.png)


### FLASK APP HOME PAGE

![GitHub Logo](/output_images/flask-intro.png)

### FLASK APP SINGLE CATEGORY RESULT

![GitHub Logo](/output_images/single_category.png)

<br>

## References
<hr>

- https://documenter.getpostman.com/view/4796420/SzmZczsh?version=latest#intro
- https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
- https://getbootstrap.com/docs/4.1/content/tables/#hoverable-rows
- https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/
- https://www.nylas.com/blog/use-python-requests-module-rest-apis/


