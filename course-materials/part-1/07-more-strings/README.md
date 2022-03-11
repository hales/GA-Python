
# More About Strings

We already talked about strings earlier, but there is more!

## Escape Sequences

Remember Betty's Pie Shop?

```python
print('Betty\'s Pie Shop')
```

The combination of the backslash followed by the single quote is an example of an **escape sequence**.

Using double quotes for that whole string allows us to avoid having to use an escape sequence for the single quote character.

```python
print("Betty's Pie Shop")
```

Below are some of the more common escape sequences:

* `\"` :arrow_right: double quote
* `\'` :arrow_right: single quote
* `\\` :arrow_right: single backslash
* `\n` :arrow_right: new line / line break
* `\t` :arrow_right: tab

Try out this example code to better understand escape sequences:

```python
print("Hello\t\tworld")
print("1. Hello\n2. World")
print("Hello\n\n\n\n\nGoodbye world")
print("Hello \"world\"")
print("Hello \'world\'")
```

## Length of a String

Remember Tim?

<img width="400" src="../01-orientation/assets/drop_the_ego.png" />

And finally here is how to find out the length of a string -- with `len()`:

```python
name = 'Sandra'
name_length = len(name)
print(name_length)
#==> 6
```

or more simply:

```python
name = 'Sandra'
print(len(name))
#==> 6
```

or even:

```python
print(len('Sandra'))
#==> 6
```

We've seen this kind of thing before with `print()` and `input()`, where you can put some value inside the parentheses.

`print()`, `input()`, and `len()` are all examples of what we call **functions**. We distinguish using a function from using a **variables** by the parentheses that come after them!

If functions seem weird for now there is no need to fear - they are an important concept so we have coming up an entire lesson dedicated to functions!

## Does a String Contain Another String?

You can find out if a string contains another string with `in`:

```python
s = 'Hello World'

print('Hello' in s) #==> True
print('hell' in s) #==> False
print('or' in s) #==> True
```

The result of that expression is a **boolean**, remember those? We'll be talking about booleans in great detail very soon.

<!--
and of course you can use this boolean expression inside an `if` statement:

```python
sub_str = 'Hello'

if sub_str in my_str:
  print(sub_str, 'is in', my_str)
else:
  print(sub_str, 'is not in', my_str)
```
-->

## Stripping Strings

Sometimes you find yourself in the possession of a string that has spaces in front of it, after it, or even both!

```python
dirty_str = '   hello!  '
print(dirty_str)
#==>   hello!  
```

In order to deal with this nonsense, you can use `.strip()`. The syntax is kind of different and funny, but it works like this:

```python
dirty_str = '   hello!  '
clean_str = dirty_str.strip()
print(clean_str)
#==> hello!
```

## Search & Replace

Sometimes you want to replace a part of a string. To do that, use `.replace()`:

```python
incorrect_str = 'hello'
correct_str = incorrect_str.replace('hell', 'heck')
print(correct_str)
#==> hecko
```

---

# Additional Resources

* [List of Python Escape Characters](https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples)

<!--
### Splitting Strings

TODO: Add `split`

Move to List class
-->

<!--

So now the non-working example from earlier:

```python
'Mambo #' + 5
-> TypeError: can only concatenate str (not "int") to str
```

Can become:

```python
'Mambo #' + str(5)
-> 'Mambo #5'
```

-->

<!-- 
## String Operators

Strings can also work with some arithmetic operators (`+`, `-`, `*`, etc) and comparison operators (`>`, `<=`, `==`, etc). Try a few in the REPL to see what works and what doesn't.
-->

<!-- 
## String Concatenation

You've seen this already -- but just to remind you again: Recall again that the `+` operator allows us to join strings together. This is called **string concatenation**.

```python
first_name = 'Doc'
last_name = 'Brown'
full_name = first_name + last_name
print(full_name)
#==> Prints 'DocBrown'
```

Oops, notice that there is no space between `DocBrown`. To fix that, you just have to be mindful of putting a space in there.

```python
full_name = first_name + ' ' + last_name
print(full_name)
#==> Prints 'Doc Brown'
```

Remember that numbers inside of strings do not behave like numbers, the behave like strings:

```python
'5' + '4'
#==> '54'
```

Also, remember you can't add strings to a number, and vice versa!

```python
'Mambo #' + 5
#==> TypeError: can only concatenate str (not "int") to str
```

If you really want to, you'll have to convert the data types.

```python
'Mambo #' + str(5)
#==> 'Mambo #5'
```
-->