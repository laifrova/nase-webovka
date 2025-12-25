from django.shortcuts import render
import random
def home(request):
   return render(request, 'home.html')


def game(request):
    result = None
    computer_choice = None
    player_choice = None
    image_path = None
    reaction_image= None

    if request.method == "POST":
        player_choice = request.POST.get('choice')
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        # Cesta k tvé fotce
        image_path = f"images/{computer_choice}.jpeg"

        # Logika vyhodnocení
        if player_choice == computer_choice:
            result = "It's a draw! 😐"
            reaction_image = ""
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win! 🎉"
            reaction_image = "sad_me.jpeg"
        else:
            result = "I win"
            reaction_image = "happy_me.jpeg"

    context = {
        'result': result,
        'computer_choice': computer_choice,
        'image_path': image_path,
        'player_choice': player_choice,
        'reaction_image': reaction_image
    }
    return render(request, 'game.html', context)
def final_page(request):
    return render(request, 'final_page.html')