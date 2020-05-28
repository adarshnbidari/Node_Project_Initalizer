#buidling node app (express framework)


import os,webbrowser as wb

print("Version: 1.0.0.2")
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

const path=require('path');

const express = require('express');

const bodyParser = require('body-parser');

const cookieParser = require('cookie-parser');

//

const app = express();

//


//

app.use('/', express.static(path.join(__dirname, 'views')));

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

    print("Initalizing project: "+folderName+" ...")

    os.chdir(folderName)

    os.system("npm init -y")

    print("Installing dependencies , refer package.json for more information")

    os.system("npm i express hbs body-parser cookie-parser --save")

    print("Installation successfull :) ")

    print("Press Crtl-C to stop the server\n")

    wb.open('localhost')

    os.system("node index.js")

    
    


if folderName is not "":
    os.mkdir(folderName)
    proceed()
