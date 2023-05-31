
Backend consisting of flask for defining a custom REST API, and SQLite for storage. Ran on localhost for my foodpath app (react native expo). Frontend is in a private repository.

# Demos
Frontend + backend:
(in-progress)

Backend (Reccomendation system GUI):
<img src='.gif' width=1000 title='Reccomendation system GUI' width='' alt='Video Walkthrough' />


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

# running
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

logs.py:
- [ ]

recsys.py:
- [ ]

users.py:
- [ ]

other:
- [ ] 

# recsys info:
Modification of 
https://github.com/frason88/Diet-Recommendation-System- to make it work with our app, backend data sources, etc. 
"The module works on the basis of K-Means Clustering and Random Forest Classification Algorithms."
