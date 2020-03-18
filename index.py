#buidling node app (express framework)


import os,webbrowser as wb

print("Version: 1.0.0.1")
print()
print('----------------')
print()
print('Author: Adarsh N Bidari')
print()

folderName=str(input("Enter the folder name\n"))
print("")

def proceed():
    
    setView()
    
    createIndexFile()

    initialize()




#utilities


def setView():
    os.mkdir(folderName+'/views')


def createIndexFile():

    IndexData="""
const express = require('express');

const bodyParser = require('body-parser');

const cookieParser = require('cookie-parser');

//

const app = express();

//


//

app.use(bodyParser.urlencoded({ extended: true }));

app.use(cookieParser());


app.set("view engine", "hbs");

//


app.get("/", (req, res) => {

    res.render('index');
});




app.listen(80, () => {

    console.log("Server is running at localhost");

});

    """
    ViewData="""

    <html>
    <head>
    <title>Works</title>
    </head>
    <body>
    <h1>App is running</h1>
    </body>
    </html>

    """
    
    
    index=open(folderName+"/index.js","w")

    index.write(IndexData)

    index.close()

    view=open(folderName+'/views/index.hbs',"w")

    view.write(ViewData)

    view.close()

def initialize():

    os.chdir(folderName)

    os.system("npm init -y")

    os.system("npm i express hbs body-parser cookie-parser --save")

    wb.open('localhost')

    os.system("node index.js")

    


if folderName is not "":
    os.mkdir(folderName)
    proceed()
