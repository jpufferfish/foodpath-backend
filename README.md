https://github.com/jpufferfish/foodpath-backend

[In-progress]: Backend using flask for defining a custom REST API, and SQLite for storage. Ran on localhost for my meal recommendation app (react native expo). Frontend is in a private repository.

# Demos
Frontend + backend:
(in-progress)

Recommendation system:
<img src='demos/recsys_gui1.gif' width=1000 title='Reccomendation system GUI' width='' alt='Video Walkthrough' />

# installing packages on mac (might not be all of them)
```
brew install --cask miniconda
pip install -r requirements.txt
pip3 install pipreqs
pip3 install pip-tools 
conda install pandas   
conda install ipython
pip install wheel
pip install pandas
pip install sklearn
pip3 install -U scikit-learn scipy matplotlib
```

# running server
```
cd src
python3 app.py
```

# testing to see what recsys.py does visually:
```
cd recsys-gui
python3 recsys_gui1.py
```

TODO:
put x in each box (no spaces) when done

users.py:
- [ ] user updates such as pw changes, deletion, etc
- [ ] https connection (e.g user registration POST w/ password)

history.py:
- [ ] majority is broken ATM
- [ ] programatically appending food data to the csv to improve the recsys
- [ ] try to rename 'history' to 'logs'(?)
- [ ] split up csv's by meal type, and consider what csv's strengths qre over sql (can eaily view their own food data?)


recsys.py:
- [ ] 

other:
- [ ] split sqlite tables into separate .db files
- [ ] sort out CORS usage
- [ ] pytest or unittest
- [ ] debug environment variables
- [ ] programatically assign sqlite3 conn's to values derived from .sql files

# recsys info:
Modification of 
https://github.com/frason88/Diet-Recommendation-System- to make it work with our app, backend data sources, etc. 
"The module works on the basis of K-Means Clustering and Random Forest Classification Algorithms."
