# The `for` Loop

This situation isn't so bad:

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

print(visible_colors[0])
print(visible_colors[1])
print(visible_colors[2])
print(visible_colors[3])
print(visible_colors[4])
print(visible_colors[5])
```

But what would we do if there were 1,000 items in the list to print? How about 100,000 items?

This is exactly where a computer is useful. You can program it to automatically perform repetitive tasks, using loops!

The first form of loop we'll study is the `for` loop. `for` loops are a standard feature in most computer languages.

In Python, the `for` loop follows this form:

```python
for an_item in a_list:
  # Do something with/process that item
```

* The indentation is like the `if` statement you learned before
* `a_list` is some variable referencing a list
* `an_item` will be a temporary holding variable which has a **copy** of the item currently being "processed"

For example:

```python
visible_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

for color in visible_colors:
  print(color)
```

This code:

* Starts with a new list containing some strings
* Begins the `for` loop. We loop once for each `color` in the list (`visible_colors`)
* Prints the current color inside the loop

The `for` loop is perfect for when you have a specific collection of items — each of which must be processed once — or for when you know that you must execute a set of instructions a specific number of times. Those are the use cases for which it was designed.

The program will start with the first item and automatically stop after it finishes with the last item.

## Knowledge Check: What Will this Code Do?

Think about what the code will do before you actually run it.

```python
for name in ['Tom', 'Deborah', 'Murray', 'Axel']:
  print('Now appearing on the stage...')
  print(name)
  print('THUNDEROUS APPLAUSE!')
```

The statements inside a loop that you want to repeat must be indented like the statements inside an `if` block. So, if you have three lines of code that you want to execute on each loop iteration, each must be indented one level underneath your `for` line.

What happens if you move the last `print('THUNDEROUS APPLAUSE!')` outside the for loop?

```python
for name in ['Tom', 'Deborah', 'Murray', 'Axel']:
  print('Now appearing on the stage...')
  print(name)
print('THUNDEROUS APPLAUSE!')
```

<details>
<summary>Answer (SPOILER!)</summary>

It'll print `THUNDEROUS APPLAUSE!` only once, after everyone appears on the stage.
</details>

<!--
## We Do: Writing a Loop

Let's write a loop to print names of guests.

First, we need a list.

* Create a file named `my_loop.py`
* Declare a variable `my_list` and assign it to a list containing the names of at least five people

Now, we'll add the loop.

* For the variable that holds each item, give it a name that reflects what the item is (e.g. `name` or `person`)
* Inside your loop, add the code to print `'Hello,'` plus the name

  Expected Output:

  ```
  Hello, Felicia!
  Hello, Srinivas!
  ```

* Our guests are VIPs! Let's give them a lavish two-line greeting instead
* Inside your loop, add the code to print another sentence of greeting:

  Expected Output:

  ```
  Hello, Srinivas!
  Welcome to the party!
  ```

Fantastic! Now each guest is greeted by their name and welcomed to the party.

<details>
<summary>Answer (SPOILER!)</summary>

Those two `print()` lines are executed on every iteration because both are indented to be in the `for` loop's code block. Think of the indented block as a unit of instructions executed as a group each time the loop runs.

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
for guest in guests:
  print(f'Hello, {guest}!')
  print('Welcome to the party!')
```
</details>
-->

<!--
# Looping Over Strings

A loop prints everything in a collection of items.

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
```

What, besides a list, could we use a loop on?

*Hint: There are six of them inside the list!*

<details>
<summary>Answer (SPOILER!)</summary>
The answer is a string! We can loop through the characters in a string.
</details>

You may not realize it, but a string is a collection of characters. Just so you can see that a for loop has the same syntax for any collection, let's add the following code below what we've just written.

```python
my_string = 'Hello, world!'

for character in my_string:
  print(character)
```

When you run this code, you'll see that each character in the string is printed!
-->

# Ranges

## What about Only *Part* of the List?

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for guest in guests:
  print(f'Hello, {guest}!')
```

The standard `for` loops runs once for every item in the list. Here, it runs 6 times.

What if you only want to loop through part of the list?

## Enter: `range()`

```python
range(x)
```

* Automatically generates a range that contains only integers that you can loop over
* Starts at zero
* Stops before the number you specify

```python
range(5) # 0, 1, 2, 3, 4
```

In this example, with `range(5)` then your loop will execute **five** times. Let's see it in action:

```python
for i in range(5):
  print(i)
```

We can see that this code prints each of the numbers in our range of 0 through 4 (5 numbers total). We don't need to have our loop print anything. This loop could be used to execute any sequence of code 5 times.

You can actually do more with `range()` to control what number it starts at and how big each step is to the next number, but we will keep it simple for now. If you're curious, here's the [documentation](https://docs.python.org/3/library/stdtypes.html#range) for `range()`.

## "Accumulating" Values into a List

One common pattern that we see in software development all the time is the idea of starting from an empty list, and then *accumulating* items into it.

```python
squares = []

for num in range(5): # 0, 1, 2, 3, 4
  sqr = num ** 2
  squares.append(sqr)

print(squares)
#==> [0, 1, 4, 9, 16]
```

We would often "accumulate" values in a situation where there's some sort of an idea of "waiting". For example, if you're writing software to simulate the performance of a subway system, then passengers arriving at a subway platform over time could be appended to a list. When the train finally arrives, the entire list of passengers can be taken away by the train.

## Looping Over Part of a List

Getting back to looping over lists -- compare looping through the entire list:

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for guest in guests:
  print(f'Hello, {guest}!')
```

and now, if you only want to admit the first 3 guests, we can now use `range()`:

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
num_to_admit = 3

for i in range(num_to_admit):
  print(f'Hello, {guests[i]}!')
```

## Looping Over the Whole List with `range()`:

If you want to loop over the entire list with `range()`, just use the length of the list!

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for i in range(guests):
  print(f'Hello, {guests[i]}!')
```

## Modifying an Item in a List (Part 1)

But why would you use `range()` on a list, when you could just `loop` over list? The syntax seems harder!

But there is one special use for `range()` that is vital to know about.

When we use the `for item in collection` syntax, it is not possible to **modify** the list item that is being iterated over.

```python
for an_item in a_list:
  # Do something with an_item
```

Recall that `an_item` is a temporary holding variable -- when we access `an_item` we are actually getting a ***copy*** of the current item in the list!

For example, If you want to modify everybody's name on the guest list, this won't do anything:

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for guest in guests: # guest is a copy of each string, on each iteration
  guest += 'ay'      # Same as guest = guest + 'ay'

print(guests) # Nothing changed
```

In order to **modify** the content of the item in the list, we need the index of that item in the list. And guess what `range()` gives us...

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for i in range(len(guests)):
  guests[i] = guests[i] + 'ay' # Same as guests[i] += 'ay'

print(guests) # Names are changed!
```

## Modifying an Item in a List (Part 2)

Let's try to make the guest list all uppercase.

This code won't do the trick, because it's using the `for item in collection` syntax:

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for guest in guests:
  guest = guest.upper()

print('Without using range, the guest list is', guests)
```

Remember that the `guest` variable is just a temporary copy so it doesn't matter what happens to it. The original list item won't be modified.

But this code will do it:

```python
guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']

for i in range(len(guests)):
  guests[i] = guests[i].upper()

print('Using range, the guest list is', guests)
```

Again, the secret here is that we are modifying the item in the list by *accessing it by its index*.

## Knowledge Check

Which of the following lines is *syntactically correct*?

```python
my_list = ['mon', 'tue', 'wed', 'thu', 'fri']

# Answer A
for j in range(my_list):
  ... more code here ...

# Answer B
for j in range(len(my_list)):
  ... more code here ...

# Answer C
for j in range(my_list.length):
  ... more code here ...
```

<details>
<summary>Answer (SPOILER!)</summary>

The answer is B
</details>

## You Do: Range

[5 minutes]

Partner up! Choose one person to be the driver and one to be the navigator.

Create a new file called `range_practice.py`. In it:

* Create a list of colors with `'red'`, `'green'`, and `'blue'`
* Using a `for` loop, print out the list
* Next, using `range()`, set each item in the list to be the number of characters in that item
* Print the list

The expected output is:

```python
red
green
blue
[3, 5, 4]
```

<details>
<summary>Answer (SPOILER!)</summary>

```python
colors = ['red', 'green', 'blue']

for color in colors:
  print(color)

for i in range(len(colors)):
  colors[i] = len(colors[i])

print(colors)
```
</details>

---

# Additional Resources

* [Learn Python Programming: Loops Video](https://www.youtube.com/watch?v=JkQ0Xeg8LRI)
* [Python: For Loop](https://wiki.python.org/moin/ForLoop)
* [Python: Loops](https://www.tutorialspoint.com/python/python_loops.htm)

---

# Challenging Take Home Exercises

These are challenging exercises, and you may not be able to do them until after you've had more practice, and we learn about **functions**. You can always do them later on to continue sharpening your skills.

If you're a pure beginner, I recommend you come back to these *after* the first half of the course is over.

## You Do: FizzBuzz

[5 minutes]

This is a *very* common programming question. It's often on job interviews and a buzzword in the industry as a simple but common task to show your understanding of programming.

Create a new file: `fizzbuzz.py`.

* Write a program that prints the numbers from 1 to 100, except:
   * For multiples of three, print `Fizz` instead of the number
   * For multiples of five, print `Buzz`
   * For numbers which are multiples of both three **and** five, print `FizzBuzz`

<details>
<summary>Answer (SPOILER!)</summary>

```python
def fizz_buzz(num):
  if num % 15 == 0:
    return 'FizzBuzz'
  elif num % 5 == 0:
    return 'Buzz'
  elif num % 3 == 0:
    return 'Fizz'
  else:
    return num
for i in range(1, 101):
  print(fizz_buzz(i))
```
</details>

## You Do: Building a Copy of a List

[5 minutes]

* In a new file `list_exercises.py`, write a function, `copy_list`, that takes in a list, `original_list`, as a parameter
* Your function should create a new list, `my_new_list` with the contents of the original list
* Your function should return `my_new_list`

An example of how this function can be used:

```python
my_list = [1, 2, 3]
my_new_list = copy_list(my_list)
print(my_new_list)
#==> [1, 2, 3]
```

Make sure you run your code to check that it works!

Some hints are provided below; try to open just one of them at a time!

<details>
<summary><strong>Hint 1</strong></summary>

You'll need a `for` loop
</details>

<details>
<summary><strong>Hint 2</strong></summary>

You'll need to declare `my_new_list` above (outside of) your `for` loop
</details>

<details>
<summary>Answer (SPOILER!)</summary>

```python
def copy_list(original_list):
  my_new_list = []
  for item in original_list:
    my_new_list.append(item)
  return my_new_list
```
</details>

## You Do: Comparing two Lists

[5 minutes]

Awesome job! Let's try a harder one.

In a file (it can be the same one as before, if you'd like), write a function, `check_list_equality`, that takes in two lists, `first_list` and `second_list`, as parameters. Your function should return  `True` if the two lists contain the same elements in the same order. Otherwise, it returns `False`.

Examples of how this function can be used:

```python
list_one   = [1, 2, 3]
list_two   = [1, 2, 3]
list_three = [3, 2, 1]
list_four  = [1, 2, 3, 4]
print(check_list_equality(list_one, list_two))   # True
print(check_list_equality(list_one, list_three)) # False
print(check_list_equality(list_one, list_four))  # False
```

<details>
<summary><strong>Hint 1</strong></summary>

Start by making sure the lists have the same length!
</details>

<details>
<summary><strong>Hint 2</strong></summary>

You'll only need one `for` loop
</details>

<details>
<summary><strong>Hint 3</strong></summary>

You'll certainly need to use `range()` and `len()`
</details>

<details>
<summary>Answer (SPOILER!)</summary>

```python
def check_list_equality(first_list, second_list):
  if len(first_list) != len(second_list):
    return False
  for i in range(len(first_list)):
    if first_list[i] != second_list[i]:
      return False
  return True
```
</details>

## You Do: Reversing a List (HARD)

[10 minutes]

This is a more challenging exercise.

In a file (it can be the same one as before, if you'd like), write a function, `reverse_list`, that takes in a list, `my_list`, as a parameter.

Your function should reverse the list *in place* and return it.

An example of how this function can be used:

```python
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)
#==> [5, 4, 3, 2, 1]
```

<details>
<summary><strong>Hint 1</strong></summary>

Do not declare another list -- your function should *modify* the existing list
</details>

<details>
<summary><strong>Hint 2</strong></summary>

Remember that you can access an item from the end of a list with a negative index. Example: `my_list[-2]` is 4, in the example above.
</details>

<details>
<summary><strong>Hint 3</strong></summary>

You'll certainly need to use `range()` and `len()`
</details>

<details>
<summary><strong>Hint 4</strong></summary>

Make sure your function works with lists that are both <em>even</em> and <em>odd</em> lengths
</details>

<details>
<summary>Answer (SPOILER!)</summary>

```python
def reverse_list(my_list):
  for i in range(len(my_list) // 2):
    temp = my_list[i]
    my_list[i] = my_list[-i-1]
    my_list[-i-1] = temp
```
</details>

<!--

# Review: For Loops and Range

* `for` loop on a list (a collection of strings)

  ```python
  guests = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
  for guest in guests:
    print('Hello, ' + guest + '!')
  ```

* `for` loop on a string (a collection of characters)

  ```python
  my_string = "Hello, world!"
  for character in my_string:
    print(character)
  ```

* Basic `range()`

  ```python
  range(4) # 0, 1, 2, 3
  ```
  
* Using `range()` as an index counter (with `len()`)

  ```python
  names = ['Flint', 'John Cho', 'Billy Bones', 'Nanda Yuna']
  for i in range(len(names)):
    print(names[i])
  ```

* Using `range()` to change a list

  ```python
  names = ['Fred', 'Cho', 'Brandi', 'Yuna', 'Nanda', 'Denise']
  for i in range(len(names)):
    names[i] = 'A new name'
  ```

-->
