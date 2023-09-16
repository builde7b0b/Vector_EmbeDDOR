# Vector_EmbeDDOR





## Local Testing 

### Steps
1. Setup Virtual Environment
2. Install Dependencies 
3. Run App Locally 
4. Access pp 
5. Test with sample queries 
6. Verify Recommendations 
7. Review Logs 
8. Exit 



### Steps - In Depth 

Install Python and Dependencies (Pip etc.)
MacOS: brew install python 

Install PIP 

- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

- `python3 get-pip.py`

- `pip3 --version`

- `pip --version`


1. Setup Virtual Env
python -m venv venv 
source venv/bin/activate 

2. Install Dependencies 
pip install gensim Flask pandas nltk 

3. To Run the app, you must first generate some data 
python generate_dataset.py 

- Next, Pre-Process your data

`python data_preprocessing.py`

4. Word Embedding

`python Word_Embedding.py `


5. Finally, Serve your application using Flask

`python app.py`

- Open Browser to: http://127.0.0.1:5000/


### Things to Check: 
- Ensure you have a templates folder with your html files to be served.
