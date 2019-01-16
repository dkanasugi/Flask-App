# Flask-App
A Python 3 Project that produces a flask app on a local device (http://127.0.0.1:5000/). 
The pictures are randomized from the dictionary and when you click on the picture, it 
will take you to another page on the browser and gives you the mode of the image (RGB, Greyscale, etc.),
type of image (JPEG, PNG, etc.), and the size (width and length) of the picture.

I used PowerShell(admin) and Python 3 to run the application. 
These are the following Python packages that is required in the program
1. Flask
2. Flask-Bootstrap
3. Image (PIL)

On PowerShell, the FLASK_APP and FLASK_ENV need to changed in the virtual environment for it to run. 
These are codes that I typed in for declaration/initalization

--------Code to for to run flask application----------
$env:FLASK_APP = "main.py"
$env:FLASK_ENV = "development"
flask run
------------------------------------------------------

After it is running, PowerShell will tell where it is running on. I used Mozilla FireFox and 
copy and pasted http://127.0.0.1:5000/ on the urlbar. 

Here are some pictures of the randomized pictures and examples of the output (mode, type, and size).
Main Page Example 1:
https://github.com/dkanasugi/Flask-App/blob/master/result_pics/main1.png

Result Page Example 1:
https://github.com/dkanasugi/Flask-App/blob/master/result_pics/pic1.png

Main Page Example 2:
https://github.com/dkanasugi/Flask-App/blob/master/result_pics/main2.png

Result Page Example 2:
https://github.com/dkanasugi/Flask-App/blob/master/result_pics/pic2.png
