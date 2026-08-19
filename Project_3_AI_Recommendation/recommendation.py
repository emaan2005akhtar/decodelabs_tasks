# Project 3 - AI Recommendation Logic
# DecodeLabs

movies = [
    {
        "title": "Interstellar",
        "genres": {"sci-fi", "adventure", "drama"}
    },
    {
        "title": "The Matrix",
        "genres": {"sci-fi", "action", "thriller"}
    },
    {
        "title": "Avengers: Endgame",
        "genres": {"action", "adventure", "sci-fi"}
    },
    {
        "title": "The Notebook",
        "genres": {"romance", "drama"}
    },
    {
        "title": "Inception",
        "genres": {"sci-fi", "action", "thriller"}
    },
    {
        "title": "The Conjuring",
        "genres": {"horror", "thriller"}
    },
    {
        "title": "Jurassic Park",
        "genres": {"adventure", "sci-fi", "thriller"}
    }
]


def calculate_similarity(user_preferences, movie_genres):
    matched_preferences = user_preferences.intersection(movie_genres)

    if not user_preferences:
        return 0

    score = (len(matched_preferences) / len(user_preferences)) * 100
    return score


def get_recommendations(user_preferences):
    recommendations = []

    for movie in movies:
        score = calculate_similarity(user_preferences, movie["genres"])

        if score > 0:
            recommendations.append({
                "title": movie["title"],
                "score": score,
                "matched": user_preferences.intersection(movie["genres"])
            })

    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations


print("=" * 50)
print("       AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

user_input = input(
    "\nEnter your interests separated by commas "
    "(e.g., action, sci-fi, adventure): "
)

user_preferences = {
    preference.strip().lower()
    for preference in user_input.split(",")
    if preference.strip()
}

if not user_preferences:
    print("\nPlease enter at least one valid interest.")
else:
    recommendations = get_recommendations(user_preferences)

    print("\nRecommended Movies:")
    print("-" * 50)

    if recommendations:
        for index, recommendation in enumerate(recommendations, start=1):
            print(
                f"{index}. {recommendation['title']} "
                f"- Similarity Score: {recommendation['score']:.1f}%"
            )
            print(
                f"   Matched interests: "
                f"{', '.join(sorted(recommendation['matched']))}"
            )
    else:
        print("No matching movies found.")

print("\nThank you for using the recommendation system!")