# little-help-book-py

A python program that implements an API endpoint that let's you generate and download: 

* the static data for little help book
* the mailmerge files used by Whitebird for generating the printed book

The webpage displays a list of the expected files. The ones that exist are presented as a clickable download link, along 
with the date they were generated. For the ones that are not present, it indicates that they don't exist. 

Pressing the `Generate` button runs the `get_table.py` program that generates the above. After pressing the button, you get
feedback as the above list of files is updated. They should then all show as exsiting, with the date reflecting the present time. 
(Otherwise something went wrong, which could be anything from Airtable being down to a bug in the present code.) 

# The code

* __endpoint.py__ generates and serves the webpage
* __get_table.py__ the program from little-help-book-web that generates the static data and mailmerge files

# todo

Edit the kubernetes file and deploy on MVP. 
