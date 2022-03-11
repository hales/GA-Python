# Common Mistakes

Let's look at some code with some common beginner mistakes.

What do you think is wrong with the following code? Will it run at all? If yes, what does it print?

## Discussion: Common Mistake #1

Do you think this will run? If yes, what does it print?

```python
my_num
print(my_num)
```

<details>
<summary>Answer (SPOILER!)</summary>
No, it won't run; you've declared a variable without assigning it a value.
</details>

## Discussion: Common Mistake #2

How about this? Does it run? If so, what does it print?

```python
my_num = 5
print()
```

<details>
<summary>Answer (SPOILER!)</summary>
It will run, but it won't print anything.
</details>

## Discussion: Common Mistake #3

How about this? Does it run? If so, what does it print?

```python
my_num = 5
my_string = 'Hello'
print(my_num + my_string)
```

<details>
<summary>Answer (SPOILER!)</summary>
This won't run, because Python will try to add a string and a number and throw an error.
</details>

## Discussion: Common Mistake #4

One last question. What does this do?

```python
my_num1 = '10'
my_num2 = '20'
print(my_num1 + my_num2)
```

<details>
<summary>Answer (SPOILER!)</summary>
There's nothing technically wrong with this one, except that it makes a string and not a number. It prints the string 1020.
</details>
