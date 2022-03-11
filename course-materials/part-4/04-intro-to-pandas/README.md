# Intro to Pandas

<!-- 
## Learning Objectives

*After this lesson, you will be able to:*

* Use Pandas to read in a dataset
* Investigate a dataset's integrity
* Understand the basic data types of Pandas: DataFrames and Series
* Filter, sort, and manipulate DataFrames and Series

---

-->

# What is Pandas?

![](https://media.giphy.com/media/EatwJZRUIv41G/giphy.gif)

* A kind of adorable bear :panda_face::panda_face::panda_face:
* But also... a Python library for data manipulation and analysis

## So, Pandas the Library

The Swiss Army Knife of data manipulation!

Pandas:

* Is *the* library for exploratory data analysis (EDA)
* Formats, wrangles, munges, cleans, and prepares our data
* Replace many things we know how to do in Excel

With Pandas, you can:

* Produce code so that your steps are reproducible
  * How many times have you seen a spreadsheet where nobody understands what's going on in there?
* Can exceed 1M rows and 16K columns, unlike [Excel](https://support.office.com/en-us/article/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3)!
  * Older versions of Excel could only handle 64K rows!
  * Ugh: [Excel: Why using Microsoft's tool caused Covid-19 results to be lost](https://www.bbc.com/news/technology-54423988)

Some basics:

<!--
* An open source project to analyze [Panel Data](https://en.wikipedia.org/wiki/Panel_data) (hence "Pandas") by [Wes McKinney](https://en.wikipedia.org/wiki/Wes_McKinney)
-->

* A "panel" is the name of the Pandas object which can hold an n-dimensional array of data
* Don't let the word intimidate you, a panel is basically the same thing as an excel table
* A 2-dimensional panel is called a `DataFrame` (rows and columns)
* A 1-dimensional panel is called a `Series` (just a single column)
* Pandas is run from within Jupyter Notebooks

## Exploratory Data Analysis (EDA)

Pandas is used for **Exploratory Data Analysis** -- the process of understanding our dataset and producing our first level of insights.

In this introductory course, we will focus on the most 'mission critical' elements of EDA, including:

* Reading in data: "Import the data about the cat population"
* Checking data types: "Is the population count in integers? You can't have 2.5 cats"
* Renaming columns: "`cat_breed` is easier to work with than typing `Biological Family` all the time"
* Joining together data: "Combine the US cat population data with the Canadian set of cat population data"
* Looking for missing data: "Hey, the data doesn't mention anything about Sphynx cats!"
* And more!

![](assets/sphynx.jpg)

<!--
In this lesson, we'll use Pandas to:

* Read in a dataset
* Investigate a dataset's integrity
* Filter, sort, and manipulate a `DataFrame` and its columns (`Series`)

Before we begin: Hypothesis-driven EDA is essential to productive EDA -- otherwise we will ceaselessly torture our data for answers.
-->

We'll start down the road to learning these today.

---

# Example Dataset - Adventure Works Cycles Products

For today's Pandas lesson, we will be using data for a company known as [Adventure Works Cycles](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks) (AWC), a manufacturer and seller of bicycles and accessories.

AWC is actually a fictional company developed by Microsoft for training purposes, for its Microsoft SQL Server **relational database** software. Enterprise companies in the real world universally store their data in databases, and the data we're looking at is actually exported from a database.

* Only a single table from this database: The **Products** table
* Contains information on products the company makes
   * Product names
   * Product lines information
   * Prices
   * The product weights, measures
   * ...etc
* (The data has been slightly cleaned up and modified for the purposes of this class, but is essentially the same as the original.)

We'll be working with this, and other tables in the future. As we join more tables together, we'll uncover more information about this business.

As we go through this exercise, think about your own work experience at different companies and how these ideas might apply to you!

## Data Dictionary

Let's take a closer look at the **Product** table.

The following table is a description of the fields (columns) of the table. This is known as a **Data Dictionary**.

| Field | Description
| :--- | :---
| **ProductID** | Primary key for Product records
| **ProductSubcategoryID** | Product is a member of this product subcategory. Foreign key to the ProductSubcategory table.
| **Name** | Name of the product
| **ProductNumber** | Unique product identification number
| **ProductLine** | R = Road, M = Mountain, T = Touring, S = Standard
| **Class** | H = High, M = Medium, L = Low
| **Style** | W = Womens, M = Mens, U = Universal
| **Color** | Product color
| **StandardCost** | Standard cost of the product
| **ListPrice** | Selling price
| **Size** | Product size
| **SizeUnitMeasureCode** | Unit of measure for the Size column
| **Weight** | Product weight
| **WeightUnitMeasureCode** | Unit of measure for the Weight column
| **MakeFlag** | 0 = Product is purchased, 1 = Product is manufactured in-house.
| **FinishedGoodsFlag** | 0 = Product is not a salable item. 1 = Product is salable
| **SellStartDate** | Date the product was available for sale
| **SellEndDate** | Date the product was no longer available for sale
| **DiscontinuedDate** | Date the product was discontinued
| **ModifiedDate** | Date and time the record was last updated

([Original Source from Microsoft](https://www.sqldatadictionary.com/AdventureWorks2014/Production.Product.html))

## Discussion: What Could We Examine?

Now that you know what the data contains, what are some potential insights you think you would be able to uncover?

## Data Integrity: The Clean Truth about Dirty Data

The first thing we typically check with any data set, to assure our data can be trusted to produce meaningful insights.

* Our data must have correctly formatted data types: "Decimals should be floats, not strings"
* Our data should not have missing chunks: "Why do we only have half a year of data?"
* Dealing with data integrity isn't a one-stop step
* Much like EDA itself, it's an ongoing process!
* We will uncover additional potential problems and anomalies to fix along the way

---

# To the Notebook!

It turns out that we can run Pandas inside a Jupyter Notebook!

We will now proceed to the Jupyter Notebook for this lesson.

You can locate it inside your Kaggle account under <kbd>Code</kbd> :arrow_right: <kbd>Your Work</kbd> :arrow_right: <kbd>Shared With You</kbd>

You won't be able to make changes to that notebook (as it's the instructor's copy).

So, once you have it open, click the <kbd>Copy and Edit</kbd> button (upper right hand corner) to make a copy of the notebook, so that you can make changes to it!

---

# Additional Resources

* Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/)

<!--

* DataSchool [30-video series](http://www.dataschool.io/easier-data-analysis-with-pandas/) (by a former GA instructor!)

---

# Folder Structure

From now on, notice that each lesson will have a:

* `.python-version` hidden file, which specifies the version of Anaconda we are using
* `data` folder, which will contain spreadsheet(s) of data that we will use for analysis
* `assets` folder, where I will place some supporting graphics

You will not need to mess with any of these files folders, and will continue to work in the `student` folder, while I work in the `instructor` folder.

Note that these `data`/`assets` folders have also been provided with shortcuts (symbolic links) in the `student`/`instructor` folders, so we are all working off of the same data source!

Now that we're fledgling data scientists, we'll work launch and work directly in the Jupyter Notebook!

The `.ipynb` file you will open is called `intro-to-pandas.ipynb`.

Go into your `student` folder and execute:

```zsh
jupyter notebook intro-to-pandas.ipynb
```
-->
