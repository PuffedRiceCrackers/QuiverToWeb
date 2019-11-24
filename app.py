from flask import Flask, render_template, send_from_directory, request
import os, os.path
import json
from editstyle import cssEditor

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

##################customize#################
YOUR_BLOG_NAME = "Puffed\nRice\nCracker"
YOUR_TAB_NAME = "Puffed Rice Cracker"
DEFAULT_NOTEBOOK_NAME = "ChromePRCextension"
############################################

categories = []
category_notebooks = []
notebooks = []
categoryDict = {}
notebookDict = {}
categoryTitleDict = {}
notebookTitleDict = {}

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def main(path):
    global YOUR_BLOG_NAME
    global DEFAULT_NOTEBOOK_NAME

    global categories
    global category_notebooks 
    global notebooks 
    global categoryDict 
    global notebookDict 
    global categoryTitleDict 
    global notebookTitleDict 

    # Set notebook as default value when first visited
    if not path:
        path = notebooks[0][0] if not DEFAULT_NOTEBOOK_NAME else DEFAULT_NOTEBOOK_NAME
        isInCategory = "false"
    else:
        isInCategory = request.args.get("isInCategory")

    # Set path
    if isInCategory == "true":
        currCategory = request.args.get("category")
        postTitle = categoryTitleDict[currCategory].get(path)
        postSource = categoryDict[currCategory].get(path)
    else:
        postTitle = notebookTitleDict.get(path)
        postSource = notebookDict.get(path)

    # render template
    return render_template(
        "index.html",
        yourTabName=YOUR_TAB_NAME,
        yourBlogName=YOUR_BLOG_NAME,
        currNoteBook=path.replace('PRC', ' '),
        verticalPos=request.args.get("verticalPos") if request.args.get("verticalPos") != None else 1,
        categories=categories,
        category_notebooks=category_notebooks,
        lastOpenedCategory=request.args.get("lastOpenedCategory"),
        lastOpenedNotebook =request.args.get("lastOpenedNotebook"),
        notebooks=notebooks,
        postTitle=postTitle,
        firstPage=postSource[0],
        postSource=json.dumps(postSource))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Uncomment this when you need to edit index.html to block caching
# @app.after_request
# def after_request(response):
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response

def getSidebarList():
    # Collect lists to show on sidebar
    global categories 
    global category_notebooks 
    global notebooks

    # (1) Get Category Lists
    categories = os.listdir("./static/categories")
    try:
        categories.remove(".DS_Store")
    except:
        pass
    categories = [[item.replace('PRC', ' '), item] for item in categories]

    # (2) Get notebook lists inside a category
    category_notebooks = []
    for _, category_dir_name in categories:
        inside_category = os.listdir(f"./static/categories/{category_dir_name}")
        try:
            inside_category.remove(".DS_Store")
        except:
            pass
        inside_category = [[item.replace('PRC', ' '), item] for item in inside_category]
        category_notebooks.append(inside_category)

    # (3) Get notebook lists that don't belong to a category
    notebooks = os.listdir("./static/notebook")
    try:
        notebooks.remove(".DS_Store")
    except:
        pass
    notebooks = [[item.replace('PRC', ' '), item] for item in notebooks]

def helper(path):
    posts = os.listdir(path)
    try:
        posts.remove("index.html")
        posts.remove("resources")
        posts.remove(".DS_Store")
    except:
        pass
    return list(enumerate(posts))

def getPath():
    global categoryDict
    global notebookDict
    global categoryTitleDict 
    global notebookTitleDict

    # Category
    for i in range(len(categories)):
        category = categories[i][1]
        notebooksInsideCategory = [ntb[1] for ntb in category_notebooks[i]]
        postPathOfNotebooks = []
        titleOfPosts = []
        for notebook in notebooksInsideCategory:
            posts = helper("./static/categories/" + category + "/" + notebook)
            titleOfPosts.append([[item[0], item[1].replace('.html', '')] for item in posts])
            postPathOfNotebooks.append(["./static/categories/" + category + "/" + notebook + "/" + item[1] for item in posts])  # ["./static/iframefile/data structure/index.html"]
        categoryTitleDict[category] = { k:v for k,v in zip(notebooksInsideCategory, titleOfPosts)}
        categoryDict[category] = {k: v for k, v in zip(notebooksInsideCategory, postPathOfNotebooks)}

    # Notebook
    for i in range(len(notebooks)):
        currNtb = notebooks[i][1]
        posts = helper("./static/notebook/" + currNtb)
        notebookTitleDict[currNtb] = [[item[0], item[1].replace('.html', '')] for item in posts]
        notebookDict[currNtb] = ["./static/notebook/" + currNtb + "/" + item[1] for item in posts]


if __name__ == '__main__':

    # This will edit the style of htmls so use it only once
    #cssEditor()

    getSidebarList()
    getPath()

    app.run()



# categories=[['Python', 'Python'], ['Swift', 'Swift'], ['Javascript', 'Javascript']]

# category_notebooks=[[['    기본', 'PRCPRCPRCPRC기본'], ['    flask, jinja', 'PRCPRCPRCPRCflask,PRCjinja'], ['    data structure', 'PRCPRCPRCPRCdataPRCstructure'], ['    class', 'PRCPRCPRCPRCclass'], ['    pandas', 'PRCPRCPRCPRCpandas'], ['    실제개발', 'PRCPRCPRCPRC실제개발'], ['    scraping', 'PRCPRCPRCPRCscraping'], ['    function', 'PRCPRCPRCPRCfunction'], ['    개념', 'PRCPRCPRCPRC개념'], ['    sqlalchemy orm', 'PRCPRCPRCPRCsqlalchemyPRCorm']], [['    문법+', 'PRCPRCPRCPRC문법+'], ['    udemy course', 'PRCPRCPRCPRCudemyPRCcourse'], ['    문법', 'PRCPRCPRCPRC문법'], ['    data structure', 'PRCPRCPRCPRCdataPRCstructure'], ['    class', 'PRCPRCPRCPRCclass'], ['    xcode', 'PRCPRCPRCPRCxcode'], ['    개념', 'PRCPRCPRCPRC개념']], [['    문법', 'PRCPRCPRCPRC문법'], ['    활용', 'PRCPRCPRCPRC활용']]]

# notebooks=[['algorithm', 'algorithm'], ['Chrome extension', 'ChromePRCextension'], ['data structure', 'dataPRCstructure'], ['programming', 'programming']]




# posts = [(0, 'Sort_Insertion.html'), (1, '기본.html'), (2, 'BFS.html'), (3, 'Heap 문제.html'), (4, 'DFS.html'), (5, 'Divide and Conquer.html'), (6, 'While 신중히 쓰기.html'), (7, 'Dynamic Programming.html'), (8, 'Greedy.html'), (9, 'tail recursion.html'), (10, 'Recursion.html'), (11, 'Sort_Quick.html'), (12, 'binarySearch.html'), (13, 'Sort_Merge.html')]

# postTitle = [[0, 'Sort_Insertion'], [1, '기본'], [2, 'BFS'], [3, 'Heap 문제'], [4, 'DFS'], [5, 'Divide and Conquer'], [6, 'While 신중히 쓰기'], [7, 'Dynamic Programming'], [8, 'Greedy'], [9, 'tail recursion'], [10, 'Recursion'], [11, 'Sort_Quick'], [12, 'binarySearch'], [13, 'Sort_Merge']]

# postSource = ['./static/notebook/algorithm/Sort_Insertion.html', './static/notebook/algorithm/기본.html', './static/notebook/algorithm/BFS.html', './static/notebook/algorithm/Heap 문제.html', './static/notebook/algorithm/DFS.html', './static/notebook/algorithm/Divide and Conquer.html', './static/notebook/algorithm/While 신중히 쓰기.html', './static/notebook/algorithm/Dynamic Programming.html', './static/notebook/algorithm/Greedy.html', './static/notebook/algorithm/tail recursion.html', './static/notebook/algorithm/Recursion.html', './static/notebook/algorithm/Sort_Quick.html', './static/notebook/algorithm/binarySearch.html', './static/notebook/algorithm/Sort_Merge.html']


# posts = [(0, 'option page.html'), (1, 'Inject Script.html'), (2, 'incognito.html'), (3, 'Untitled Note.html'), (4, 'icon.html'), (5, 'Overview.html'), (6, 'option page, pop up.html'), (7, 'chrome events.html'), (8, 'listening event 추가하기.html'), (9, 'chrome.storage.html'), (10, 'user interface.html'), (11, 'add short cut.html'), (12, 'Declarative Content API.html'), (13, 'extension   event based programs.html'), (14, 'chrome api 와 asynchronous.html'), (15, 'manifest.json.html'), (16, 'Content Script.html'), (17, 'chrome.tabs..html')]

# postTitle = [[0, 'option page'], [1, 'Inject Script'], [2, 'incognito'], [3, 'Untitled Note'], [4, 'icon'], [5, 'Overview'], [6, 'option page, pop up'], [7, 'chrome events'], [8, 'listening event 추가하기'], [9, 'chrome.storage'], [10, 'user interface'], [11, 'add short cut'], [12, 'Declarative Content API'], [13, 'extension   event based programs'], [14, 'chrome api 와 asynchronous'], [15, 'manifest.json'], [16, 'Content Script'], [17, 'chrome.tabs.']]

# postSource = ['./static/notebook/ChromePRCextension/option page.html', './static/notebook/ChromePRCextension/Inject Script.html', './static/notebook/ChromePRCextension/incognito.html', './static/notebook/ChromePRCextension/Untitled Note.html', './static/notebook/ChromePRCextension/icon.html', './static/notebook/ChromePRCextension/Overview.html', './static/notebook/ChromePRCextension/option page, pop up.html', './static/notebook/ChromePRCextension/chrome events.html', './static/notebook/ChromePRCextension/listening event 추가하기.html', './static/notebook/ChromePRCextension/chrome.storage.html', './static/notebook/ChromePRCextension/user interface.html', './static/notebook/ChromePRCextension/add short cut.html', './static/notebook/ChromePRCextension/Declarative Content API.html', './static/notebook/ChromePRCextension/extension   event based programs.html', './static/notebook/ChromePRCextension/chrome api 와 asynchronous.html', './static/notebook/ChromePRCextension/manifest.json.html', './static/notebook/ChromePRCextension/Content Script.html', './static/notebook/ChromePRCextension/chrome.tabs..html']




# category dict
