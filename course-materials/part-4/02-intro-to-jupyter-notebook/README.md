# Jupyter Notebook

<!--

## We Do: Launching Jupyter Notebook

Go into the `student` directory of this lesson. Note that there's already a file called `my-first-notebook.ipynb`. This is an "Interactive Python Notebook" file.

Now, let's try to open that file with Jupyter Notebook.

```zsh
jupyter notebook my-first-notebook.ipynb
```

And it should say something like:

```
pyenv: jupyter: command not found

The `jupyter' command exists in these Python versions:
  anaconda3-2020.11
```

See, currently we are using the latest version of plain-jane Python -- which does not have all of the data science tools installed, so we cannot launch `jupyter notebook` or any other data science tool. 

We *could* install the tools manually with `pip`, but it would take a very long time to manually install of the required modules.

The alternative is to install Anaconda (which comes with everything in the box), which we have already done. All we have to do is access it! This is where **Pyenv** comes in, which you might remember we installed way back at Installfest.

To run the Anaconda version of Python instead, do the following:

```zsh
pyenv local anaconda3-2020.11
```

You will notice that a new hidden file called `.python-version` has been created inside your `student` directory (you can see hidden files with the `ls -a` shell command).

If you `cat` the contents of `.python-version`, it only says `anaconda3-2020.11`.

What this file does is tell the Operating System: "*Hey, when we are inside this directory (or any subdirectory), use the Anaconda version of Python!*"

This is what **Pyenv** is good for! If you have a project using an older version of Python, for example, you can designate that directory with the older version, and the older version will be automatically used while inside that folder (and its subfolders!).

(If you exit the `student` folder with `cd ..`, you'll see that we revert to using plain Python again while in the parent directory.)

Let's get back to Jupyter Notebook. Make sure you're back in the `student` folder. If you try to launch Jupyter Notebook again:

```zsh
jupyter notebook my-first-notebook.ipynb
```

*wait...*

It opens in your browser! 

**Note:** Development environments between Mac and Windows differ, and there are different ways to open Jupyter Notebooks (Just like there are many ways to open any given file or program on your computer!), but this is the way we're going to do it... On the Command Line!
-->

## We Do: Launching Jupyter Notebooks on Kaggle

Let's head over to https://www.kaggle.com

* Click the <kbd>Code</kbd> link on the sidebar
* Click the <kbd>+ New Notebook</kbd> button
* Double click the random name at the top (like `notebookc5bb5efb78`) and rename the notebook to be `My First Notebook`

## We Do: Code Cells

Let's begin!

* There's already a cell that exists in the new notebook.

  Ignore what's there for now, we'll talk about it later. Delete all that, and write:

  ```python
  print('Hello World')
  ```

* Be sure your cursor is inside the cell. Press <kbd>Ctrl-Enter</kbd> to execute the code.

After a few seconds, you'll see `Hello World` outputted right below the cell. This is how you run a code cell!

* Create a new cell: Click <kbd>+ Code</kbd>. Enter:

  ```python
  my_list = [1, 2, 3]

  for i in my_list:
    print(i)
  ```

* `Ctrl-Enter` to run it

So you see that **Code Cells** can execute any Python code you put in it!

## We Do: Markdown Cells

Markdown cells allow you to write and format text.

* Make a cell: Click the <kbd>+ Markdown</kbd> button. This generates a **Markdown cell**

<!--
   * You're going to be doing this a lot!

* Change this cell to a markdown cell:
   * Click: `Cell` :arrow_right: `Cell Type` :arrow_right: `Markdown`
   * (Or you can click on a code cell and press <kbd>m</kbd>)
-->

* Inside the markdown cell, write:

  ```md
  # A Fantastic Title
  ```

  * Make sure there's a **space** between `#` and `A`!

* Run the cell: `Ctrl-Enter`. Bam! Pretty formatted text.
* If you want to update the markdown cell, double click it and you can update the text.

Here are some more levels of headings:

<pre>
# Heading 1

Some text

## Heading 2

Some text

### Heading 3

All the way to...

###### Heading 6

Some text
</pre>

You can also use `Shift-Enter` to execute the cell which will automatically create another new cell but it will always be a **Code Cell**, so you'll have to change it to a Markdown cell if you wish to write text. Right click and select **Change to Markdown Cell Type**.

Let's try some more commonly used Markdown syntax:

<pre>
**Bold**

_Italic_

* List Item
* Another List Item
   * A second leve list item

```python
print('Sample code')
```
</pre>

**Note**: We will not spend much time learning markdown syntax! Instead, take a look at the cheatsheet and links in Additional Resources.

When it comes to markdown, no one trys to memorize its syntax. Instead, reference the cheatsheets to review how to make large headers, bulleted lists, tables, and more. 

n apt analogy is a painter does not spend time memorizing pantones, but when he/she needs to do a paint job, they will look up the necessary color codes.

<!--
## We Do: Closing Down

* **Note**: Jupyter Notebook automatically saves your work as you execute cells. ***BUT***, before you close the notebook, click the :floppy_disk: icon to save your work, just in case!
   * ([What is that funny looking icon anyway?](https://www.distractify.com/p/save-icon-vending-machine))
* Now, close the tab in your browser
* That actually doesn't fully quit the Notebook program!
   * Jupyter Notebook is a **Client-Server** app
   * We've closed the Client-side, now we have to close the Server-side
* Open your Terminal where we first used the `jupyter notebook` command. You'll see that the process is still running
   * Hit <kbd>⌃ Control</kbd>+<kbd>c</kbd>
   * It should ask `Shutdown this notebook server (y/[n])?`
   * Enter `y`
* That will fully shutdown both the client and server sides of the Jupyter Notebook program
-->

## Miscellaneous

* You can **Re-run** your notebook with:
   * *Run* :arrow_right: *Run All*
   * Sometimes if you've made a ton of changes, you may have to: *Run* :arrow_right: *Restart & clear cell outputs*

---

# Why Jupyter Notebooks?

Jupyter Notebook is the preferred integrated development environment (IDE) of data science. Why?

## Data Science is Both Code and Methodology

As data scientists, the code we write is only half the story. The methodology, or manipulations, that we're applying on that data are -- are the other half.

Typically these methdologies are far more subjective in contrast to typical straight software development. So we need both code along with explanatory text. Jupyter Notebooks make it easy to create code cells next to text cells.

For example: Pretend we're missing many values in our data. Do you fill in missing values with the mean (average) or the median? The code for doing either of these operations is fairly easy compared to the subjective justifying decision, which should be documented in text cells.


<!--
## Connect to Remote Computing Resources

While we will not be doing this, but Jupyter Notebooks make it easy to connect to remote computers in datacenters. This is why the Jupyter Notebook is in your browser.

Basically we've created a website for one person: you, running on your computer. After we're done writing the code, we could in swap the brains from your laptop for stronger computers in a datacenter if we need to do more muscular processing. Wow!
-->

---

# Additional Resources

* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Interactive Markdown Cheatsheet](http://markdownlivepreview.com/)
* [Working with Markdown on Google Colab](https://colab.research.google.com/github/gitedio/examples/blob/master/Working%20With%20Markdown%20Cells.ipynb)
