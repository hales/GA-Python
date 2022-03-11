# Output and Input

> Let's try the following code examples in a new file called `inout.py`.

In Replit, if you want to run a different file than `main.py`, you have to do it in the **Shell** tab with the following command:

```zsh
python inout.py
```

This is a sneak peek into using the **command line** -- something we'll learn later in the course!

## `print()`

We've already seen this: `print()` allows us to display information to the program's user. This is called **output**.  

```python
print('Hello world!')
```

If you have more than one piece of data to be printed, you can also use commas in your `print()` statement:

```python
name = 'Jill'
time = 'Morning'
print('Good', time, name)
#==> Good Morning Jill
```

When you use commas in `print`, notice how it automatically inserts a space between each item to be printed!

(Of course, you can also make a long string, and print that, using **string interpolation** as we saw already. What technique you use is up to you, the programmer!)

## `input()`

The opposite of `print()` (i.e. "output") is `input()`.

`input()` allows us to *receive information from the program's user*.

```python
print("What's your name?")
user_name = input()
print(f'Hello, {user_name}')
```

**Protip:** When a user gives you data via `input()`, it's always in the form of a **string**, even if they might have typed in some numbers!

---

# Additional Resources

* [A Repl.it Summarizing Print Statements](https://repl.it/@brandiw/Python-01-Variables-4?lite=true)
