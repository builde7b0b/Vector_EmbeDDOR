from flask import Flask, request, jsonify, render_template
from gensim.models import Word2Vec
import pandas as pd


app = Flask(__name__)



data = pd.read_csv('product_descriptions.csv')


# Load the pre-tained Word2Vec model 
model = Word2Vec.load("word2vec.model")

def get_document_vector(query, model):
    # Get the dimensionality of the word vectors 
    vector_dimensionality = model.vector_size 

    # Create a placeholder vector of zeroes with the same dimensionality 
    return [0.0] * vector_dimensionality



@app.route('/')
def index():
    return render_template('UI.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.json['query']

    # Get the vector representation of the query 
    query_vector = get_document_vector(query, model)

    # Calculate similarity with all product descriptions 
    similarities = data.apply(lambda row: model.wv.cosine_similarities(query_vector, [row['description']])[0], axis=1)

    # Sort and get top recommendations 
    recommended_indices = similarities.argsort()[::-1][:5]
    recommendations = data.loc[recommended_indices, 'description'].tolist()

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run()