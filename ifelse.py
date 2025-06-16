n=input("My name is KOUSALYA\n I am Very much intrested in Drawing portraits,its my hobby\n till now i have drawn many\n Are u curious to see my art work (YES/NO):")
if n=='YES':
    print("Visit my profile to see all my arts,After watching all those let me know how they are looking")
    n=input("They are looking great,awesome\nYou have done a excellent work (TRUE/FALSE):")
    if n=='TRUE':
        print("Thank you so much for your response\n i will feel great")
    else:
        print("They are not that much good ,please try again improve your skills\n any ways they are looking good\n try newly")
    n=input("Are you curious to make your picture as portrait\n Do you want me to draw yours (YES/No):")
    if n=='YES':
            print("Oh sure i will work on it definitely you are going to get your portrait")
    else:
        print("its ok\n next time i will definitely try to impress you with my art work")
        n=input("Do you want me to improve my skills\n i am thinking to improve my skills\n then you definitely select YES!!!! HAHAHAHAH!!!!\n will work hard for it (TRUE/FALSE)")
        if n=='TRUE':
            print("Sure definitly im gona work on it as u like")
        else:
            print("Thank you for spending time on watching portraits or Arts")
    n=input("Are you intrested to learn Drawing\n Do you want me to teach you (YES/NO)")
    if n=='YES':
        print("OK sure i will teach you drawing.....you are going to learn it")
    else:
        print("why are you not willing to learn or you not interested.......")
        n=input("Not interested,or you intrested any other paint works or sand arts or other art works")
        if n=='paint works':
            print("OH EXCELLENT....")
        else:
            print("supebbbbbb!!!!!!!!!!!")
    n=input("Did you draw cartoons in school days if yes enter YES otherwise enter type of Drawing:")
    if n=='YES':
        print("huhu!! Tom&Jerry,Bheem,Mr.Bean,Sinchan,Ninja Hattori.......I am Remembering my school days!!!!!!!!!")
        y=input("from which class are u learnig drawing:")
        if y=='1st':
            print("suprbbbbb...")
        else:
            print(y)
    else:
        print(n)
        """THIS IS FOR MOTIVATION.."""
        x=input("Did you participate in any competitions in school days coloring or sketching")
        if x=='coloring':
            print("LIFE IS A PAINTING WITH FULL OF COLOURS AND YOU ARE THE ARTIST")
        elif x=='art':
            print("LIFE IS THE ART OF DRAWING ,WITHOUT AN ERASER")
        else:
            print(x)
        
elif n=='no':
    print("Oh! No! please go through my art work just watch it i hope u will like it\n once go through it i will feel HAPPY!!!")
    n=input("Now say YES/NO:")
    if n=='YES':
        print("Visit My profile\nand Enjoy watching arts")
        print("EVERY ART WORK OF ART,THE ARTIST himself/herself is present/n ART IS NOT WHAT YOU SEE,BUT WHAT YOU MAKE OTHERS SEE.......")
        n=input("DO you like it if yes type wow:")
        if n=='wow':
            print("cool")
        else:
            print(n)
    else:
        print("OKKKKKKK.....THANK you for responding\n ART IS LIE THAT ENABLES US TO REALISE THE TRUTH......")
else:
    print("Oooopsss!!!!! please just enter only (YES/NO)")
        
