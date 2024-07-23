import pickle 
import streamlit as st
import numpy as nm

st.header("Book Recommender System")

model = pickle.load(open("artifacts/model.pkl",'rb'))
book_name = pickle.load(open("artifacts/books_name.pkl",'rb'))
final_rating = pickle.load(open("artifacts/final_rating.pkl",'rb'))
book_pivot = pickle.load(open("artifacts/book-pivot.pkl",'rb'))


selected_books = st.selectbox(
    "Types or select a book",
    book_name
)

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])


def recommend_book(book_name):
    book_list = []
    book_id = nm.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    poster_url = fetch_poster(suggestion)  
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url        

if st.button('Show Recommendation'):
    recommendation_books,poster_url = recommend_books(selected_books)