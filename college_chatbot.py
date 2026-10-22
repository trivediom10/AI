"""
Rule-Based College Chatbot
Topic  : College Enquiry
Author : Om Trivedi
Method : if-elif-else conditions on user input
"""

COLLEGE = "GMIU College"


def get_response(user_input):
    msg = user_input.lower().strip()

    if msg == "":
        return "Please type something so I can help you."
    elif any(w in msg for w in ["hello", "hi", "hey", "good morning", "good evening"]):
        return f"Hello! Welcome to {COLLEGE}. How can I help you today?"
    elif "course" in msg or "program" in msg or "branch" in msg:
        return ("We offer B.Tech (CSE, IT, Mechanical, Civil, Electrical), BCA, BBA, "
                "B.Com, MCA, MBA and M.Tech programs.")
    elif "admission" in msg or "apply" in msg:
        return ("Admissions open in May every year. You can apply online on the college "
                "website or visit the admission office with your 12th marksheet.")
    elif "eligib" in msg:
        return ("For B.Tech you need 12th Science (PCM) with at least 45%. "
                "For BCA/BBA/B.Com, 12th pass in any stream is required.")
    elif "fee" in msg or "fees" in msg:
        return ("Approximate yearly fees: B.Tech - Rs. 85,000, BCA - Rs. 45,000, "
                "BBA - Rs. 40,000, MBA - Rs. 90,000. Scholarships are available.")
    elif "scholarship" in msg:
        return ("Scholarships are given on merit (above 85%) and through government "
                "schemes like MYSY and Post-Matric. Contact the scholarship cell.")
    elif "hostel" in msg:
        return ("Separate hostels for boys and girls are available with Wi-Fi, mess "
                "and 24x7 security. Hostel fee is about Rs. 60,000 per year.")
    elif "library" in msg:
        return ("The central library is open from 8:00 AM to 8:00 PM (Mon-Sat) and has "
                "over 50,000 books, journals and e-resources.")
    elif "timing" in msg or "time" in msg or "hours" in msg:
        return "College timings are 9:00 AM to 4:30 PM, Monday to Saturday."
    elif "placement" in msg or "job" in msg or "recruit" in msg:
        return ("Our placement cell invites companies like TCS, Infosys, Wipro and L&T. "
                "Last year 85% of eligible students were placed.")
    elif "exam" in msg or "result" in msg:
        return ("Semester exams are held in November and May. Results are published "
                "on the university portal within 45 days.")
    elif "canteen" in msg or "food" in msg:
        return "The college canteen serves hygienic veg food from 8:30 AM to 5:00 PM."
    elif "sport" in msg or "gym" in msg:
        return ("We have a cricket ground, basketball and volleyball courts, indoor "
                "games and a gym for students.")
    elif "transport" in msg or "bus" in msg:
        return "College buses run on all major city routes. Bus fee is Rs. 15,000 per year."
    elif "contact" in msg or "phone" in msg or "email" in msg:
        return "Phone: +91 98765 43210 | Email: info@gmiu.edu.in"
    elif "address" in msg or "location" in msg or "where" in msg:
        return f"{COLLEGE} is located on the main campus road, Bhavnagar, Gujarat."
    elif "thank" in msg:
        return "You're welcome! Feel free to ask anything else."
    elif "help" in msg:
        return ("You can ask me about: courses, admission, eligibility, fees, "
                "scholarship, hostel, library, timings, placement, exams, canteen, "
                "sports, transport, contact and address.")
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can answer."


def main():
    print("=" * 55)
    print(f"   {COLLEGE} Enquiry Chatbot")
    print("   Type 'help' for topics, 'bye' to exit.")
    print("=" * 55)
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day.")
            break
        print("Bot:", get_response(user_input))


if __name__ == "__main__":
    main()
