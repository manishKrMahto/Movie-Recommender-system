# library imports 
import streamlit as st 
import pickle 
import requests 

# loading important data from notebook
movies = pickle.load(open('movies.pkl' , 'rb') )
similarity = pickle.load(open('similarity.pkl' , 'rb')  )

recommend_no = 6  # number of movies should be recommend

def recommend_movies(movie_name):
    lst = []
    index = movies[movies['title'] == movie_name].index[0]
    for i in list(sorted(enumerate(similarity[index]) , reverse = True , key = lambda x : x[1]))[1:recommend_no + 1]:
        lst.append(movies.iloc[i[0]]['title'])
        
    return lst


def find_poster(movie_lst):
    poster = []
    director = []
    release = []
    runtime = []
    writer = []
    actors = []
    imdb = []
    api_key = 'de077cf7'
    for movie in movie_lst:
        url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"
        data = requests.get(url).json()
        poster.append(data['Poster'])
        director.append(data['Director'])
        actors.append(data['Actors'])
        release.append(data['Released'])
        runtime.append(data['Runtime'])
        writer.append(data['Writer'])
        imdb.append(data['imdbRating'])

    return poster , director ,actors , release , runtime , writer , imdb


def show_all_information():
    rec_movies = recommend_movies(movie)
    poster , director , actors, release , runtime , writer , imdb = find_poster(rec_movies)

    cols = st.columns(3)
    index = 0
    for i in range(3):
        cols[i].image(poster[index])
        cols[i].write(f'Movie : {rec_movies[index]}')
        cols[i].write(f'Director : {director[index]}')
        cols[i].write(f'Actors : {actors[index]}')
        cols[i].write(f'Writer : {writer[index]}')
        cols[i].write(f'Release Date : {release[index]}')
        cols[i].write(f'Runtime : {runtime[index]}')
        cols[i].write(f'IMDB Rating : {imdb[index]}')
        index = index + 1
        
        
    cols = st.columns(3)
    for i in range(3 ):
        cols[i].image(poster[index])
        cols[i].write(f'Movie : {rec_movies[index]}')
        cols[i].write(f'Director : {director[index]}')
        cols[i].write(f'Actors : {actors[index]}')
        cols[i].write(f'Writer : {writer[index]}')
        cols[i].write(f'Release Date : {release[index]}')
        cols[i].write(f'Runtime : {runtime[index]}')
        cols[i].write(f'IMDB Rating : {imdb[index]}')
        index = index + 1


if __name__ == '__main__':
    st.title('Movie Recommendation System')
    st.write('using content based filtering')
    movie = st.selectbox('choose movie to recommend ' , movies['title'])
    st.write(f' you choosen : {movie}')

    status = st.button('Recommend')

    if status:
        show_all_information()
