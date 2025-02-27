day = "Friday" 
match day: 
    case "Monday": 
        print("Start of the week!") 
    case "Friday": 
        print("Weekend is near!") 
    case "Sunday": 
        print("It's a holiday!") 
    case _: 
        print("Regular day")
