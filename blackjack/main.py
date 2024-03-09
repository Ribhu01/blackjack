import random
from ASCI import logo
print(logo)
def blackjack():
    is_blackjack = False
    if user_score == 21:
        print("You win, you got blackjack!")
        is_blackjack = True
    elif computer_score == 21:
        print("You lose!")
        print(f"Computer's final hand card: {computers_cards}, and computer's score is {sum(computers_cards)}")
        is_blackjack = True
    return is_blackjack



def deal_card():
    """ RETURNS A RANDOM CARD FROM THE DECK"""
    card = random.choices(cards)
    return card


def check_ace():
    if 11 in users_cards:
        users_cards.remove(11)
        users_cards.append(1)
        if user_score > 21:
            print(f"computer's final hand card: {computers_cards},and computers score is {sum(computers_cards)}")
            print("You lose!")

        else:
            ask_to_draw_cards()
    else:
        print(f"computer's final hand card: {computers_cards},and computers score is {sum(computers_cards)}")
        print("You lose!")


def ask_to_draw_cards():
    to_draw = input("Type 'y' to draw another card or 'n' to pass: ")
    return to_draw


def computer_draw(c_score):
    computers_cards.extend(deal_card())
    c_score = sum(computers_cards)
    if c_score > 21 and user_score > sum(computers_cards):
        print(f"Your final hand: {users_cards}, your current score {user_score}")
        print(f"computer's final hand card: {computers_cards},computer's score is {sum(computers_cards)}")
        print("YOU WIN!")
    else:
        compare_score(user_score, computer_score)


def compare_score(u_score, c_score):
    if c_score > 21:
        print(f"computer's final hand card: {computers_cards},and computers score is {sum(computers_cards)}")
        print("You win!")

    elif u_score < c_score:
        print(f"computer's final hand card: {computers_cards},and computers score is {sum(computers_cards)}")
        print("You win!")

    elif u_score == c_score:
        print("Draw!")


if_again = True
while if_again:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    users_cards = []
    computers_cards = []
    is_game_over = False

    for i in range(2):
        users_cards.extend(deal_card())
        computers_cards.extend(deal_card())
    should_continue = True
    ask_answer = ""
    while should_continue:
        user_score = sum(users_cards)
        computer_score = sum(computers_cards)
        print(f"Your cards: {users_cards}, your current score {user_score}")
        print(f"computer's first card: {computers_cards[0]}")

        blackjack_output = blackjack()
        if blackjack_output:  # Check if blackjack is True
            should_continue = False  # Exit the loop
            break
        if blackjack_output == "False":
            if user_score > 21:
                check_ace()

        if user_score < 21:
            ask_answer = ask_to_draw_cards()
            if ask_answer == "y":
                users_cards.extend(deal_card())
                user_score = sum(users_cards)
            elif ask_answer == "n":
                should_continue = False
                computer_draw(computer_score)
                computer_score = sum(computers_cards)
        elif user_score > 21:
            print("you lose!")
            is_game_over = True
            print(f"computer's final hand card: {computers_cards},and computers score is {sum(computers_cards)}")
            should_continue = False

    again = input("Do you wanna play again? type 'y' to play again and 'n' to exit.")
    if again == "n":
        if_again = False
