# Data Munging with Pandas

## Learning Objectives

*After this lesson, you will be able to:*

* Identify and handle missing values
* Use `groupby` statements for specific segmented analysis
* Use `apply` to clean data

---

# To the Notebook!

Let's proceed to the Jupyter Notebook for this lesson.

You can locate it inside your Kaggle account under <kbd>Code</kbd> :arrow_right: <kbd>Your Work</kbd> :arrow_right: <kbd>Shared With You</kbd>

You won't be able to make changes to that notebook (as it's the instructor's copy).

So, once you have it open, click the <kbd>Copy and Edit</kbd> button (upper right hand corner) to make a copy of the notebook, so that you can make changes to it!

<!--

We will commence this lesson directly in the Jupyter Notebook, `data-munging.ipynb`, to walkthrough the what, why, and how all at once.

```zsh
jupyter notebook data-munging.ipynb
```

Below, we have included a review of the key concepts.

---

# How do we Handle Missing Data?

To handle missing data, we must:

* Identify we have missing data from our DataFrame
* Determine, to the best of our ability, the cause of this missingness
* Justify how we will handle the missing data (drop or fill in with a specific value?)

**Pro tip:** If you can understand *why* some observations are missing, the faster and more accurately you can handle them.

## Key Pandas Functions for Missing Data

### Identify how many nulls you have

```python
df.isnull().sum()
```

### Drop rows with nulls (if necessary)

```python
df.dropna(inplace = True) #careful!
```

### Fill in (if necessary)

Replace missing value with the desired way of filling

```python
df.fillna(value=column.mean(), inplace=True)
```

---

# How do we use `groupby`?

**`groupby`** allows us to conduct analysis on a specific subset.

Groupby follows a "split, apply, combine" methodology:

![](assets/split_apply_combine.png)

Determine what attribute to `groupby` in a cohort, and how to aggregate those values within that cohort.

e.g. If we have 300 lemonade stands, do we want to know the average amount of lemonade sold across all stands, or identify which lemonade stand sold the most?

## Aggregating with `groupby`:

Replace `'column'` with the actual column of interest!

```python
df.groupby('column').agg('count', 'mean', 'max', 'min')
```

---

# How do we use `apply`?

The **`apply`** function help us clean values across an entire DataFrame column. They are like a for loop for cleaning, but many times more efficient.

The steps to follow to use `apply`:

1. Write a function that convert a single value
1. `apply` that function to all of the values in a single column

## Example:

```python
def dollars_to_float(value):

  # try to convert the value to a float
  try:
    return float(value.strip('$'))

  # in the case of the value being a null value, we simply return a null
  except:
    return np.nan

df['sale_clean'] = df['sale_unclean'].apply(dollars_to_float)
```

-->
