from code import interact


from carbs import nutritions
# This welcoming message contains the app description for the user
def Welcome_msg():
    interact= ''' ___
                          _/`.-'`.
                _      _/` .  _.'
       ..:::::.(_)   /` _.'_./
     .oooooooooo\ \o/.-'__.'o.
    .ooooooooo`._\_|_.'`oooooob.
  .ooooooooooooooooooooo&&oooooob.
 .oooooooooooooooooooo&@@@@@@oooob.
.ooooooooooooooooooooooo&&@@@@@ooob.
doooooooooooooooooooooooooo&@@@@ooob
doooooooooooooooooooooooooo&@@@oooob
dooooooooooooooooooooooooo&@@@ooooob
dooooooooooooooooooooooooo&@@oooooob
`dooooooooooooooooooooooooo&@ooooob'
 `doooooooooooooooooooooooooooooob'
  `doooooooooooooooooooooooooooob'
   `doooooooooooooooooooooooooob'
    `doooooooooooooooooooooooob'
     `doooooooooooooooooooooob'
       `dooooooooobodoooooooob'
       `doooooooob dooooooob'
         `"""""""' `""""""'
                                    
        ======================================
        ==   Welcome to the carbs viewer    ==
        ==  this app helps you to find many ==
        ==  delicious plates with nutrition ==
        ==  facts depending on your range   ==
        ==       of minimum and maximum     ==
        ==         carbs consumption        ==
        ======================================
          


     '''

    print(interact)
def looping(res):
      # Here we are looping through every single attribute of the object returned by the API depending on the users choice 
    while res != "quit":
        
        option= input("press 1 to show the calories of each plate  \n press 2 to show the protein of each plate  \n press 3 to show the fat of each plate  \n press 4 to show the carbs of each plate \n \"quit\" to exit \n > ")
        
        if option == '1':
             for i in nutritions.get_calories():
                print(i['title'] ,"--> "+ str(i['calories'])+"cal")
                print("========================================")
        elif option == '2':
            for i in nutritions.get_protein():
                print(i['title'] ,"--> "+ str(i['protein']+" of protein"))
                print("========================================")
        elif option == '3':
            for i in nutritions.get_fat():
                print(i['title'] ,"--> "+ str(i['fat']+" of fat"))
                print("========================================")
        elif option == '4':
            for i in nutritions.get_carbs():
                print(i['title'] ,"--> "+ str(i['carbs'])+" of carbs")
                print("========================================")
        elif option== "quit" or option == "q":
            print("Good bye")
            break
        if option >= "5" :
            raise ValueError("oops invalid number The input should be as suggested ")   


def user_input():
   # user input for the min and max carbs, if the user inputs something else than values that are not in the (0-119) range we raise a warning message
    print("please enter the Minimum and the Maximum carbs\n ** NOTE = > The Minimum value should be between (0-118)\n ** NOTE = > The Maximum value should be between (1-119)")
    print(" ** NOTE = >  Maximum value > Minimum value  ")
    try : 
         min = int(input("> Minimum carbs : "))
         max = int(input("> maximum carbs : "))
    except :        
        raise ValueError("you should enter an intger number")
    if int(min)> int(max) :
        raise ValueError("it can not be Minimum value > Maximum value")
    while (int(min) in range(0,119)and int(max) in range(1,120))== False :
        print("invalid number ")
        min = input("please enter the Minimum > between (0-118) ")
        max = input("please enter the Maximum > between (1-119)  > ")
        if int(min)> int(max) :
            raise ValueError("it can not be Minimum value > Maximum value ")

    
    nutritions.set_carb(min,max)
    nutritions.get_data()
    res = input("> if you want to continue type any things or \"quit\" to exit ")
    print("=============================================")
    looping(res)
if __name__ == "__main__":
    Welcome_msg()
    user_input()

