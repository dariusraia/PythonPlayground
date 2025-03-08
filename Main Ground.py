from datetime import datetime

def didi_bot():   
    print("DIDI Bot: Hello there! My name is Didi bot and I am your personal virtual assistant. It's a pleasure to meet you. First, I would like to know your name, please!")
    while True:
        user_input = input("Please enter something: ")
        if user_input == "Bye":
            print("DIDI Bot: Goodbye!")
            return
        if all(x in user_input.lower() for x in ["how", "are", "you"]):
                print("Zer Gut! You?")
                continue  
        if any(x in user_input.lower() for x in ["time", "hour", "clock"]):
                print(f"The hour is {datetime.now().strftime('%H:%M')}")
                continue  
                      
didi_bot()          
