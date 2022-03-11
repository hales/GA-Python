# Tuples

## Discussion: Immutability

What if, we have a list of data that we want to stay the same?

```python
rainbow_colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
```

We **don't** want this to be able to happen:

```python
rainbow_colors_list[0] = 'gray'    # Gray's not in the rainbow!
rainbow_colors_list.pop()          # We can't lose violet!
rainbow_colors_list.append('pink') # Pink's not in the rainbow!
```

We want `rainbow_colors_list` to be **immutable**, meaning: 'unchangeable'.

We do that in Python with **tuples**! 

## Tuples vs Lists

**Tuples** are similar to a list with the difference that, once assigned, the tuple _cannot be changed_:

```python
rainbow_colors_tuple = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
```

Tuples are denoted with parentheses `()` (instead of square brackets `[]` like regular lists).

Basically, a **tuple** is a kind of data structure that provides immutable values in a list-type format.

You use tuples to hold data in your program that is guaranteed to not change, while the program is running:

* 12 Months of the year
* 4 seasons
* 12 Zodiac signs: Aries, Gemini, Pisces, etc...
* The list of planets of the solar system (...oops, Pluto...)

## Tuple Syntax

* Access the elements of a tuple via indices (just like a list)

   ```python
   rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
   print(rainbow_colors[1])
   #==> 'orange'
   ```

* The elements of a tuple can be printed with a `for` loop (just like a list)

   ```python
   rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')

   for color in rainbow_colors:
     print(color)
   ```

Tuples work exactly like lists, except that, when you create a tuple, you use parentheses instead of square brackets.

* You can put anything you want in a tuple, but for today we'll just put in strings.
* One Gotcha with tuples -- to create a tuple with only *one* element, you must trail a single comma after it:

   ```python
   weird_tuple = ('singleton',)
   ```

### Watch out

* You can have duplicate values in a tuple!
* Once a tuple is created and assigned its elements, no changes can be made to the tuple
   * However, you can **reassign** the entire tuple if necessary
* Using a tuple communicates to other developers that the data contained inside should not be changed
* If you need the power to add, remove, or edit items while the program is running, use a list instead

## You Do: Tuples

[5 minutes]

* Make a file called `tuples_practice.py` and declare a tuple named `seasons`
* Set it to have the values `'fall'`, `'winter'`, `'spring'`, and `'summer'`
* Print the entire tuple
* Access each element directly with its index and print it
* Using a `for` loop, print each element
* Try to change the value of an element using its index (you can't!)
* Try to `pop` the last element off (you can't!)
* Try to `append` an element (you can't!)

<details>
<summary>Answer (SPOILER!)</summary>

```python
seasons = ('fall', 'winter', 'spring', 'summer')

print(seasons)
print(seasons[0])
print(seasons[1])
print(seasons[2])
print(seasons[3])

for season in seasons:
  print(season)

# seasons[0] = 'autumn'
# seasons.pop()
# seasons.append('springter')
```
</details>

## Tuples in Lists, Lists in Tuples

Don't forget that lists and tuples can hold anything, even other lists and tuples!

```python
tup1 = (0,1,2)
tup2 = (0, 'hello', tup1)
print(tup2)
#==> (0, 'hello', (0, 1, 2))
```

That's of course the same thing as:

```python
tup2 = (0, 'hello', (0,1,2))
print(tup2)
#==> (0, 'hello', (0, 1, 2))
```

And of course you cannot change any of these elements:

```python
tup2[2][1] = 'one'
#==> TypeError: 'tuple' object does not support item assignment
```

The situation changes if you had a list inside that tuple instead:

```python
tup3 = (0, 'hello', [0,1,2])
tup3[2][1] = 'one'
print(tup3)
#==> (0, 'hello', [0, 'one', 2])
```

The internal list is not bound by the rules of the enclosing tuple!

The takeaway lesson here: Whenever you are programming -- you as the programmer **must be aware of what type of data you're dealing with, at any time**.

## What's the Data Type of a Tuple?

Remember `type()`? It also works on Lists and Tuples:

```python
print(type(tup3))
#==> <class 'tuple'>
print(type(tup3[2]))
#==> <class 'list'>
```

A-ha! So you know that you cannot modify the outer data structure `tup3`, because it's a tuple, but you can modify the 2nd element of `tup3`, because that's a list!


<!--

----

# Quick Review: Sets, Tuples, Lists

**List**:

* The original: `['red', 'red', 'yellow', 'green']`
* Can have duplicates and is mutable: `append()`, `insert(index)`, `pop()`, `pop(index)`

**Set**:

* List without duplicates: `{'red', 'yellow', 'green'}`
* Mutable with `add()` and `remove()`
* Remember `add()` vs `append()` - because we can't guarantee it's going at the end of the set

**Tuple**:

* Can have duplicates, but immutable: You can't change it!
* `('red', 'red', 'yellow', 'green')` will *always* be `('red', 'red', 'yellow', 'green')`

Watch Out for Different Braces:

* `[]` vs `{}` vs `()`

## Creation

### List

```python
my_list = ['red',  'yellow', 'green', 'red']
```
### Sets

```python
my_set = {'red',  'yellow', 'green'}
my_set2 = set(my_list))
my_set = set(a_list_to_convert)
```
### Tuples

```python
my_tuple = ('red',  'yellow', 'green')
```

## Appending/Inserting/Adding

```python
my_list.append('blue')
my_list.insert(2, 'green')
my_set.add('blue')
# With tuples -> You can't!
```

## Removing

```python
my_list.pop(1)
my_set.remove('red')
# With tuples -> You can't!
```

By the way, you aren't expected to be syntax experts - you can always look this up! Working programmers look things up every day on the job. But you have to know what things you can do, and then you can look up the syntax.


## You Do: Partner Exercise: List Types Practice

[10 minutes]

You know the drill: Grab a partner and pick a driver!

Create a file, `sets_tuples.py`. In it:

* Create a list (`[]`), set (`{}`), and tuple (`()`) of some of your favorite foods
* Now, Create a *second* set *from the list*!

Next, in every list type (that you are allowed to):

* Add `'pizza'` anywhere; append `'eggs'` to the end
* Remove `'pizza'`
* Re-assign the element at index `1` to be `'popcorn'`
* Remove the element at index `2` and re-insert it at index `0`
* Print the element at index `0`

Print your final lists using loops.

Then print the **type** of each list (Recall the `type` function).

Make sure there are no errors!

<details>
<summary>Answer (SPOILER!)</summary>

```python
food_list  = ['Sushi', 'Pizza', 'Curry']
food_set   = {'Sushi', 'Pizza', 'Curry'}
food_tuple = ('Sushi', 'Pizza', 'Curry')
food_set2  = set(food_list)

# List
#--------
food_list.insert(0, 'Pizza')
food_list.append('Eggs')
food_list.remove('Pizza')         # Removes only one of the Pizzas
food_list[1] = 'Popcorn'          # Replaces 'Pizza' with 'Popcorn'
removed_food = food_list.pop(2)   # Removes 'Curry'
food_list.insert(0, removed_food) # Puts 'Curry' at beginning
print(food_list[0])

# Set
#--------
food_set.add('Pizza')
#food_set.append('Eggs')
food_set.remove('Pizza')
#food_set[1] = 'Popcorn'
#removed_food = food_set.pop(2)
#food_set.insert(0, removed_food)
#print(food_set[0])

# Tuples
#--------
#food_tuple.insert(0, 'Pizza')
#food_tuple.append('Eggs')
#food_tuple.remove('Pizza')
#food_tuple[1] = 'Popcorn'
#removed_food = food_tuple.pop(2)
#food_tuple.insert(0, removed_food)
print(food_tuple[0])

# Set
#--------
food_set2.add('Pizza')
#food_set2.append('Eggs')
food_set2.remove('Pizza')
#food_set2[1] = 'Popcorn'
#removed_food = food_set2.pop(2)
#food_set2.insert(0, removed_food)
#print(food_set2[0])

print("Looping through List")
for food in food_list:
  print(food)

print("Looping through Set")
for food in food_set:
  print(food)

print("Looping through Tuple")
for food in food_tuple:
  print(food)

print("Looping through Set2")
for food in food_set2:
  print(food)

print(type(food_list))
print(type(food_set))
print(type(food_tuple))
print(type(food_set2))
```
</details>

---

# Summary and Q&A

We've learned two new types of lists:

Sets:

* A mutable list without duplicates
* Handy for storing emails, usernames, and other unique elements

```python
emails = {'my_email@gmail.com', 'second_email@yahoo.com', 'third_email@hotmail.com'}
```

Tuples:

* An immutable list that allows duplicates
* Handy for storing anything that won't change

```python
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
```

-->

---

# Additional Resources

* [Python Tuple](https://www.programiz.com/python-programming/tuple)
* [Tuples](http://openbookproject.net/thinkcs/python/english3e/tuples.html)
* [Repl.it that recaps Tuples](https://repl.it/@GAcoding/python-programming-tuple-practice?lite=true)
* [Python Count Occurrences of Letters, Words and Numbers in Strings and Lists-Video](https://www.youtube.com/watch?v=szIFFw_Xl_M)
* [Storing Multiple Values in Lists](https://swcarpentry.github.io/python-novice-inflammation/03-lists/)
