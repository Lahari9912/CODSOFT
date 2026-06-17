import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")

# Combine features
df["content"] = df["genre"] + " " + df["description"]

# Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["content"])

# Compute similarity
similarity = cosine_similarity(tfidf_matrix)

# Recommendation function
def recommend(movie_name):
    if movie_name not in df["title"].values:
        print("Movie not found in dataset!")
        return

    index = df[df["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))

    # Sort movies based on similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended movies for '{movie_name}':\n")

    # Show top 5 recommendations
    for i in scores[1:6]:
        print(df.iloc[i[0]]["title"])

# Main program
if __name__ == "__main__":
    print("🎬 Movie Recommendation System")
    print("Available movies:\n")
    print(df["title"].to_string(index=False))

    while True:
        user_input = input("\nEnter a movie name (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        recommend(user_input)
        
