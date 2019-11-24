import re
import os

# Change CSS of notebooks inside a directory
def editCss(path):
    notebooks = []
    # Get lists of notebook inside the directory
    for i, files in enumerate(next(os.walk(path))): 
        if i == 1:
            notebooks.extend(files)
    for notebook in notebooks:
        notes = None
        # get lists of note inside a notebook
        for i, files in enumerate(next(os.walk(path + "/" + notebook))):  
            if i == 2:
                notes = files
        # change style of notes
        for note in notes:
            try:
                with open(path + "/" + notebook + "/" + note, "r+", errors='ignore') as f: 
                    contents = f.read()
                    contents = re.sub("body{margin:0 auto;max-width:800px;line-height:1.4}", "body{margin:3vw 5vw 5vw 5vw;max-width:100%;line-height:1.8;color:#C7C7C7} a {cursor: pointer;color:#5D689A;} .ace_line {line-height:1.45}", contents)
                    contents = re.sub(".text-cell {font-size: 15px;}.code-cell {font-size: 12px;}.markdown-cell {font-size: 15px;}.latex-cell {font-size: 15px;}", ".text-cell {font-size: calc(14px + 0.2vh);}.code-cell {font-size: calc(12px + 0.2vh);}.markdown-cell {font-size: calc(12px + 0.2vh);}.latex-cell {font-size: calc(12px + 0.2vh);}", contents)
                    f.seek(0)                                                      
                    f.write(contents)
                    f.truncate()
            except:
                print("Error at " + path + "/" + notebook + "/" + note)

# Replace " " in a folder
def replaceBlankToDollar(path):
    for i, files in enumerate(next(os.walk(path))):
        if i == 0:
            dirpath = files
        if i == 1:
            for idx in range(len(files)):
                new_name = files[idx].replace(' ', 'PRC')
                os.rename(os.path.join(dirpath, files[idx]), os.path.join(dirpath, new_name))
                
def cssEditor():
    paths = ['./static/notebook']
    replaceBlankToDollar('./static/categories')
    for i, files in enumerate(next(os.walk('./static/categories'))):
        if i == 1:
            categories = ['./static/categories/' + notebook for notebook in files]
    paths.extend(categories)
    for path in paths:
        replaceBlankToDollar(path)
        editCss(path)

