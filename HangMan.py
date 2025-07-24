#איש תלוי- נועם חי

HANGMAN_ASCII_ART = """
Welcome to the game Hangman

  _    _                                          
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| 
                      __/ |                      	
                     |___/
"""

MAX_TRIES = 6  # מקסימום ניסיונות ניחוש לפני הפסד

HANGMAN_PHOTOS = {
    0: """x-------x""",
    1: """x-------x
|       |""",
    2: """x-------x
|       |
|       0""",
    3: """x-------x
|       |
|       0
|       |""",
    4: """x-------x
|       |
|       0
|      /|\\ """,
    5: """x-------x
|       |
|       0
|      /|\\
|      / """,
    6: """x-------x
|       |
|       0
|      /|\\
|      / \\""",
    7: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

def choose_word(file_path, index):
    count = 0  # סופר את מספר המילים הייחודיות בקובץ
    with open(file_path, 'r') as f1:  # פותח את הקובץ לקריאה
        words = f1.read().split()  # קורא את המילים מהקובץ ומפריד אותן
        arr = []  # רשימה לאחסון מילים ייחודיות
        for word in words:  # עובר על כל מילה בקובץ
            if word not in arr:  # אם המילה אינה כבר ברשימה
                arr.append(word)  # מוסיף את המילה לרשימה הייחודית
                count += 1  # מגדיל את המונה של המילים הייחודיות
               
        while index > len(words):  # אם המיקום המבוקש גדול ממספר המילים
            index -= len(words)  # מעגל את המיקום למקום הנכון

    return (count, words[index - 1])  # מחזיר את מספר המילים הייחודיות ואת המילה במיקום המבוקש

def check_valid_input(letter_guessed, old_letters_guessed):
    # בודק אם הקלט חוקי (אות אחת בלבד ולא אות שניחשה בעבר)
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():  
        return False
    
    if letter_guessed.lower() in old_letters_guessed:  # בודק אם האות ניחשה בעבר
        return False
        
    return True  # הקלט חוקי

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # מנסה לעדכן את הרשימה של האותיות שניחשו
    if check_valid_input(letter_guessed, old_letters_guessed):  # אם הקלט חוקי
        old_letters_guessed.append(letter_guessed.lower())  # מוסיף את האות לרשימה
        return True
        
    print('X')  # מדפיס 'X' במקרה של קלט לא חוקי
    print(" -> ".join(sorted(old_letters_guessed)))  # מציג את האותיות שניחשו
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    # מציג את המילה הנסתרת עם קווים תחתונים במקום אותיות שלא ניחשו
    printedword = ""  # מחרוזת המייצגת את המילה הנסתרת
    for char in secret_word:  # עובר על כל תו במילה הסודית
        if char in old_letters_guessed:  # אם התו ניחש
            printedword += char + " "  # מוסיף את התו
        else: 
            printedword += "_ "  # אם לא, מוסיף קו תחתון
    return printedword.strip()  # מחזיר את המילה עם קווים תחתונים

def check_win(secret_word, old_letters_guessed):
    # בודק אם כל התווים במילה הסודית ניחשו
    for char in secret_word:  # עובר על כל תו במילה
        if char not in old_letters_guessed:  # אם תו לא ניחש
            return False  
    return True  # מחזיר True אם כל התווים ניחשו

def print_hangman(num_of_tries):

    if 0 <= num_of_tries <= 7:  # אם מספר הניסיונות בטווח
        print(HANGMAN_PHOTOS[num_of_tries])  
    else:
        print("Already Lost")  # הדפס הודעת הפסד

def print_welcome_screen():
    # מדפיס את המסך הפתיחה של המשחק
    print(HANGMAN_ASCII_ART, MAX_TRIES)  

def main():
    print(HANGMAN_ASCII_ART, MAX_TRIES)  

    file_path = input("Enter the path to the words file: ")  
    index = int(input("Choose a word index (1-based): "))  

    secret_word = choose_word(file_path, index)[1]  # בוחר מילה סודית
    old_letters_guessed = []  # רשימה לאחסון אותיות ניחוש
    num_of_tries = 0  # מונה עבור מספר ניסיונות

    print_hangman(num_of_tries)  # הצגת מצב האיש
    print(show_hidden_word(secret_word, old_letters_guessed))  # מציג את המילה הנסתרת

    while num_of_tries < MAX_TRIES:  # עד שמספר הניסיונות קטן מהמקסימום
        guess = input("Guess a letter: ")  # קלט עבור ניחוש אות
        
        if try_update_letter_guessed(guess, old_letters_guessed):  # אם הקלט תקין ולא נוחש עוד
            if guess.lower() not in secret_word.lower():  # בודק אם האות לא במילה
                num_of_tries += 1  # מגדיל את המונה במקרה של ניחוש לא נכון
                print(":(")  # מדפיס פרצוף עצוב במקרה של ניחוש לא נכון
                print_hangman(num_of_tries)  
                
            print(show_hidden_word(secret_word, old_letters_guessed))  # מציג את המילה הנסתרת
            if check_win(secret_word, old_letters_guessed):  # בודק אם ניצחו
                print("WIN! You've guessed the word:", secret_word)  # מציג ניצחון
                break
        else:  # במקרה של קלט לא חוקי
            print("X")  # מדפיס 'X'
            print(" -> ".join(sorted(old_letters_guessed)))  # מציג את האותיות שכבר ניחשו

    if num_of_tries == MAX_TRIES:  # אם הגיע למקסימום הניסיונות
        print("LOSE! The word was:", secret_word)  # מציג הפסד

if __name__ == '__main__':
    main()  # מפעיל את הפונקציה הראשית
