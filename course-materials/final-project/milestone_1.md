# Final Project Milestone 1

In this milestone, you'll begin the first steps of your project.

![](../part-4/01-intro-to-ds/assets/ds_workflow.png)

* Start by finding a data set that you are interested on Kaggle
   * For example, the [Complete Pokemon Dataset](https://www.kaggle.com/rounakbanik/pokemon)

* Go to the page of the data set, then click <kbd>New Notebook</kbd> button *on the data set page* to generate a new Jupyter Notebook based on that data set
   * You **must** click the <kbd>New Notebook</kbd> button on the data set page in order for the notebook to see the data properly. If you generate a brand new notebook on its own, you'll have difficulty accessing the data

* This notebook will be your **draft notebook** for expermentations

* Once you have a new notebook open, be sure to:
   * **Rename** the notebook to something that makes sense: "DRAFT - Pokemon Type and Power Analysis"
   * **Delete** the first auto-generated code cell, you don't need any of the auto-generated stuff

* Now, add a Markdown cell and:
   * Write the title of your project and a short summary
   * This is a good chance to practice some basic Markdown
   * Write a data dictionary for your data in the Markdown cell (You can optionally create another Markdown cell for the data dictionary)
   * You'll eventually add more information to this initial explanatory section later

* Load your data set into the Notebook
   * Remember that it's in `../input/data-set-name/file-name.csv`
      * Substitute your own `data-set-name` and `file-name`, of course
   * Make sure the data can load properly without errors

* Do some basic examination of your data with the Pandas methods you've learned so far
   * Check out the shape, the columns, the data types
   * Try using `.describe()`
   * Is there any missing data?
      * Use the techniques you've learned in class to identify missing data
      * Document which columns have missing data. Think about why the data is missing
      * Start thinking about a plan to deal with missing data, you'll start dealing with it soon
   * Is there any inconsistent data? Weird strings with `\n`'s or extra spaces in them?
      * Document where the data is inconsistent/strange
      * Start thinking about a plan to deal with these inconsistencies, you'll start dealing with it soon

* Start *framing* the problem -- This is Step 1 of the Data Science Workflow
   * Which columns are interesting? Which columns are not? Make a list and document these ideas
   * Start to think about what interesting information you may be able to get out of this data. Document your ideas
   * Make a list of **what you know**
   * Make a list of **what you don't know**
   * Make a list of possible problem statements
      * Try to come up with *5-10* of them if possible
      * You will decide on which ones to explore later, but for now brainstorm as much as you can

* Take your data-cleanup plan and implement it. This is *data preparation*, Step 2 of the Data Science Workflow
   * The goal is develop the *minimal amount* of code that will clean up your data correctly
      * Make sure your code reliably reproduces the same effect every time you run it
   * Frequently click on "Run all cells" and make sure all your code continues to work as you expect!
   * You don't have to do a perfect job here, as you'll no doubt have to *iterate* on this process

### For **Advanced Students** Only

* If you need data from multiple CSVs, it's certainly possible, but talk to the instructor first
   * Multiple CSVs will not be considered for beginner students

---

# It should start to feel like you're going into the Matrix...

![](https://media.giphy.com/media/A06UFEx8jxEwU/giphy.gif)
