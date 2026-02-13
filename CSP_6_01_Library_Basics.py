import analytics


# Takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    # Uses analytics function
    return analytics.add_percentage(rawPrices, 15)


# Asks the user for n scores and returns the highest and average score
def analyze_scores(n):
    scores = []

    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    highest = analytics.highest_value(scores)
    average = analytics.average_value(scores)

    return highest, average


# Takes in a list of strings and returns list with spaces removed and lowercase
def sanitize_usernames(usernames):
    sanitized = []

    for name in usernames:
        cleaned = analytics.remove_spaces_lower(name)
        sanitized.append(cleaned)

    return sanitized


# Takes in a list and returns a list of all values over 100
def identify_outliers(values):
    return analytics.filter_above_threshold(values, 100)


# Takes in list of items, sanitizes list, asks user for item to search,
# Uses binary search if sorted, linear search if not
def search_and_report(items):
    sanitized_list = []

    for item in items:
        cleaned = analytics.remove_spaces_lower(item)
        sanitized_list.append(cleaned)

    search_item = input("Enter item to search for: ")
    search_item = analytics.remove_spaces_lower(search_item)

    if analytics.is_sorted(sanitized_list):
        return analytics.binary_search(sanitized_list, search_item)
    else:
        return analytics.linear_search(sanitized_list, search_item)
