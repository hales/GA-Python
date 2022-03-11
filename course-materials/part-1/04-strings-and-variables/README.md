# Strings and Variables

## Data and Computation

<img align="right" width="200" src="assets/data.jpg">

The entire point of running a computer program is to do some sort of computation on some amount of **data**.

There are different **types** of **data** that exist in the world around us. Numbers, fractions, text, etc are all different types of data. 

## Data Types

Data is represented in computer programs as **Data Types**. Data Types let you define different kinds of data that all have their own special behaviours.

Once you have some data, you can run some sort of computation upon that data. But how do you put some data in your program?

## Variables

Data needs to be stored in your computer's memory for use later in your program (You may have heard of RAM -- Random Access Memory -- when you bought your computer).

To store a piece of data in your computer's memory, we use a **variable**.

The first type of data we'll look is textual information.

Text is represented with the **Strings** data type. So let's store a string in a variable.

To **declare** a variable, you give it a name, and place some data inside that variable with an `=` sign:

```python
my_var = 'my_var now contains this string'
```

* Variables allow us to give a name to a piece of data. Metaphorically you can think of it as a box where you can put a piece of data
* We can now refer to the variable named `my_var` whenever we want to access that piece of data, in this case a string
* They are called variables because we can put any data we like inside, and we can change the values any time we like. i.e. the value can vary over time

## Strings

> Let's now open up our code editor and learn more about strings.

Basically, a **string** is a sequence of characters between quotation marks.

This is the data type that allows you to put words and sentences in your programs.

To write a string, put some characters between single or double quotes. Below is an example of how to represent strings using either single or double quotes:

```python
hello1 = 'Hello world'
hello2 = "Hello world"
```

<!--
Let's try this now in our code editor. Create a new file called `str_practice.py`, put those lines of code in the file, and then run the program in the terminal:

```zsh
python str_practice.py
```
-->

Does anything happen when we run the program?

## Output

Notice that nothing happens when you run the program!

That's because all we did was tell Python to create two variables, but we didn't tell Python what to do with that data.

Remember that a computer program consists of some *data* and the *computation* to be run upon that data! We got the first part, but not the second part.

In order to communicate this data to the user looking at the screen, we need to `print` this data to the screen.

```python
print(hello1)
print(hello2)
```

(In the very olden days, `print` actually printed on a physical paper printer!)

And by the way, you don't *always* have to declare a variable. It's up to the programmer! You can `print` some data directly:

```python
print('look ma, no variable!')
```

## Strings Continued

What's the difference between single and double quotes?

If you need to write a quotation mark inside the string itself, then you need to use the other one to terminate the  string:

```python
mark = "Mark O'Brien"
speech = 'He said "Wow!"'
```

Otherwise there is no other difference.

Can you think of when this might not be enough?

<details>
<summary>Answer (SPOILER!)</summary>
When you need to mix lots of double and single quotes! Maybe you're writing a big novel!
</details>

The way to deal with that situation, is to use a backslash:

```python
print('I said "Let\'s go to Betty\'s Pie Shop!"')
```

Because the word "Let's" and "Betty's" contains a single quote (i.e. apostrophe), in the second line we need to use a backslash to "escape" the single quote so that Python understands that the single quote is part of the string, and not marking the end of the string.

We call this an **Escape Sequence**, and we'll see more examples of escape sequences later.

## Naming Variables

When you declare variables, give them meaningful names!

The name should match the type of data you're storing in the variable.

This helps your team members, as well as yourself in the future:

```python
employee_name = 'Betty Coder'
number_of_weeks = 12
```

* The accepted [Python style](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) is to write variable names in all lower case, with underscores separating words if necessary

* Some other [rules](https://www.google.com/search?q=python+variable+naming+rules) for naming variables are:
   * Must start with a letter or the underscore character `_`
   * Cannot start with a number
   * Can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_`)
   * Names are case-sensitive (`age`, `Age` and `AGE` are three different variables!)

### Don't Use Reserved Words

When you give a name to a variable, be sure not to use any words already used by Python, like `print`.

Otherwise, unpredictable things can happen, which is the opposite of what we want in a computer program.

We call this a [Name Collision](https://en.wikipedia.org/wiki/Name_collision).

Here's a list of [Reserved Words in Python](https://www.w3schools.com/python/python_ref_keywords.asp) -- Don't use any of those words! Unfortunately, it's not an exhaustive list as new stuff is being added to Python, and all of its associated **libraries** and **modules**, all the time (even though you don't know what those are yet!).

**Protip:** Don't use any of the **[library](https://docs.python.org/3/library/)** and **[module](https://wiki.python.org/moin/UsefulModules)** names, like `random`.

Don't worry -- this will come with experience!

### Overwriting Variables

> For this next part, let's try inside the REPL

You can change the data that you put in a variable. Here, we'll overwrite the name variable with a new name:

```python
friend = 'Joe'
print(friend) # Joe
friend = 'Jill'
print(friend) # Jill
```

You can even re-use the old data in the `friend` variable:

```python
friend = friend + ' ' + 'West'
print(friend)
#==> Jill West
```

You can even change the **type of data** in a variable (The number `123` is not a name, but that's OK for now):

```python
name = 123 
print(name)
#==> 123
```

You shouldn't be changing the **type of data** in a variable though, for sanity purposes.

We'll talk about numbers soon!

### REPL Variable Inspection

In the REPL only -- you can examine the contents of a variable simply by typing the name of the variable, without `print`ing!

This is the special ability of the REPL -- it's like "God Mode" in a video game.

When you are writing a program saved in a `.py` file, you don't get this special ability! It's only in the REPL.

## String Interpolation

> This is a **very important** technique and you must get to know this very well!

<img width="400" src="assets/form_letter.png">

**String Interpolation** sort of like filling in blanks in a form letter.

To activate this feature of Python, you must place an `f` in front of a string.

Then, you "fill in the blanks" by placing your variable inside the curly braces `{}`.

```python
name = 'Betty'
greetings = f'Hello {name}, how are you today'
print(greetings)
```

In this case, the string `'Betty'` is stored in a variable and then used in the interpolation into `greetings`.

Notice that `f` at the beginning of the `greetings` string. The `f` stands for **Formatted String**, as opposed to a regular string, which would not be able to do interpolation.

We can embed more than one value:

```python
name1 = 'Betty'
name2 = 'Bella'

print(f'Hello {name1}, hello {name2}!')
```

And a more complicated example:

```python
name = 'Sandra'
greetings = f"Hello {name}! It's good to see you again."
mission = 'Your mission, should you choose to accept it...'
print(f'{greetings} {mission}')
```

> I will emphasize **again** that string interpolation is a **very important** technique, we'll be doing this over and over again the next 10 weeks. If this is unclear, ask your questions now!

---

# Additional Resources

* [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
* [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
* [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)
* [Python Programming Tutorial: Variables](https://www.youtube.com/watch?v=vKqVnr0BEJQ)
* [Variables in Python](https://www.guru99.com/variables-in-python.html)
* [Python Style Guide: Naming](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

<!--
As we saw before, you can even skip the variables altogether:

```python
f"Hello {'Betty'}, hello {'Bella'}!"
```

You can also embed other Python code into a string, like so:

```python
f'Ada Lovelace lived for {1852 - 1815} years'
###> Ada Lovelace lived for 37 years.
```

First, Python calculated `1852 - 1815`, comes up with the number `37`, and then inserts that number into the string where we've left `{}` as a placeholder.

([Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) -- the first "computer programmer".)

Let's some more examples:

```python
f'Three times three is {3 * 3}'
``` 
-->
