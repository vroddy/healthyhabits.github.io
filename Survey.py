import random
def survey():
    questions = [
        "On average how long do you spend doing some form of exercise each day?",
        "On average how long do you spend studying each day?",
        "On average how long do you spend doing other recreational activities (such as watching tv, playing games, etc.) ?",
        "On a scale of 1-10 how would you rate your wellbeing overall, with 1 being absolutely terrible, 5 being neutral and 10 being amazingly positive. ",
        "Do you ever find yourself having trouble balancing your school work with other activities?",
        "When you keep a reminder, do your prefer writing it down on your school diary, or setting a calendar event on your computer?",
        "How much do you rely on daymap and your school diary?"
    ]
    options = [
        ["No time at all", "1-2 hours", "3-4 hours","5 hours+"],
        ["No time at all", "1-2 hours", "3-4 hours","5 hours+"],
        ["No time at all", "1-2 hours", "3-4 hours","5 hours+"],
        ["terrible","very bad", "bad", "anxious", "neutral", "somewhat positive", "generally optimistic", "positive", "very positive", "amazingly positive"],
        ["yes", "no"],
        ["Diary", "Computer", "Other"],
        ["Rarely", "Sometimes", "At least once a week", "All the time"],

    ]
    responses = []

    for index, question in enumerate(questions):
        print(f"Question {index + 1}: {question}")
        for i, option in enumerate(options[index]):
            print(f"{chr(i + ord('A'))}. {option}")
        choice = input("Enter your choice (A, B, C, etc.): ").upper()
        responses.append(choice)

    print("\nSurvey Results:")
    for index, question in enumerate(questions):
        selected_option = options[index][ord(responses[index]) - ord('A')]
        print(f"{question}: {selected_option}")

# Run the survey
print("Welcome to the survey, choose the option that you think fits best with you using the corresponding letters")
survey()
options = ['Plan 1', 'Plan 2', 'Plan 3']
random_choice = random.choice(options)

print("From the response to our survey, we strongly reccomend " +random_choice + " but you can always choose whatvever you think is best.") 
print("You can now close this tab, or return to the homepage")
