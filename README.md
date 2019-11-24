<h2>QuiverToWeb</h2>


This is a blog template made with the aim of mirroring [Quiver](https://happenapps.com/%29)'s appearance on a web page. It was based on a nice simple web template from [Truong Tran](https://codepen.io/truongtx-ccvn/pen/qLXGKV) and I added extra javascript code and python code so that it can accommodate Quiver html files seamlessly with little effort on the user side.

![enter image description here](https://i.imgur.com/FLkHTu0.gif)

The backside was written in <b>[Python 3](https://www.python.org/downloads/)</b> with <b>[Flask](http://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)</b> framework, so these should be installed before running the app. 

You can run the app as it is with included my notebooks, but of course we want to show yours not mine! So here's the instruction.

###  Instructions

1. ### Make sure you have Python 3 and Flask installed

2. ### Convert your notebook to html 

At the moment, Quiver doesn't support converting multiple notebooks at once so you need to individually convert your notebooks within the app. It also doesn't support nesting of notebooks but I added a way to make a group of notebooks as the alternative.
◦ Right-Click the notebook → "Export Notebook" → "As HTML" <br /> 

You will see an exported folder titled to follow the notebook name which has all notes converted into html files. What I refer as notebooks from now refers to this notebook folder.

3. ### Place the exported notebooks inside either `static/categories` or `static/notebook` .

	•  `static/categories`

The `static/categories` folder is for notebooks that you want to put together. Notebooks will show up under collapsible lists.


![enter image description here](https://i.imgur.com/6qiROvQ.gif)


You must <b>make a new directory inside the `categories` directory first</b> and then put related notebooks inside the new folder, because we want to have a title for the grouped notebooks! 

For example, make a directory named `javascript` inside `categories` folder and put javascript related notebooks like `grammar` and `usage` inside it.  `grammar` and `usage` will show up under the collapsible element `javascript`. It supports one-level hierarchy only.


![enter image description here](https://i.imgur.com/3qAb98d.png)


	• `static/notebook`

Put exported notebook that belong to a category inside `static/notebook`. It will show up as one of the lists you see on the side bar. There should be at least one notebook folder in `notebook` ou don't need to have a category, but there should be at least one 
 
4. ### Run the app

Run `app.py` within the project directory. First time you run the app, it edits style of html files you put inside `static/categories` and `static/notebook` with `cssEditor` module and then collect notebook lists to show. 

Once you run the app, you want to comment out  `cssEditor()`   in `app.py` to avoid editing css styles multiple times although it won't cause any crash.

```
if __name__ ==  '__main__':
	# Comment out cssEditor() except for the first run
	cssEditor()
	...
```

### Things that I hope to add in the future

• There must be at least one notebook folder inside `static/notebook` which isn't elegant. <br />
• When you click one of the notebooks on the sidebar, javascript will pass data about how much you scrolled within the sidebar and show the sidebar exactly how you left when a new page is loaded. But this doesn't work when you clicked one of the notebooks within a category yet :/ <br />
• For some reason, when you run this app on Chrome or Firefox, the sidebar doesn't have the nice, default over-scroll animation you see on Safari. <br />
• I want to turn it as robust as possible so that it doesn't crash due to just one or two things missing.  <br />
