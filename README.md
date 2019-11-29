<h1>QuiverToWeb</h1>


This is a blog template made with the aim of mirroring [Quiver](https://happenapps.com)'s appearance on a web page. It is based on a nice simple web template from [Truong Tran](https://codepen.io/truongtx-ccvn/pen/qLXGKV). With added javascript and python code, it can accommodate Quiver html files painlessly with little effort on the user side.

![enter image description here](https://i.imgur.com/FLkHTu0.gif)

The backside was written in <b>[Python 3](https://www.python.org/downloads/)</b> with <b>[Flask](http://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)</b> framework, so these should be installed before running the app. 

You can run the app as it is with the included notebooks of mine, but of course we want to show yours not mine! So here's the instruction.

<h2>Instructions</h2>
  
1. ### Make sure you have Python 3 and Flask installed  

2. ### Convert your notebook to html  

	At the moment, Quiver doesn't support converting multiple notebooks at once so you need to individually convert your notebooks within the app. It also doesn't support nesting of notebooks but I added a way to make a group of notebooks as the alternative.
◦ Right-Click the notebook → "Export Notebook" → "As HTML" <br /> 

	You will see an exported folder titled to follow the notebook name which has all notes converted into html files. What I refer as notebooks from now refers to this notebook folder.
  
3. ### Place the exported notebooks inside either `static/categories` or `static/notebook` .<br/>

<h4>• static/categories</h4>
	
This folder is for notebooks that you want to group together. Notebooks in this folder will show up under collapsible lists.
<p align="center">
<img src="https://i.imgur.com/6qiROvQ.gif" width="450" align="center"></p><br />	

<b>Make a new directory inside the `categories` folder first</b> and then put notebooks you want to group together in it.

For example, make a directory named `javascript` inside `categories` folder and put javascript related notebooks like `grammar` and `usage` inside it.  `grammar` and `usage` will show up under the collapsible element `javascript`. It supports one-level hierarchy only.<br /><br />

<p align="center">
<img src="https://i.imgur.com/3qAb98d.png" width="450" align="center"></img>
</p><br />

<h4>• static/notebook</h4>

Put notebooks that don't belong to a category inside `static/notebook`. It will show up as one of the lists you see on the side bar. <b>There should be at least one notebook folder in `static/notebook`</b>.
  
3. ### Customize the variables (Optional)
	#### `app.py`
	* `YOUR_BLOG_NAME` : The string you see at the top left of a page. 
	* `YOUR_TAB_NAME` : The string you see in the tab
	* `DEFAULT_NOTEBOOK_NAME`:
		This is the title of the notebook that you want to show when someone first visited your web site. 
        * Set this value as `None` and it will choose the first element of the notebook list it collected internally. 
        * If you want to set a specific notebook, there is this ugly but working approach.  <b>Replace any blank space in the target notebook title with the string `PRC`</b>. I had to find a string that no one would use in their notebook title and also does not fiddle with jQuery. Tried characters like #,$,% and more and just settled with this string.

	#### `index.html`
    
    Remove the `<div class="sidebar-header">` and its children if you want to get rid of the blue-yellow pebble like thing at the top right.
        
```python
##################customize#################
YOUR_BLOG_NAME = "Puffed\nRice\nCracker"
YOUR_TAB_NAME = "Puffed Rice Cracker"
DEFAULT_NOTEBOOK_NAME = "ChromePRCextension" # Chrome extension
############################################
```
  
4. ### Run the app  

	Run `app.py` within the project directory. First time you run the app, it edits style of html files you put inside `static/categories` and `static/notebook` with `cssEditor` module and then collect notebook lists to show. 

	Once you run the app, you want to comment out  `cssEditor()`   in `app.py` to avoid editing css styles multiple times although it won't cause any crash.<br /><br />

```python
if __name__ ==  '__main__':
	# Comment out cssEditor() after the first run
	cssEditor()
	...
```
<br />

### Things that I hope to improve in the future

<p>• Currently, at least one notebook inside static/notebook is required for the code to run, which isn't optimal.</p>
<p>
• It remembers where you left in the scrollable sidebar when you click a notebook and shows the sidebar exactly how you left it. This doesn't work with categories yet. </p>
<p>• Chrome/Firefox over-scroll and bounce effect isn't working in the sidebar.
</p>
<p>• Turning it as robust as possible so that it doesn't crash due to only one or two things missing.  </p>


