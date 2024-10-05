import csv
import re
import hashlib
import requests
from datetime import datetime

REGNO_FILE_PATH = 'regno.csv'
USER_ACTIVITY_LOG_PATH = 'user_activity_log.csv'

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    if len(password) < 8:
        return False
    special_characters = re.compile('[@$!%*?&]')
    return bool(special_characters.search(password))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(email, password, security_question, correct_answer):
    hashed_password = hash_password(password)
    with open(REGNO_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, hashed_password, security_question, correct_answer])
    print("Signup successful! Please log in.")
    main()

def login(email=None):
    login_attempts = 0
    if not email:
        email = input("Enter your email: ")

    while login_attempts < 3:
        password = input("Enter your password: ")
        hashed_password = hash_password(password)
        try:
            with open(REGNO_FILE_PATH, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == email and row[1] == hashed_password:
                        print("Login successful!")
                        search_news(email)
                        return
            print("Invalid email or password.")
        except FileNotFoundError:
            print("User database not found.")
            return
        login_attempts += 1
        print(f"Attempt {login_attempts} of 3.")

    if login_attempts >= 3:
        reset_choice = input("Too many failed attempts. Would you like to reset your password? (yes/no): ")
        if reset_choice.lower() == 'yes':
            reset_password(email)

def reset_password(email):
    if not validate_email(email):
        print("Invalid email format.")
        return

    try:
        with open(REGNO_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email:
                    security_question = row[2]
                    correct_answer = row[3]
                    answer = input(f"Security Question: {security_question}\nYour Answer: ")
                    if answer == correct_answer:
                        new_password = input("Enter your new password: ")
                        if validate_password(new_password):
                            hashed_password = hash_password(new_password)
                            update_password(email, hashed_password)
                            print("Password reset successful! You can now log in.")
                            return
                        else:
                            print("New password does not meet criteria.")
                            return
            print("Email not found in the database.")
    except FileNotFoundError:
        print("User database not found.")

def update_password(email, new_password):
    rows = []
    with open(REGNO_FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                row[1] = new_password
            rows.append(row)

    with open(REGNO_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Password updated successfully. Please log in.")

def search_news(email):
    keyword = input("Enter a keyword for news: ")
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=e4853dd9d7214272af5f2038635d0b67"
    response = requests.get(url)
    data = response.json()

    if 'articles' in data:
        for i, article in enumerate(data['articles'][:5], start=1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Link: {article['url']}\n")
            log_activity(email, keyword, article)

        while True:
            article_num = input("Enter article number to visit (or 'exit' to quit): ")
            if article_num.lower() == 'exit':
                break

            if article_num.isdigit() and 1 <= int(article_num) <= 5:
                selected_article = data['articles'][int(article_num) - 1]
                print(f"Visited: {selected_article['url']}\n")
            else:
                print("Invalid article number. Please try again.")
    else:
        print("No articles found for this keyword.")

def log_activity(email, keyword, article):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with open(USER_ACTIVITY_LOG_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, time_str, email, keyword, article['title'],
                         article['source']['name'], article['url']])

def main():
    print("-----------------------------Welcome to News at Galance------------------------")
    print("News at just few clicks--Browse Your headlines according to your Keywords!!")
    while True:
        print("\nWe Welcome you:::---")
        print("1. Login")
        print("2. Sign Up")
        print("3. Reset Password")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            email = input("Enter your email: ")
            if validate_email(email):
                login(email)
            else:
                print("Invalid email format. Please enter again.")

        elif choice == '2':
            email = input("Enter your email: ")
            if validate_email(email):
                password = input("Enter your password: ")
                security_question = input("Enter a security question: ")
                correct_answer = input("Enter the answer to the security question: ")
                if validate_password(password):
                    signup(email, password, security_question, correct_answer)
                else:
                    print("Invalid password format.")
            else:
                print("Invalid email format.")

        elif choice == '3':
            email = input("Enter your email: ")
            reset_password(email)

        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# Since, i have made this project in pythom due to multiple library issues that i was facing in jupyter and vscode
# In collab both my csv files are created in collab virtual environment. 
# In order to download and check them in your local use this snippet: 

# from google.colab import files
# files.download('regno.csv')
# files.download('user_activity_log.csv')
