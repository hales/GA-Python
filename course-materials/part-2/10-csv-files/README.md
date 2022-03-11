# Working with CSV Files

We now know about the idea of **files**, as well as **modules and libraries**.

Python can handle regular text files on its own, but when it comes to special types of files, you'll need the assistance of a module.

There is one type of special file we'll work with in this course -- the `.csv` file. CSV stands for "Comma-Separated Values" and is a type of file used to represent tabular data -- i.e. data you would put in a spreadsheet.

There's nothing mysterious about CSV files -- they are just text files written in a very specific way, and have an extension of `.csv` instead of `.txt`.

CSV files look like this:

```
first_name,last_name
Baked,Beans
Lovely,Spam
Wonderful,Spam
```

The first line is the name of the **columns** of the table, and each subsequent line represents one row in the table.

If you open up this CSV file with a spreadsheet program (On a Mac, this is probably *Numbers*. On a PC, this is probably *Excel*), the table would look like this:

| first_name | last_name |
| --- | --- |
| Baked | Beans |
| Lovely | Spam |
| Wonderful | Spam |

Look how each cell is separated by commas in the CSV file!

## The `csv` Module

One of the modules available in the standard library is `csv`, which can be used to both **read** and **write** to these `.csv` files.

For reference, here is the [documentation on the `csv` module](https://docs.python.org/3/library/csv.html).

We are interested in the [`DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter) and [`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader) classes, which are available inside the `csv` module. (Notice the capital letters, which indicate that they are **classes**, as you know from the Object-Oriented Programming lesson!)

Because these classes are *inside* the `csv` module, to instantiate a new instance of a `DictReader`, for example, you would have to first `import csv` at the top of your program, and then write:

```python
my_reader = csv.DictReader(...)
```

or

```python
my_writer = csv.DictWriter(...)
```

(whereas recall that when we wrote our own `Cat` and `TeaCup` classes before, we didn't have to place a module name in front of the constructor function call):

```python
my_cat = Cat(...)
my_cup = TeaCup(...)
```

In the above, `...` are simply whatever arguments each constructor needs to instantiate a new instance of that class.

Let's first look at what `csv.DictWriter` can do for us, and then `csv.DictReader` later.

### `csv.DictWriter`

The `csv.DictWriter` class allows you to **write** the contents of dictionaries as lines in a CSV file.

Here's an example of how the DictWriter works.

Let's put this in a file called `dictwriter_example.py`, and let's read through, understand, and run the program now:

```python
import csv

FIELDNAMES = ['first_name', 'last_name']
names_file = open('names.csv', 'w', newline='')

writer = csv.DictWriter(names_file, FIELDNAMES)
writer.writeheader()

dict1 = { 'first_name': 'Baked', 'last_name': 'Beans' }
writer.writerow(dict1)
dict2 = { 'first_name': 'Lovely', 'last_name': 'Spam' }
writer.writerow(dict2)
writer.writerow({ 'first_name': 'Wonderful', 'last_name': 'Spam' })

names_file.close() # Don't forget to close the file

print('All done!')
```

Note the `newline=''` keyword argument in `open()`, this is simply to guarantee interoperability between Mac and Windows. Just put it in there, we're not gonna worry too much about it, but if you're interested in why it's needed, you can read [this footnote](https://docs.python.org/3/library/csv.html#id3) in the [documentation](https://docs.python.org/3/library/functions.html#open).

If you run the previous example, you'll end up with a `names.csv` file that looks like this when you open it in a text editor:

```
first_name,last_name
Baked,Beans
Lovely,Spam
Wonderful,Spam
```

Remember that this `names.csv` file represents a table that looks like this:

| first_name | last_name |
| --- | --- |
| Baked | Beans |
| Lovely | Spam |
| Wonderful | Spam |

You can, if you want, open the `names.csv` file with whatever spreadsheet program you have on your computer to verify!

Don't forget that we can use `with` to have it automatically close the file when we're done with all the file operations:

```python
import csv

FIELDNAMES = ['first_name', 'last_name']

with open('names.csv', 'w', newline='') as names_file:
  writer = csv.DictWriter(names_file, FIELDNAMES)

  writer.writeheader()

  dict1 = { 'first_name': 'Baked', 'last_name': 'Beans' }
  writer.writerow(dict1)
  dict2 = { 'first_name': 'Lovely', 'last_name': 'Spam' }
  writer.writerow(dict2)
  writer.writerow({ 'first_name': 'Wonderful', 'last_name': 'Spam' })

print('All done!')
```

The same code with explanatory comments (for when you're reviewing the lesson again later!)

```python
import csv

# These are the header values that will become the first line of a CSV file
# It should be a List!
FIELDNAMES = ['first_name', 'last_name']

# This line opens or creates a `names.csv` file
# The newline='' argument is necessary for compatibility between Mac and PC
with open('names.csv', 'w', newline='') as names_file:

  # Construct a new instance of `DictWriter`
  # Notice that we pass in the csv file, and a list of fieldnames, as required arguments!
  writer = csv.DictWriter(names_file, FIELDNAMES)

  # Write out the first row of the file, the header row
  # (this only needs to be done once!)
  writer.writeheader()

  # Write as many rows as you want
  # Notice that each dictionary argument represents a single row in the resulting file!
  # And there's no need to actually declare separate variables, as always...
  # ... BTW typically you'd **iterate** through a list of dictionaries,
  # instead of manually writing out each one...
  dict1 = { 'first_name': 'Baked', 'last_name': 'Beans' }
  writer.writerow(dict1)
  dict2 = { 'first_name': 'Lovely', 'last_name': 'Spam' }
  writer.writerow(dict2)
  writer.writerow({ 'first_name': 'Wonderful', 'last_name': 'Spam' })

print('All done!')
```

#### Appending

Of course, you may remember that that you can also open files in **append** mode:

```python
with open('names.csv', 'a', newline='') as names_file:
  ...
```

That would allow you to **append** a line to a CSV file with a single call to `writer.writerow(...)`, instead of writing the whole thing from top to bottom.

### `csv.DictReader`

Now let's take a look at the opposite class, `csv.DictReader`, which allows us to **read** rows from a CSV file as individual dictionaries.

```python
import csv

names = []

with open('names.csv', newline='') as names_file:
  reader = csv.DictReader(names_file)
  for row in reader:
    print(row)
    print(type(row))
    names.append(row)

for name in names:
  print(name['first_name'], name['last_name'])

print('All done!')
```

If we run this code, you'll see the following output:

```
{'first_name': 'Baked', 'last_name': 'Beans'}
<class 'dict'>
Baked Beans
{'first_name': 'Lovely', 'last_name': 'Spam'}
<class 'dict'>
Lovely Spam
{'first_name': 'Wonderful', 'last_name': 'Spam'}
<class 'dict'>
Wonderful Spam
All done!
```

Notice:

* When you instantiate a DictReader, you do not need to specify the field names of the resulting dictionary, as it'll automatically be inferred from the first row of the CSV file
* Then, the reader acts like a list and allows you to iterate through it. When you do, it'll give you each subsequent row **as a dictionary**! Neat!
   * The DictReader will skip the first row, the header row, automatically
* Since each row is simply a dictionary, you can do with it what you know about dictionaries, including organiing them into another type of data structure like a list. The possibilities are endless!

## Partner Exercise: TPS Report

![](assets/tps_reports.jpg)

Source: https://ce.uci.edu/careerzot/the-days-of-building-the-tps-report-are-over/

Your boss, Bill, asks you to come in on Saturday to finish a TPS report.

You promise to finish the report, but as Bill walks away, you smile knowing you have a trick up your sleeve: CSV Files and File I/O!

You plan on quickly writing up a bit of code to finish the report, all without spending a minute of your Saturday.

### Starter Code

```python
import csv

CSV_FILE = 'tps_report.csv'

employees = [
  {
    'first_name': 'Bill',
    'last_name': 'Lumbergh',
    'job_title': 'Vice President',
    'hire_date': 1985,
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Michael',
    'last_name': 'Bolton',
    'job_title': 'Programmer',
    'hire_date': 1995,
    'performance_review': 'poor'
  },
  {
    'first_name': 'Peter',
    'last_name': 'Gibbons',
    'job_title': 'Programmer',
    'hire_date': 1989,
    'performance_review': 'poor'
  },
  {
    'first_name': 'Samir',
    'last_name': 'Nagheenanajar',
    'job_title': 'Programmer',
    'hire_date': 1974,
    'performance_review': 'fair'
  },
  {
    'first_name': 'Milton',
    'last_name': 'Waddams',
    'job_title': 'Collator',
    'hire_date': 1974,
    'performance_review': 'does he even work here?'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Porter',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Slydell',
    'job_title': 'Consultant',
    'hire_date': 1999,
    'performance_review': 'excellent'
  }
]

def main():
  # Write your code here

main()
```

There is a list of dictionaries called `employees`, where each dictionary represents information about an individual employee: There `first_name`, `last_name`, `hire_date`, `job_title`, and `performance_review`.

Using `open()`, create a new file called `tps_report.csv`, and **write a loop** to **write out** every employee in the `employees` list to the `tps_report.csv` file.

(For this business process... do you think you need the `csv.DictWriter` class or the `csv.DictReader` class?)

Write your code where indicated in the `main()` function!

**Do not** write `writer.writerow()` many times (as in the example earlier). You know how to use loops, so you should **loop through** the `employees` list instead!

**BONUS:** For the `fieldnames` of the TPS report, you *could* write out all of the field names manually... But there's also a way to retrieve the field names... Think about how, before looking at the Hint below. (It's not a big deal if you have to write it out by hand like we did in the example above.)

<details>
<summary>Hint</summary>

You can get the keys of a dictionary with the `.keys()` method, the result which then must be converted to a list (you know how to convert between different data types!)method, the result which then must be converted to a list (you know how to convert between different data types!)
</details>

### Expected Output

**After** you write and run your program, the `tps_report.csv` file should contain:

```
first_name,last_name,job_title,hire_date,performance_review
Bill,Lumbergh,Vice President,1985,excellent
Michael,Bolton,Programmer,1995,poor
Peter,Gibbons,Programmer,1989,poor
Samir,Nagheenanajar,Programmer,1974,fair
Milton,Waddams,Collator,1974,does he even work here?
Bob,Porter,Consultant,1999,excellent
Bob,Slydell,Consultant,1999,excellent
```

If you open up that file in a spreadsheet program (like Excel or Numbers), it should look something like:

| first_name | last_name | job_title | hire_date | performance_review |
| --- | --- | --- | --- | --- |
| Bill | Lumbergh | Vice President | 1985 | excellent |
| Michael | Bolton | Programmer | 1995 | poor |
| Peter | Gibbons | Programmer | 1989 | poor |
| Samir | Nagheenanajar | Programmer | 1974 | fair |
| Milton | Waddams | Collator | 1974 | does he even work here? |
| Bob | Porter | Consultant | 1999 | excellent |
| Bob | Slydell | Consultant | 1999 | excellent |

### Solution

<details>
<summary>Answer (SPOILER!)</summary>

For the `main()` function only:

```python
def main():
  with open('tps_report.csv', 'w', newline='') as csvfile:
    fieldnames = list(employees[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()

    for e in employees:
      writer.writerow(e)
```
</details>