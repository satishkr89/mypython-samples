def what_is_weekday(wk_day_num):
    wk_days = {1: "Sunday", 2: "Monday", 3 : "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    print(f"You entered weekday: {wk_day_num} ! The week day names are: {wk_days}")
    if 1 <= wk_day_num <=7:
        return wk_days[wk_day_num]
    else: 
        er_msg = "On Planet earth there are only 7 weekdays numbered between 1 and 7"
        print(er_msg)
        return er_msg

if __name__ == "__main__":

    try:
        print("This is Earth's weekday teller.")
        while(True):
            wk_day = input("enter week day number between 1 & 7 or q for quitting weekday teller: ")
            if wk_day == "q":
                print("quitting weekday teller")
                break
            else:
                i_wk_day = int(wk_day)
                print(f"You entered weekday: {i_wk_day}! The week day name is: {what_is_weekday(i_wk_day)}")
    except Exception as exp:
        print("Exception....->", type(exp), exp )
        
        