# Evalucom_NHS
skill assessment for evalucom

* I made the application in Django, so navigate into the root folder (evalucom) and run python manage.py runserver to preview it

* Issues: 

I unfortunatley wasn't able to figure out how to make a POST request to the end point using Django, so instead I used the lightweight back end that Django provides to save the changes locally. If you were to make a change to the amount of vacant beds then it would reset if you changed pages. I did this because otherwise I would've had to have store all of the data for the API, and I wans't willing to do that.

when you try to change the value of the first item of the first page it moves to position 5.
