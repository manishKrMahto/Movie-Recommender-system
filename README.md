# Movie Recommendation System

## Overview

This project implements a Movie Recommendation System using content-based filtering. The system recommends movies based on the similarity of their content to the movie selected by the user. The content includes genres, keywords, overview, production companies, countries, cast, and crew. The project also incorporates features like runtime, vote average, and popularity to enhance the recommendations.

## Features

- **Content-Based Filtering**: Recommends movies similar to the selected one based on their content.
- **Movie Metadata**: Uses information such as genres, keywords, overview, cast, crew, production companies, and countries.
- **Extended Features**: Incorporates additional features like runtime, vote average, and popularity to improve the recommendations.
- **Memory Optimization**: The system is optimized for memory usage, making it efficient even with large datasets.

## Dataset

The dataset used in this project includes metadata of 5000 movies from TMDB (The Movie Database). It consists of two CSV files:

- `tmdb_5000_credits.csv`: Contains information about the cast and crew.
- `tmdb_5000_movies.csv`: Contains detailed movie information such as genres, keywords, production companies, etc.

## Methodology

1. **Data Preprocessing**:
    - Merged the credits and movies datasets on the title.
    - Extracted relevant features from complex data structures (like lists of dictionaries).
    - Combined features into a single `tags` column.
    - Applied text preprocessing like removing spaces within multi-word tags.

2. **Vectorization**:
    - Used `CountVectorizer` to convert text data in the `tags` column into vectors.
    - Removed stop words and limited features to improve performance.

3. **Similarity Calculation**:
    - Calculated the cosine similarity between the vectors to measure the similarity between movies.
    - Added additional features (`runtime`, `vote_average`, `popularity`) to the vectorization process for a more refined similarity measure.

4. **Recommendation Function**:
    - Implemented a function to recommend the top 5 movies similar to the user-selected movie.
    - Extended the function to include additional features for enhanced recommendations.

5. **Memory Optimization**:
    - Converted similarity matrices to `float16` to reduce memory usage by 75%.

6. **Web Interface**:
    - Developed a web interface using Streamlit to allow users to interact with the recommendation system.
    - Integrated OMDB API to fetch movie posters, directors, actors, release dates, runtimes, writers, and IMDB ratings.

## Requirements

- Python 3.x
- Libraries:
  - numpy
  - pandas
  - scikit-learn
  - ast
  - pickle
  - requests
  - streamlit

## How to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/manishKrMahto/Movie-Recommender-system.git
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

4. **Interact with the System**:
    - Select a movie from the dropdown list.
    - Click on the "Recommend" button to get movie recommendations.

## Future Improvements

- Enhance the recommendation algorithm by integrating collaborative filtering.
- Add user ratings and reviews to improve recommendations.
- Improve the UI/UX of the web interface.
- Deploy the system on a cloud platform for wider accessibility.

## Acknowledgments

- TMDB for providing the movie dataset.
- OMDB API for providing additional movie details like posters and IMDB ratings.
- I took inspiration from a YouTube video by CampusX, hosted by Nitish Singh, for this project. A big thank you to him for his valuable insights! You can check out the video [here](https://www.youtube.com/watch?v=1xtrIEwY_zY&t=2s).