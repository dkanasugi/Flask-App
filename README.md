<h1>Flask-App</h1>
Python 3 Project that utilizes Flask app on a local device (http://127.0.0.1:5000/). 
There are given pictures that are randomized and when you click on the image from the main page, it 
will take you to another page and print results the mode (RGB, Greyscale, etc.),
type (JPEG, PNG, etc.), and the size (width and length) of the image.

I used PowerShell(admin) for this process.
These are the following Python packages that is required in the program:

1. Flask
2. Flask-Bootstrap
3. Image (PIL)

On PowerShell, the FLASK_APP and FLASK_ENV need to changed in the virtual environment for it to run. 
These are codes that I typed in for declaration/initalization on PowerShell.

Codes to for to run flask application:
<b> $env:FLASK_APP = "main.py"</b></br>
<b> $env:FLASK_ENV = "development" </b></br>
<b> flask run </b></br>

After the flask app is running, PowerShell will tell the location where the app is running on. I used Mozilla FireFox and 
copy and pasted http://127.0.0.1:5000/ onto the urlbar. 

Here are some pictures of the randomized pictures and examples of the output (mode, type, and size).

Main Page Screen Shot(1)</br>
![main1](https://user-images.githubusercontent.com/38510468/59983722-ff956980-95d7-11e9-9d04-e6b26b42598b.png)

Main Page Screen Shot(2)</br>
![main2](https://user-images.githubusercontent.com/38510468/59983727-15a32a00-95d8-11e9-80e4-6fca0197518d.png)

Result Page Screen Shot(1)</br>
![pic1](https://user-images.githubusercontent.com/38510468/59983741-22c01900-95d8-11e9-8e87-9b547e7cc586.png)
