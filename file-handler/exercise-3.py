# Positive and negative words lists
positive_words = ["amazing", "enjoy", "breathtaking", "wonderful", "relaxed", "mesmerizing", "excellent", "fantastic", "unforgettable"]
negative_words = ["bad", "disappointing", "poor", "lackluster"]

# Provided sentences
sentences = [
    "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it.",
    "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun.",
    "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded.",
    "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor.",
    "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing.",
    "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce.",
    "The food on our trip was excellent. We sampled delicious local cuisine at every stop.",
    "The historical tour was enlightening. We learned so much about the culture and heritage of the region.",
    "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
]
with open("travel_blogs.txt", 'w') as file:
    for sentence in sentences:
        file.write(f"{sentence}\n")


# Initialize counts
positive_count = 0
negative_count = 0

# Iterate through each sentence
for sentence in sentences:
    sentence_lower = sentence.lower()
    

    for word in positive_words:
        if word in sentence_lower:
            positive_count += sentence_lower.count(word)

    for word in negative_words:
        if word in sentence_lower:
            negative_count += sentence_lower.count(word)

print("Positive words count:", positive_count)
print("Negative words count:", negative_count)
