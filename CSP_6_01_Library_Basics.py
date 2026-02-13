import analytics


def process_expenses(cost_list):
    updated = analytics.add_percentage(cost_list, 15)
    return [round(x, 2) for x in updated]


def analyze_scores(count):
    values = []
    for _ in range(count):
        values.append(float(input()))
    top = analytics.highest_value(values)
    avg = analytics.average_value(values)
    return top, avg


def sanitize_usernames(name_list):
    return [analytics.remove_spaces_lower(x) for x in name_list]


def identify_outliers(data_points):
    return analytics.filter_above_threshold(data_points, 100)


def search_and_report(entries):
    cleaned = [analytics.remove_spaces_lower(x) for x in entries]
    target = analytics.remove_spaces_lower(input())

    if analytics.is_sorted(cleaned):
        return analytics.binary_search(cleaned, target)
    else:
        return analytics.linear_search(cleaned, target)


