import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Nirvana lyrics from JSON file
def load_lyrics():
    with open("nirvana_lyrics.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

nirvana_lyrics_dict = load_lyrics()

# Preprocess lyrics for similarity search
vectorizer = TfidfVectorizer()

# Flatten the lyrics (combine all lines into a single list)
all_lyrics = []
all_song_titles = []

for song, lyrics in nirvana_lyrics_dict.items():
    for line in lyrics:
        all_lyrics.append(line)
        all_song_titles.append(song)

# Create the TF-IDF matrix for the individual lines
tfidf_matrix = vectorizer.fit_transform(all_lyrics)

# Define a threshold for similarity
SIMILARITY_THRESHOLD = 0.2  # You can adjust this threshold as needed

def find_best_match(user_input):
    """Finds the most similar Nirvana lyric line based on user input."""

    # Special case for "david pham"
    if "david pham" in user_input.lower():
        return "And when the screams won't end,\nYou find your peace again, \nDavid Pham, you’re all we see, \nBut in the end, you’ll just be free."
    
    if "who are you" in user_input.lower():
        return "My name is Kurt CoBOT. I take your messages and find matching Nirvana lyrics!"
    
    # Transform the user input
    user_vec = vectorizer.transform([user_input])
    
    # Calculate similarities between user input and all lyric lines
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()
    
    # Get the index of the most similar line
    best_match_idx = np.argmax(similarities)

    # Check if the best match has a similarity above the threshold
    if similarities[best_match_idx] < SIMILARITY_THRESHOLD:
        return "Hold your Teen Spirit, buddy. No lyrics match what you're saying. - Kurt CoBOT"

    # Get the corresponding song title and the matching lyric line
    best_song = all_song_titles[best_match_idx]
    best_line = all_lyrics[best_match_idx]

    # Find the previous and next lines for context
    prev_line = all_lyrics[best_match_idx - 1] if best_match_idx > 0 else None
    next_line = all_lyrics[best_match_idx + 1] if best_match_idx < len(all_lyrics) - 1 else None

    # Build a snippet with context (previous, current, and next line)
    context = ""
    if prev_line:
        context += f"{prev_line}\n"
    context += f"{best_line}\n"
    if next_line:
        context += f"{next_line}"

    return context