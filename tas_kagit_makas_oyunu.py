import random

def get_user_choice():
    choice = input("Taş, kağıt, makas? ").lower()
    while choice not in ['taş', 'kağıt', 'makas']:
        choice = input("Lütfen geçerli bir seçenek girin (taş, kağıt, makas): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['taş', 'kağıt', 'makas'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == 'taş' and computer_choice == 'makas') or \
         (user_choice == 'kağıt' and computer_choice == 'taş') or \
         (user_choice == 'makas' and computer_choice == 'kağıt'):
        return "Tebrikler, kazandınız!"
    else:
        return "Üzgünüm, bilgisayar kazandı!"

def main():
    print("Taş Kağıt Makas Oyununa Hoş Geldiniz!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Siz: {user_choice}\nBilgisayar: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
