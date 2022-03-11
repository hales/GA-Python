# Intro to Object Oriented Programming

**Protip for Advanced Students**: It is important to underscore here that if you've learned some ideas about Object Oriented Programming in the past in other languages, you'll have to set all of that aside now. While the general ideas remain the same, Python's OOP is **not** the same as other popular languages like C++, Java, or Javascript -- do not try to carry over knowledge from those languages (if you know them) into Python, and try to learn all of it from the beginning again. I promise you it'll save a ton of heartache.

## Theory: Intro to OOP

* Object Oriented Programming is a **Programming Paradigm**
  * A way to organize your code and approaching the problem solving process
  * It's easy for us to think about because it models the way real life works
* OOP has lots of **vocabulary words**!
* Brief history
  * Gained prominence in the 70s and 80s
* These ideas apply to all languages that you might learn in the future
  * All modern programming languages are object-oriented languages
* Objects have 2 parts:
  * **State**
  * **Behaviour**
  * An object's behaviours can possibly change its states
  * On the flip side, an object's current states can also change its behaviours

## Class Discussion

What are the states and behaviours of this particular object?

<img src="assets/bumblebee_camaro.jpg" width="500">

## State ~ Variables, Behaviours ~ Functions

This idea of objects neatly map onto ideas that you already know: **variables** and **functions**.

We learned earlier that we can collect a group of related data together using a **dictionary**.

The new idea now, is that in addition to grouping together related data in a neat little package, we can now also attach related **functions** to that group. Now, instead of a dictionary, we have an **object**! **Objects** group both variables and functions up in a single unit!

In an object, we:

* Hold **state** with **variables**
* Model **behaviour** with **functions**
   * Except that there's a new vocab word here -- when a function is attached to an object, it's now called a **method** ... (why so many different names, I don't know, [it's just the way it is](https://softwareengineering.stackexchange.com/questions/20909/method-vs-function-vs-procedure))

| | Object |
| --- | --- |
| State | Variable |
| Behaviour | Method |

All of this so far is *OOP Theory* -- but now let's apply it towards Python!

<!--
## Aside: The Docstring

  * You can write a "docstring" using three quotation marks at the beginning and end of a string, right after a function declaration

```python
def hello():
    '''Says hello'''
    print('hello')
```

  * A "docstring" is simply a string that documents the functioning of your code
  * Once you have written the function and docstring, `hello.__doc__` returns the docstring
  * Another example: `input.__doc__`
  * `print(input.__doc__)` is nicer
  * `help(input)` is even nicer
-->


<!--
* Advantages of OOP:
  * Encapsulation
  * Abstraction
  * Polymorphism
  * Inheritance
-->
