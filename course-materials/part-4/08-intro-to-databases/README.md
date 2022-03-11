# Intro to Databases

## Basic Database Theory

* Basic Database Theory will be demonstrated in the lesson.

## Joining 

* As you have seen, data in a database is [normalized](https://support.microsoft.com/en-us/help/283878/description-of-the-database-normalization-basics).    
   * When a database is *normalized*, it is structured in such a way that redundancy of data is minimized 
   * This allows a database to be faster, smaller, and more flexible when it comes time to change the data inside of it
   * Tables in a Database can be exported into `.csv` files that we can import into Pandas
* When a database is normalized, the data is contained within [tables](https://en.wikipedia.org/wiki/Table_(database)), related to each other by [keys](https://www.studytonight.com/dbms/database-key.php), or columns in one table that equal a column in another table, allowing them to be joined
* In a database system, joining is done with a language called SQL

## SQL

* Traditional Databases work with a language called SQL (Structured Query Language)

```sql
SELECT * FROM movies 
  INNER JOIN directors 
  ON movies.director_id = directors.id
```

* A SQL join statement looks like the above
* We can specify:
  * The tables to be joined to each other
  * _How_ the columns (keys) are related _to each other_ in the join
  * And other things like filtering, sorting, one-to-many/many-to-many joins
* SQL is out of the scope of this course -- Instead, we'll be calling functions and methods in Pandas to do joining

## Join Types

* There are different types of joins that are possible with database data. We'll only be interested in:
   * Inner Joins
   * Left Joins
   * Right Joins
* These will be demonstrated in the next lesson!

![](assets/join_types.jpg)
