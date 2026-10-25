"""
College Help Desk Chatbot - Rule-based chatbot using if-else conditions.
Topic: College
Run: python college_chatbot.py
"""


def get_response(user_input):
    msg = user_input.lower().strip()

    if msg == "":
        return "Please type something so I can help you."
    elif msg in ("hi", "hello", "hey") or "good morning" in msg or "good evening" in msg:
        return "Hello! Welcome to the College Help Desk. How can I help you today?"
    elif "admission" in msg:
        return ("Admissions are open from June to August. Apply online on the college "
                "portal with your 12th marksheet, ID proof and photographs.")
    elif "course" in msg or "program" in msg:
        return ("We offer B.Tech (CSE, IT, ME, CE), BCA, BBA, B.Com, MCA and MBA programs.")
    elif "fee" in msg:
        return ("B.Tech: Rs. 1,20,000/year, BCA: Rs. 60,000/year, BBA: Rs. 55,000/year, "
                "MBA: Rs. 1,00,000/year. Fees can be paid in two installments.")
    elif "scholarship" in msg:
        return ("Merit scholarships are given to students scoring above 85%. "
                "Government scholarships are also available via the state portal.")
    elif "hostel" in msg:
        return ("Separate hostels for boys and girls are available with Wi-Fi, mess and "
                "24x7 security. Hostel fee is Rs. 70,000/year including food.")
    elif "library" in msg:
        return "The library is open 8:00 AM to 8:00 PM, Monday to Saturday, with 50,000+ books."
    elif "timing" in msg or "time" in msg or "hours" in msg:
        return "College timings are 9:00 AM to 4:00 PM, Monday to Saturday."
    elif "exam" in msg:
        return ("Mid-semester exams are held in October/March and end-semester exams in "
                "December/May. Check the portal for the exact timetable.")
    elif "result" in msg:
        return "Results are published on the college web portal within 30 days after exams."
    elif "placement" in msg or "job" in msg:
        return ("Our placement cell has 150+ recruiting companies. Highest package last year "
                "was 18 LPA and average was 4.5 LPA.")
    elif "canteen" in msg or "food" in msg:
        return "The canteen is open from 8:00 AM to 6:00 PM serving snacks and meals."
    elif "transport" in msg or "bus" in msg:
        return "College buses run on 12 routes across the city. Bus fee is Rs. 15,000/year."
    elif "sport" in msg:
        return "We have cricket, football, basketball, volleyball courts and an indoor gym."
    elif "contact" in msg or "phone" in msg or "email" in msg:
        return "Phone: +91 98765 43210 | Email: info@college.edu.in"
    elif "location" in msg or "address" in msg or "where" in msg:
        return "The college is located at University Road, Ahmedabad, Gujarat."
    elif "thank" in msg:
        return "You're welcome! Happy to help."
    elif msg in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day."
    else:
        return ("Sorry, I didn't understand that. You can ask about admission, courses, fees, "
                "hostel, library, exams, results, placement, transport, sports or contact.")


def main():
    print("=" * 55)
    print("        COLLEGE HELP DESK CHATBOT")
    print("  Type 'bye' to exit.")
    print("=" * 55)
    while True:
        user_input = input("You: ")
        print("Bot:", get_response(user_input))
        if user_input.lower().strip() in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
