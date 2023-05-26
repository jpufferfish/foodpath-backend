
Backend consisting of flask for defining a custom REST API, ran on localhost for the foodpath app prototype (in react native expo). Frontend is in a private repository, so the result of it is shown below.

# Demos
Frontend + backend


Backend



# installing packages mac (might not be all of them)
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
python3 app.py
```

# testing to see what recsys.py does visually:
```
python3 recsys_gui1.py
```

TODO:
put x in each box (no spaces) when done

logs.py:
- [x] get sqlite code from # https://github.com/cs125-group53/foodpath/blob/master/previous-src/App.tsx, and integrate it
- [ ] 
- [ ]


recsys.py:
- [x] fix app.route()'s in rec_sys_api.py (refer to logs.py for examples?)
- [ ] add api endpoints, http request methods
- [ ]

users.py:
- [x] get sqlite code from # https://github.com/cs125-group53/foodpath/blob/master/previous-src/App.tsx, and integrate it

other:
- [ ] uhh where do we make calls to food api's?

# recsys info:
Heavy modification of 
https://github.com/frason88/Diet-Recommendation-System- to make it work with our app, backend data sources, etc. 
"The module works on the basis of K-Means Clustering and Random Forest Classification Algorithms."
