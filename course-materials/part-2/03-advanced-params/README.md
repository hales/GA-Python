# Advanced Function Parameters

Now it's time to take a look at some "advanced" function parameters; we'll see them a lot later on!

---

# Review: Function Parameters and Arguments

* A function can have no parameters, one parameter, or many parameters
* **Parameter**: The variable that's defined in a function's declaration
* **Argument**: The actual value passed into the function when the function is called
* The relative **position** of arguments matter!

```python
def greetings(name, age, job):
  return f'Hello, my name is {name}, I am {age}, and I am an {job}'

print(greetings('Simu', 30, 'actor'))
#==> Hello, my name is Simu, I am 30, and I am an actor

# Oops
print(greetings(25, 'engineer', 'Muhammad'))
#==> Hello, my name is 25, I am engineer, and I am an Muhammad
```

In practice, developers will use both words interchangeably, unfortunately.

---

# Keyword Arguments (kwargs)

We see that normally the position order of arguments matter very much!

Much like if you go to a restaurant, *by default* you will get drinks, then appetizers, then entrees, then desserts.

However, you are free to ask your waiter to bring your dessert first instead. You don't need to specify anything if the default order is fine, but if you are going to reinvent dinner order, you will need to say something!

Using **Keyword Arguments (kwargs)**, order doesn't matter:

* Arguments are named according to their corresponding parameters
* Order doesn't matter - Python will check the names and match them!
* Values are assigned because the *keyword argument* and the *parameter name* match

```python
print(greetings(age=25, job='engineer', name='Muhammad'))
#==> Hello, my name is Muhammad, I am 25, and I am an engineer

print(greetings(job='nurse', name='Chantal', age=33))
#==> Hello, my name is Chantal, I am 33, and I am an nurse
```

## Mix It Up... But Not With Every Argument?

Fun fact: You can provide some args in order (**positional**) and some with keywords.

* Positional arguments are assigned in sequential order
* Keyword arguments have to come last!

```python
def dinner(drink, app, main_course, dessert):
  print("You're drinking:", drink)
  print("You're snacking on:", app)
  print("You're dining on:", main_course)
  print("You're wrapping up with:", dessert)

dinner(app='chicken wings', main_course='medium rare steak', drink='water', dessert='milkshake')
dinner('chicken wings', 'water', dessert='milkshake', main_course='medium rare steak')
```

* What happens if you put a kwarg first?

   ```python
   dinner(main_course='steak', 'nachos', 'water', dessert='cake')
   ```

   Oops: `SyntaxError: positional argument follows keyword argument`

* What happens if you name two arguments the same?

   ```python
   dinner(app='nachos', app='steak', drink='water', dessert='cake')
   ```

   Oops: `SyntaxError: keyword argument repeated`

---

# Multiple Positional Arguments

Now, let's make functions a little more sophisticated.

What do you think the following code does?

```python
def multiply(x, y):
  return x * y

print(multiply(1, 2, 3)) # Too many arguments!
```

When we tried to run the function with too many arguments, we got an error.

What if we want to have any number of arguments? What if we want all of these to work?

```python
print(multiply(4, 5, 6))
print(multiply(4, 5))
print(multiply(4, 5, 2, 7, 3, 9))
```

## Introducing `*args`

`*args` is a parameter that says "Put in as many arguments as you'd like!"

* Pronounced like a pirate - "arrrrghhhs!"
* Known as **multiple positional arguments**
* The `*` at the beginning is what specifies the unknown number of arguments
* You can even put in 0 arguments!

```python
def multiply(*args):
  total = 1

  # We don't know the number of args, so we need a loop
  for num in args:
    total *= num

  return total

print(multiply(4, 5, 6)) # Prints 120!
```

* Declaring `*args` as a parameter gives us a list of arguments inside `args` (without the `*`), that we can loop over!
* Note how we declared a `total` variable to accumulate the total (called a 'product' in math)
* Check out the `*=` shorthand syntax! (Short for `total = total * num`)
* Don't forget the `*` and the `s`
  * The `*` indicates the unknown number of arguments
  * The `s` tells other programmers that your intention is to accept multiple arguments
  * Writing `*arg` (without an s) would be very confusing to someone maintaining your code in the future!
* (By they way, `*args` is just a convention, you can also say `*spoons` if you want, but that wouldn't make much sense!)


## We Do: `*args`

Let's create a file `args_practice.py`.

* We'll write a function, `add` that takes any numbers of arguments and adds them together
* The function should **return** the sum
* Your program should print out the result of calling the function
* Let's try it with `add(4, 5, 6)` and `add(6, 4, 5)`. The order doesn't matter! The result should be `15` of course
* Be sure to try calling the function with more or less arguments. Remember that `*args` means "any number of arguments" - you can even pass in no arguments at all!

<details>
<summary>Solution (SPOILER)</summary>

```python
def add(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

print(add(4, 5, 6)) # Prints 15
```
</details>

## `print()` uses `*args`!

`*args` is exactly why `print()` can print multiple arguments, separated by commas!

```python
print('hello', 33, 'cute', 'cats')
#==> hello 33 cute cats
```

---

# Revisiting Optional Parameters

Remember optional/default parameters?

**Optional parameters** have default values, so you don't need to pass arguments into them.

Only pass in an optional argument if you need it to be something other than the default!

```python
def greetings(name, age, job, city='Toronto'):
  return f'Hello, my name is {name}, I am {age}, and I am an {job}, and I live in {city}'

print(greetings('Simu', 30, 'actor'))
#==> Hello, my name is Simu, I am 30, and I am an actor, and I live in Toronto

print(greetings(job='nurse', name='Keisha', age=33, city='Atlanta'))
#==> Hello, my name is Keisha, I am 33, and I am an nurse, and I live in Atlanta
```

## Discussion: `print` Again!

Turns out...

* `print` accepts an optional keyword argument: `sep`
* The `sep` value given will be used as a **separator**
* It's optional! Without it, `print` by default uses a space, which is why you haven't seen it
* **This only applies when using commas to separate the arguments for `print`**

```python
print('Hi!', 'Vanilla', 'please,', 'but', 'chocolate', 'is', 'cool.')
#==> Hi! Vanilla please, but chocolate is cool.
print('Hi!', 'Vanilla', 'please,', 'but', 'chocolate', 'is', 'cool.', sep='--')
#==> Hi!--Vanilla,--please,--but--chocolate--is--cool.
```

* `sep` can be any string (but not an int)

If we look at the [documentation on `print`](https://docs.python.org/3/library/functions.html#print), we see that the function signature is:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

This tells us that `*objects` denotes multiple arguments, while `sep`, `end`, `file`, and `flush` are optional arguments with default values.

(Here, they've chosen to say `*objects` instead of `*args`, it's just another parameter name, after all.)

## Optional Keyword Arguments

In this case where `*args` is the first parameter, all the optional parameter must be keyword arguments!

This won't do what you expect:

```python
print('Will', 'this', 'work?', '---')
#==> Will this work? ---
```

But this will:

```python
print('But', 'this', 'will!', sep='---')
#==> But---this---will!
```

That's because without the keyword `sep`, the unnamed argument will just get shoved into `*args`!

<!--

---

# (If Time Permits) Partner Exercise

[5 mins]

## Poke At It!

Pair up! Choose a driver and a navigator.

* Create a file called `poke.py`, write a function, `print_food()` that has four optional parameters (*all with defaults of your choice*):
   * `favorite_food`
   * `lunch_today`
   * `lunch_yesterday`
   * `breakfast`
* `print_food()` should print out each of these.

Call this function a few ways:

* No arguments
* All arguments supplied
* Give all four arguments, but use a keyword for `lunch_yesterday` and `breakfast`
* All keyword arguments - out of order

<details>
<summary>Solution (SPOILER)</summary>

```python
def print_food(favorite_food='sushi', lunch_today='burger', lunch_yesterday='pad thai', breakfast='muffin'):
  print('my favorite food is:', favorite_food)
  print('my lunch today is:', lunch_today)
  print('my lunch yesterday is:', lunch_yesterday)
  print('my breakfast is:', breakfast)

print_food()
print_food('steak', 'mac&cheese', 'hot dog', 'cold pizza')
print_food('salad', 'sausage', lunch_yesterday='soup', breakfast='bacon&eggs')
print_food(lunch_yesterday='soup', favorite_food='salad', breakfast='bacon&eggs', lunch_today='sausage')
```
</details>

---

# How About Multiple Kwargs?

Now that you know about **multiple positional arguments**, and you know about **keyword arguments**... How crazy would it be if we could mix these two together?

In fact, it's not crazy at all.

What if I go to Froyo? I need:

* One argument `size`, to pick a cup size
* A variable number of arguments for all the toppings on the of frozen yogurt I might eat!

So basically we want to write code like this:

```python
buy_froyo('small', 'peanuts', 'gummie bears', 'sprinkles')
buy_froyo('medium', 'chocolate chip')
```

* Will this work?

   `def buy_froyo(*args)`?

   No! `*args` won't work - we need to know which arg is the cup size.

* Will this work?

   `def buy_froyo(size, toppings)`?

   No! There can be multiple toppings.

## Introducing: `**kwargs`

Recall that the `*` in `*args` means: Any number of *positional arguments*.

To take in a variable number of **keyword arguments**, we use `**kwargs` instead. Note the double `**`!

`kwargs` then becomes a dictionary that you can loop over!

```python
def buy_froyo(size, **kwargs):
  print(size)
  # We need a loop, because we don't know how many kwargs there are
  for topping, flavor in kwargs.items():
    # kwargs.items() yields the key and the value of each item in the dict,
    # which we're calling the "topping" and the "flavor" in the loop.
    print('My', topping, 'is', flavor)

# Like before, the unnamed arg has to come first!
buy_froyo('large!', first_topping='cherries', second_topping='chocolate chip', third_topping='banana')
```

and we get the output:

```
large!
My first_topping is cherries
My second_topping is chocolate chip
My third_topping is banana
```

* **Note:** `kwargs` is a dictionary!
* Can we skip the `size` positional arguments? (No!)

---

# (If Time Permits) Partner Exercise

[5 mins]

## Keep Poking!

Change roles!

Write two more functions to print food.

First, write `print_food_args()`, using `*args` as the parameter. Start the function by printing the contents of `args`, so you can see what's going on. Then, print each value you pass in (up to you to use a loop or not).

Then, write `print_food_kwargs()`, using `**kwargs` as the parameter. Start the function by printing the contents `kwargs`, so you can see what's going on. Then, as above, print each value you pass in (use a loop for this one).

<details>
<summary> Solution (SPOILER)</summary>

```python
def print_food_args(*args):
  print(args)
  print('my favorite food is:', args[0])
  print('my lunch today is:', args[1])
  print('my lunch yesterday is:', args[2])
  print('my breakfast is:', args[3])

def print_food_kwargs(**kwargs):
  print(kwargs)
  for keyword, value in kwargs.items():
    print(f'{keyword} is: {value}')

print_food_args('soup', 'salad', 'bacon&eggs', 'sausage')
print_food_kwargs(lunch_yesterday='soup', favorite_food='salad', breakfast='bacon&eggs', lunch_today='sausage')
```
</details>

---

# (Advanced Folks Only) Combining All The Types of Parameters

It is possible to combine all the different types of Parameters in one single function. You'll not likely to need to write this kind of function until you are in a much more senior situation, however!

```
def all_advanced_params(foo, bar='default bar', *args, **kwargs):
  print('foo:', foo)
  print('bar:', bar)
  print('args:', args)
  print('kwargs:', kwargs)

all_advanced_params('actual foo', 'actual bar', 'arg1', 'arg2', kwarg1='kwarg1', kwarg2='kwarg2')
```

and the output would be:

```zsh
foo: actual foo
bar: actual bar
args: ('arg1', 'arg2')
kwargs: {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'}
```

In the case of combining all of these types of parameters:

* First list all of the positional parameters without default values
* Then comes all of the positional parameters with default values
* After that you can use multiple positional parameters (`*args`)
* And finally multiple keyword parameters (`**kwargs`)

---
-->

<!-- At this point, we have `*args`, `kwargs` and `**kwargs`:

# Review of Argument Types

**`*args`:** Any number of arguments:

```python
def multiply(*args):
  total = 1
  for num in args:
    total *= num
  return total

print(multiply(4, 5, 6))
```

**Keyword Arguments (Kwargs):** Named (keyword) arguments

```python
def triple_divide(x, y, z):
  return(x / y / z)

print(triple_divide(x=10, y=2, z=1))
```

**`**kwargs`:** Any number of Kwargs

```python
def buy_froyo(size, **kwargs):
  for topping, flavor in kwargs.items():
    print(topping, 'is', flavor)

buy_froyo('large!', topping1='sprinkles', topping2='chocolate chips', topping3='butterscotch')
``` -->

# Summary

* kwargs:
  * ​A set number of **keyword arguments**
  * Can be defined out of order
  * `my_func(a=1, b=2, c=3)`
* `*args`:
  * ​Variable number of arguments
  * `def multiply(*args):`
* Optional parameters:
  * Default values are given in the function declaration
  * Example: `sep` in print
  * `def my_func(a=10, b=15, c=20)`

Are there more? Yes, there are. There's also `**kwargs`, which is **multiple keyword arguments**. We won't cover it as we won't need it, but as you get more and more advanced in Python, you can look into that as well. As usual, in this course we'll learn *just enough* to be able to move on!

<!--
* `**kwargs`:
  * Any number of keyword arguments
  * `def buy_froyo(size, **kwargs)`
-->

---

# Additional Resources

* [Optional Parameter Repl.it](https://repl.it/@GAcoding/python-programming-optional-parameters)
* [Keyword Args](http://treyhunner.com/2018/04/keyword-arguments-in-python/)
* [Args and Kwargs](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
* [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
