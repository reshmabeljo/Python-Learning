
#Step 1: Preloaded Feedbacks

feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)

#Step 2: Add More Feedbacks


def fnfeedbacks(X):
    index=1
    while(index<=Count):
          Name=input("Enter Name")
          Feedback=input("Enter Written Feedback")
          Rating=input("Enter Rating (1–5)")
          feedback_data["Name"].append(Name)
          feedback_data["Feedback"].append(Feedback)
          feedback_data["Rating"].append(Rating)
          feedback_data["S_No"].append(len(feedback_data["S_No"])+1)
          index+=1
    print(feedback_data)
         
Count=int(input("Enter how many more feedbacks want to add.")) 
    
fnfeedbacks(Count)


# Step 3: Text Cleaning

data=len(feedback_data["Feedback"])

#1.Remove punctuation (., ,, !, ?)

for i in range(data):
    for p in ".,!?":
        feedback_data["Feedback"][i] = feedback_data["Feedback"][i].replace(p, "")

#2.Replace multiple spaces with a single space

for i in range(data):
    feedback_data["Feedback"][i] = " ".join(feedback_data["Feedback"][i].split())

#3.Remove leading and trailing spaces

for i in range(data):
    feedback_data["Feedback"][i] = feedback_data["Feedback"][i].strip()


#4.Convert all text to lowercase


for i in range(data):
    feedback_data["Feedback"][i] = feedback_data["Feedback"][i].lower()


print(feedback_data["Feedback"])


#Step 4: Word Count Insights

def count_word_in_feedbacks(word):

     x=1
     for i in feedback_data["Feedback"]:
          if word.lower() in i.lower().split():
              x+=1

     return x

word = input("Enter a word: ")
result = count_word_in_feedbacks(word)

print("Number of feedbacks containing the word:", result)

#Step 5: Final Summary & Insights

#1.Display the final cleaned feedback_data (dictionary of lists).

print(feedback_data)

#2.Print the average rating from all feedbacks.

TotalRating = sum(feedback_data["Rating"])
TotalFeedbacks = len(feedback_data["Rating"])
Avg_rating = TotalRating / TotalFeedbacks

print("Average Rating:",Avg_rating)

#3.Find and display the feedback with the longest comment (in terms of word count).

longest_feedback = ""
max_words = 0

for feedback in feedback_data["Feedback"]:
    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("Longest Feedback:", longest_feedback)
print("Word Count:", max_words)


#4 Print the list of unique words used across all feedbacks (avoid duplicates).


unique_words = []

for feedback in feedback_data["Feedback"]:
    for word in feedback.split():
        if word not in unique_words:
            unique_words.append(word)

print("Unique Words:")
print(sorted(unique_words))


#): Sort feedbacks by rating (highest to lowest) using zip() and sorted(). Display the sorted entries.


data = list(zip(feedback_data["S_No"],
                feedback_data["Name"],
                feedback_data["Feedback"],
                feedback_data["Rating"]))

data = sorted(data, key=lambda x: x[3], reverse=True)

print("sorted entries")

for item in data:
    print(item)




