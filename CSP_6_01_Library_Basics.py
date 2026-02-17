#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)
import analytics



# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    updated =[]
    for price in rawPrices:
        amount = analytics.apply_markup(price,0.15)
        amount = round(amount, 1)
        updated.append(amount)
    return updated

# Modify the below function such that it asks the user for n scores and then returns the highest score and
# the average score of the list.
def analyze_scores(n:list):
    highest = n[0]
    sum = 0
    for items in n:
        sum += items
        if highest< items:
            highest =items

    return [highest, sum/len(n)]


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(usernames):
   analyics = analytics.clean_text(usernames)
   usernames = []
   for i in usernames:
       cleaned = name.replace(" ", "").lower()
       usernames.append(cleaned)
   return analyics


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(nums):
    numbers = analytics.filter_threshold(nums,100)
    num = []
    for i in nums:
        if i > 100:
            num.append(i)
    return num


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case words with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items, target):
    # Sanitize the list
    items = [str(item).strip().lower() for item in items]
    target = str(target).strip().lower()

    # Check if list is in order
    in_order = True
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            in_order = False
            break

    # If sorted do Binary Search
    if in_order:
        left = 0
        right = len(items) - 1

        while left <= right:
            mid = (left + right) // 2
            if items[mid] == target:
                return mid
            elif items[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # If not sorted do Linear Search
    else:
        for index, item in enumerate(items):
            if item == target:
                return index
        return -1
