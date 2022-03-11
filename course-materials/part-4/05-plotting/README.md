# Plotting with Pandas and Matplotlib

## Lesson Objectives

*After this lesson, you will be able to:*

* Implement different types of plots/graphs/charts
* Use pandas to plot using three different datasets

---

# Let's Go!

Let's proceed to the Jupyter Notebook for this lesson.

You can locate it inside your Kaggle account under <kbd>Code</kbd> :arrow_right: <kbd>Your Work</kbd> :arrow_right: <kbd>Shared With You</kbd>

You won't be able to make changes to that notebook (as it's the instructor's copy).

So, once you have it open, click the <kbd>Copy and Edit</kbd> button (upper right hand corner) to make a copy of the notebook, so that you can make changes to it!

---

# Additional Resources

* [Pandas Plotting Documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)
* [Matplotlib Documentation](https://matplotlib.org/)
* [Matplotlib sample plots](https://matplotlib.org/tutorials/introductory/sample_plots.html)


<!--

---

# Plotting with Matplotlib

* [Matplotlib](https://matplotlib.org/) is a charting library for python and scientific computing
* Many data science shops use matplotlib as a standard
* It's considered the de-facto standard for charting in Python
   * It's best for EDA, general introspection of data, and scientific papers
      * Especially for publication-ready graphics
   * It's not so great for charts that are embedded in applications.
      * Instead, check out [d3.js](https://d3js.org/)
         * Works in a browser
         * Potential for interactivity
* Pandas' `.plot()` functionality is effectively a wrapper for Matplotlib

## Pandas and Matplotlib

Whats a wrapper? (Recall: We talked about this in APIs.)

A program that _abstracts_ another program to modify its interface.

* Pandas `.plot()` functionality uses matplotlib behind the scenes
* Matplotlib has a reputation for being fairly complex
   * Even for fairly simple charts, you will frequently write loops
   * A fairly plain chart can take 20-30 lines of code
* Pandas helps us here; most charts can be produced with 1-2 lines of code in Pandas
   * Some functionality is reduced, but _effort is minimized_ in most cases
   * There is a balance between package complexity and overall utility - sometimes a good answer delivered on time beats a perfect answer delivered late
* We will focus on using Pandas to chart, but if you wish, we encourage you to learn matplotlib on your own time
* You can use Matplotlib functions in combination with Pandas methods to alter the charts after drawing them
   * For example, you can use Matplotlib's `xlabel` and `title` functions to label the plot's x-axis and title, after the chart is drawn

As we explore different types of charts, notice:

* Different types of charts are drawn very similarly -- they even tend to share parameter names
* In Pandas, calling `plot()` on a `DataFrame` is different than calling it on a `Series`.
   * Although the methods are both named `plot`, they may take different parameters

*Sometimes Pandas can be a little frustrating... perserverence is key!*

![](https://media.giphy.com/media/EPcvhM28ER9XW/giphy.gif)

## Chart Types

We'll be covering the following chart types during this lesson:

* Time series line charts
* Categorical bar charts
* Histograms of single columns
* Histograms of entire data frames
* Scatter plots
* Scatter matricies (multiple scatter plots in a grid)
* Scatter plots with class colors for data points

The above chart types have been selected specifically to cover the majority of cases you'll encounter.

---

# Talk Data to Me

We'll be using three data sets for this lesson:

* **Football Records**: International football (read: *soccer*) results from 1872 to 2018
* **Avocado Prices**: Historical data on avocado prices and sales volume in multiple US markets
* **Chocolate Bar Ratings**: Expert ratings of over 1,700 chocolate bars

All datasets have been graciously downloaded from [Kaggle.com](https://kaggle.com) (an online community of data scientists and machine learners, owned by Google)

We'll discover that the right visualization can often replace a bit of fancy machine learning, if done properly.

-->