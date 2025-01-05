# Nested dictionary
nested_dict = {
    "fictions": {
        "Harper Lee": "To Kill a Mockingbird",
        "George Orwell": "1984"
    },
    "non-fiction": {
        "Yuval Noah Harari": "Sapiens",
        "Michelle Obama": "Becoming"
    }
}

# List to store keys
all_keys = []

# Iterate over the outer dictionary
for genre, books in nested_dict.items():
    all_keys.append(books)  # Append outer keys
    for author in books.keys():  # Append nested keys
        all_keys.append(author)

print(all_keys)

