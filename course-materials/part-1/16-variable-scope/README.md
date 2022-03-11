# Variable Scope

<!--
## Lesson Objectives

*After this lesson, you will be able to…*

* Define variable scope
* Explain the order of scope precedence that Python follows when resolving variable names
-->

## Discussion: Delivering a Letter

Let's pretend you want to give someone a letter.

You write "For Dave" on the envelope, with no other information, and you hand it to your classmate to deliver.

Which "Dave" would they deliver it to? If there is no other information, so they'd just give the letter to the first Dave they see!

They'd look:

* First in the classroom. Is there a "Dave" here? They get the letter!
* No? OK, look in the neighborhood. Is there a "Dave" here? They get the letter!
* No? OK, look in the town. Is there a "Dave" here? They get the letter!
* No? OK, look in the state. Is there a "Dave" here? They get the letter!
* ...etc

That's what **scope** means. That's basically where your class mate would look for someone named "Dave".

If there are more than one "Dave"s around, you might have to write more information on the envelope, if you want the letter to get to the right "Dave". Each "Dave" is a different person!

Your mail-carrying classmate would look in the **scope** of, in priority:

* Your classroom:
   * There's *probably* only one Dave
   * "For Dave" is fine
* Your town:
   * There might be multiple Daves in the town
   * "For Dave, on Main Street" would work
* In your state:
   * There are multiple Main Streets in New York!
   * "For Dave, on Main Street in Brooklyn" would work

## `x` marks the spot. Or does it?

Python has the idea of **scope**, too.

We can have many variables with the same name, and Python will look for them in the smallest-possible scope first.

---

# Local Scope

Let's start with the smallest scope: **local scope**.

We've seen that any variable declared inside a function, exists only within the function they are declared in.

We call these variables **local variables** as they exist only in the **local scope** of each function. They cannot cross the boundary to another function, nor can they escape the function.

```python
def my_func1():
  x = 1    # This is a LOCAL variable
  print(x) # 1

def my_func2():
  x = 5    # This is a DIFFERENT local variable, even though it has the same name
  print(x) # 5

my_func1()
my_func2()

print(x) # no x exists here, they all live inside the functions -- so x is "out of scope"
```

* The local scope is the most specific level of scope and is where most of your variables should be declared, whenever possible
* Only the function in which the variable was declared in can use that variable

In the previous example, The first `x` is only accessible from inside the `my_func1()` function. When we call the `my_func1()` function, as soon as it finishes running, the variable `x` ceases to exist. Even while the function was running, `x` was only accessible to `my_func1()`. Same with `my_func2()`.

Each of those `x`s are totally different variables, even though they have the same name!

## Parameters Also Create Local Variables

If a function accepts a parameter, a *local variable* of the same name is automatically declared in that function:

```python
def my_func3(y):
  # <---- Here, there's a local variable named y, initialized to the argument value
  print(y)
```

* `y` is a local variable inside the function `my_func3()`.

Note that it's actually possible to **assign** to that variable, although it's not typically a good idea to do so. If you must change the meaning of an input to the function, you should declare a new variable instead.

This is not so good:

```python
def my_func3(y):
  y += 100
  return y

print(my_func3(50)) #==> 150
```

Instead, do something like:

```python
def my_func3(y):
  z = y + 100
  return z

print(my_func3(50)) #==> 150
```

## Multiple Variables, One Name

Because parameters automatically create local variables for use within the function, it allows us to now **reuse** names in parameter lists!

For example:  `x` and `y` are frequently used to represent numbers.

```python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

print(divide(8,2))   #==> 4
print(multiply(3,1)) #==> 3
```

Understanding scope is important, so you realize these are all independent variables!

This is a good thing, otherwise we'd have to declare completely new variable names everytime we need to write similar functions such as `add`, `subtract`, `multiply`, and `divide`.

**Main Takeaway**: In *different* scopes, you can re-use the same variable name
   
* Each of them are a *completely different* variable!
* That is totally ok to do!

---

# Global Scope

When you declare a variable **outside** of a function, it is a **global variable**.

* When we define a variable _inside_ a function, it's _local_
* When we define a variable _outside_ a function, it's _global_
* Variables that are in **Global Scope** can be accessed by any function

**But first things first**: Avoid using **global variables**!

So why do we talk about this then? While you should always try to write code with only local variables, you might accidentally write code with global variables, or you have to deal with someone else's code that has global variables -- and you'll have to understand how to deal with them.

This is a general rule that applies to *all programming languages*.

Unfortunately, in some programming communities (unfortunately, Python in particular), the use of global variables is rampant, and they do come in useful *sometimes*.

You can read more about avoiding global variables [here](https://stackoverflow.com/a/19158418) if you want.

First, an example of where a global variable can be handy.

## Use of a global variable: `PI`

Remember from high school -- how to calculate the circumference and area of a circle:

```python
PI = 3.14

def circumference(r):
  return 2*PI*r

def area(r):
  return PI*(r**2)

r = 5
print(f'{circumference(r):.2f}') #==> 31.40
print(f'{area(r):.2f}')          #==> 78.50
```

In this example, it makes sense to place `PI` in the global scope, so that multiple functions can make use of it. These functions simply *use* the value of `PI`, never changing it (nor should they, it's `PI`!). Other types of data that should never change might include `HOURS_IN_A_DAY` or `DAYS_IN_A_WEEK`. (You can optionally stick these values inside a Tuple to make them truly immutable.)

**Protip**: Use `UPPER_CASE_NAMES` when declaring a global variable that is intended to be constant, to make it more clear!

These kinds of **constant** data might be just about the only reason you might want to declare a global variable!

Note also how we use formatted strings to show the circumference/area to 2 decimal places, by adding `:.2f` to the data being interpolated into the string!

This is one of the most useful features of `f`-strings. You can read as much as you like about using `f`-strings to format in [A Guide to f-string Formatting](http://cis.bentley.edu/sandbox/wp-content/uploads/Documentation-on-f-strings.pdf) but that's all we're going to talk about.

## More about Global Variables

* Python will adopt an "inside-out" strategy when evaluating variables of the same name, giving precedence to a local variable before using a global one

```python
x = 1

def my_func1():
  x = 2
  print(x)

def my_func2():
  print(x)

my_func1() #==> 2 - Python checks local scopes first
my_func2() #==> 1 - x doesn't exist in the local scope of my_func2!

print(x) # 1 - Python cannot access any of the x's in functions, so it will print the global x
```

* It is not necessarily a good thing that global variables are accessible from anywhere
  * Because global variables can be accessed anywhere, it can lead to troublesome bugs

## We Do: Scope Can Be Tricky

Lets try another, similar, example.

Now what do you think happens here?

```python
x = 1

def my_func3():
  x = 9000
  print(x) 

print(x)   # prints 1
my_func3() # prints 9000
print(x)   # prints 1
```

The variable `x` went back to its old value after the function finished! Actually, not quite. Here's what happened:

* The line in the function where `x` is assigned the value of `2` causes the creation of a new local variable of the same name
* We then set this variable's value to `2`, the function prints the value, and the function finishes. However, the global variable `x` was never touched by the function
   * They are completely different variables even though they have the same name!
* While we are able to *read* the value of the global `x` we were unable to *change* (i.e. *write*) the value of the global `x`!

That's because Python is protecting global variables from being changed inside functions, to avoid unintended consequences.

* Any time you assign a value inside a function with `=`, Python creates a local variable
   * Meaning, the `x` variable inside the `my_func3()` function is a different variable than the global `x` -- same name, different variable
   * Python does this to prevent unexpected behavior and accidental bad practice
* Any arguments passed into a function are put inside a local variable of the same name
* Global variables should be avoided whenever possible
   * Some argue that you will need to use a global variable _if multiple functions need access to that variable_. This is almost never true.
   * If a function needs a certain value, it should accept that value as a parameter. This maintains the integrity _of the interface between the data and the function_.
   * _Any_ function that has access to a global variable (i.e. all functions) can potentially modify its state. As an application grows, you will become unable to determine which function is modifying a global variable and it can be extremely difficult to debug.

## The `global` keyword

If you *really really really* want to *write* to a global variable within a function, then there's a way to tell Python to stop protecting you. You have to use the `global` keyword.

```python
x = 1

def my_func3():
  global x
  x = 9000
  print(x) 

print(x)   # prints 1
my_func3() # prints 9000
print(x)   # prints 9000
```

But don't use `global` if you can!!!

**Caveat**: Python only protects global variables that are **basic data types**, like strings, ints, floats, and booleans!

Things get even *more* confusing when your global variable is a **complex data types** such as a list or dictionary data type, as Python will protect them from being reassigned, but you can still change the contents by `.append()` ing to a global list, for example.

---

# Summary

Python checks **scope** to find the right variable:

* Functions create individual **local scopes**
   * A **local** variable doesn't exist outside its local function
* Any variable declared or assigned outside of any function is considered "global"
   * Variables that are in **global scope** can be accessed anywhere

Python will check for a **local** variable before using a **global** one.

There are actually even more scope levels! Python always works from the inside out — keep that in mind as you learn more about Python and your programs get more advanced.

---

# Additional Resources

* [Global vs. Local Variables](https://www.python-course.eu/python3_global_vs_local_variables.php)
* [Variables and Scope](http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html)
* (For Advanced Students Only) [Nested Functions — What Are They Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)


<!--
# You Do: Just a Day in the Jungle

Create a new file, `piranhas.py`:

* Declare a global variable `piranhas_hungry` and set it to `True`
* Write a function: `swing_vine_over_river()`. Inside it:
   * Print `Ahhh! Piranhas got me!`
   * Change `piranhas_hungry` to `False`
* Write another function: `jump_in_river()`. Inside it:
   * If `piranhas_hungry` is `True`:
      * Print `I'm not going in there! There are hungry piranhas!`
   * Otherwise:
      * Print `Piranhas are already full! Swimming happily through the Amazon!`

* Call the functions in this order:

   ```python
   jump_in_river()
   swing_vine_over_river()
   jump_in_river()
   ```

* Notice that we are not passing any arguments to `swing_vine_over_river` and `jump_in_river`. Does the value of `piranhas_hungry` change?
* Now let's try to pass `piranhas_hungry` as an argument to the two functions. Does the value of `piranhas_hungry` change now?

```python
piranhas_hungry = True

def swing_vine_over_river(piranhas_hungry):
    print('Ahhhh! Piranhas got me!')
    piranhas_hungry = False

def jump_in_river(piranhas_hungry):
    if piranhas_hungry:
        print("I'm not going in there! There's hungry piranhas!")
    else:      
        print("Piranhas are already full! Swimming happily through the Amazon!")

jump_in_river(piranhas_hungry)
swing_vine_over_river(piranhas_hungry)
jump_in_river(piranhas_hungry)
```

Either way, even though we are able to *read* the value of `piranhas_hungry` we were unable to *change* (or *write*) the value of `piranhas_hungry`!

That's because Python is protecting global variables from being changed inside functions, to avoid unintended consequences:

* Any time you assign a value inside a function with `=`, Python creates a local variable
* Any arguments passed into a function are put inside a local variable of the same name

If you *really really really* want to *write* to a global variable within a function, then there's a way to tell Python to stop protecting you. You have to use the `global` keyword:

```python
piranhas_hungry = True

def swing_vine_over_river():
    global piranhas_hungry
    print('Ahhhh! Piranhas got me!')
    piranhas_hungry = False

def jump_in_river(piranhas_hungry):
    if piranhas_hungry:
        print("I'm not going in there! There's hungry piranhas!")
    else:      
        print("piranhas are full! Swimming happily through the Amazon!")

jump_in_river(piranhas_hungry)
swing_vine_over_river()
jump_in_river(piranhas_hungry)
```

In this case, we inserted `global piranhas_hungry` inside the `swing_vine_over_river` function. We also had to remove the parameter, or else you'll get a `SyntaxError: name 'piranhas_hungry' is parameter and global` error, as Python will be confused about your intentions!

Now the output is as expected:

```
I'm not going in there! There's hungry piranhas!
Ahhhh! piranhas got me!
piranhas are full! Swimming happily through the Amazon!
```
-->


<!--
What if we add a variable in a local function scope and try to access it from the global scope?

```python
x = 1

def my_func3():
  bar = 2
  print(bar)

print(x)  # prints 1
my_func3() # prints 2
print(bar)  # NameError: name 'bar' is not defined
```

It fails! When run this code, you will get an error: `NameError: name 'bar' is not defined`.

`bar` is only accessible from inside the `my_func3` function. We called the `my_func3` function, but as soon as it finished running, the variable `bar` ceased to exist. Even while the function was running, `bar` was only accessible to `my_func3`.
-->
