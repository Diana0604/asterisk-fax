import version
question = ""
while question != "exit":
    question = version.get_input("What do you want to test? Options are: 'lights', 'sound', 'calls', 'smoke', 'buttons' or 'exit' to finish tests. ")
    if(question == 'lights'):
        import tester_lights
        continue

    if(question == 'sound'):
        import tester_sounds
        continue
    
    if(question == 'calls'):
        import tester_calls
        continue

    if(question == "smoke"):
        import tester_smoke;
        continue

    if(question == 'buttons'):
        import tester_buttons
        continue
    
    if(question != 'exit'):
        print("did not understand what you are trying to test. Please check your spelling and try again.")
