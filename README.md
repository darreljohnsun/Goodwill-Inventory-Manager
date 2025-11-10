# Goodwill-Inventory-Manager

Goodwill-Inspired E-Commerce Inventory System



Role: Data \& Automation Developer

Tech Stack: Python, Pandas, SQLite, Jinja2, Git/GitHub, Optional AWS S3



Project Overview



This project simulates an e-commerce inventory management system inspired by second-hand retail operations like Goodwill. It automates the process of cleaning, validating, storing, and displaying product inventory data while demonstrating data engineering, automation, and cloud exposure skills.



The system:



Reads product data from a CSV file



Cleans and validates inventory records



Stores data in a local SQLite database



Generates an HTML product catalog for easy visualization



Optionally uploads database and HTML files to AWS S3



Key Features



Automated Data Processing: Removes duplicates, ensures valid stock and price values, and prepares data for storage.



Database Integration: Uses SQLite to store clean inventory data for easy querying and analysis.



Inventory Reporting:



Total stock across all products



Stock by category



Low-stock alerts (<5 units)



HTML Catalog Generation: Displays products with images, prices, and categories for quick online visualization.



Optional Cloud Deployment: Supports uploading files to AWS S3 for remote storage and access.



Version Control: Fully tracked with Git/GitHub for collaboration and portfolio showcase.



Sample Output



Terminal Output:



Cleaned Data:

&nbsp;  product\_id             name      category   price  stock                 image\_url

0           1        Blue Hoodie       Clothing  29.99     10  https://via.placeholder.com/100

1           2       Red Sneakers      Footwear  49.99      5  https://via.placeholder.com/100

2           3  Vintage Coffee Mug    Home Goods   9.99     20  https://via.placeholder.com/100

3           4       Leather Belt    Accessories  14.99     15  https://via.placeholder.com/100

4           5        Used Laptop    Electronics 199.99      3  https://via.placeholder.com/100



--- Inventory Summary ---

Total items in stock: 53



Stock by Category:

category

Accessories     15

Clothing        10

Electronics      3

Footwear         5

Home Goods      20

Name: stock, dtype: int64



Low Stock Alerts:

&nbsp;  product\_id        name  stock

1           2  Red Sneakers      5

4           5    Used Laptop      3





HTML Output:



Displays each product with its name, category, price, stock, and placeholder image.



Can be opened in any browser to simulate an online product catalog.



Getting Started

Prerequisites



Python 3.x



pip packages: pandas, jinja2, boto3 (optional for AWS S3)



Installation



Clone the repository:



git clone https://github.com/YOUR\_USERNAME/Goodwill-Inventory-Manager.git

cd Goodwill-Inventory-Manager





Create and activate a virtual environment:



python -m venv venv

venv\\Scripts\\activate   # Windows

\# source venv/bin/activate  # Mac/Linux





Install dependencies:



pip install pandas jinja2 boto3





Run the script:



python inventory\_manager.py





Open inventory.html in a browser to view the product catalog.



Project Highlights for Technical Applications



Data Engineering: Automated ETL-like process using Python and Pandas.



Automation: Scripted inventory validation and HTML generation.



Cloud Exposure: Optional AWS S3 integration demonstrates knowledge of cloud deployment.



Version Control \& Collaboration: Fully tracked with Git/GitHub.



Resume-Ready Skills: Python, SQL, SQLite, Automation, Git, Data Cleaning, Optional Cloud Deployment.



Future Enhancements



Add interactive filtering on HTML page (e.g., by category or price).



Add dynamic stock updates from CSV or user input.



Integrate real AWS S3 deployment and optional API for cloud-based product management.

