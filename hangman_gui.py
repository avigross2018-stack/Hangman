def show_gui(rounds_counter : int, max_rounds : int):
    rounds = max_rounds - rounds_counter
    match rounds:
        case 5:
            print("    (  )    ")
            print("     ||     ")
            print(" ====  ==== ")
            print("     ||     ")
            print("     ||     ")
            print("     /\     ")
            print("    /  \    ")
            print("   /    \   ")
        case 4:
            print("    (  )    ")
            print("     ||     ")
            print(" ====  ==== ")
            print("     ||     ")
            print("     ||     ")
            print("     /     ")
            print("    /      ")
            print("   /       ")
        case 3:
            print("    (  )    ")
            print("     ||     ")
            print(" ====  ==== ")
            print("     ||     ")
            print("     ||     ")
            print("          ")
            print("          ")
            print("         ")