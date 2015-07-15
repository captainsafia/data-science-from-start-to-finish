# Data Analytics with Python

The following tutorial is a Dexy documentation project containing a sequence of workshops designed to teach the fundamentals of data analytics using the Python stack.The series is divided into the following sections:

* Data Cleaning and Munging
* Exploring Timeseries Data with Pandas
* Visualizing Data in Python
* Exploratory Data Analytics with Pandas — Part I
* Exploratory Data Analytics with Pandas — Part II
* Logistic Regression with Sci-kit Learn 
* Clustering with Sci-kit Learn
* An Gentle Guide to the Data Science Community


## Collaborate

If you are interested in contributing your own bit to the curriculum, please take the follow steps.

1. Fork this repository into your Github user account.
2. Clone your forked repository into your computer using `git clone https://github.com/your-username/data-analytics-course.git`.
3. Create a new branch in the cloned repository for the change you would like to make using `git checkout -b change-i-am-making`.
4. Install dexy onto your machine using `pip install dexy`.
5. Add any shell commands that you use in your process to the appropriate shell file, for example `clean.sh`.
6. And any Python code used n your process to the appropriate Python file, for example `clean.py`.
7. Use the `### "section-name-here"` syntaxt to seperate out sections of your code in the files mentioned in steps 5 and 6.
8. Write out your process in the respective Markdown file, for example `cleaning.md`.
9. Use the `{{d['filename|idio']['section-name-here']}}` syntax to reference pieces of the code that you wrote in your files within the Markdown documentation.
10. Run `dexy setup && dexy` in order to generate the dexy docuemntation.
11. Change into the `output` directory and run the `python -m SimpleHTTPServer` to start a webserver in that directory.
12. Navigate to `http://localhost:8000` in your browser and open the respective HTML file, for example `cleaning.html`.
13. Repeat the above process as necessary.
14. Once you are finished, add and commit the files you changed using `git add`.
15. Commit them with a message describing the content that you added.
16. Push the changes into your branch using `git push origin change-i-am-making`.
17. Navigate to your forked Github repository and click "Compare and Pull Request" to request that your changes be merged into the main repository.
18. Rejoice!
