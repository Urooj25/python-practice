day = 7
match(day):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:#yah  _:end krne kaliya used like else
        print("Looking forward to weekend")
#Another way
day = 7
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Working day")
    case 6 | 7:
        print("Sorry this is weekend")
#You can add if statements in the case evaluation as an extra condition-check:
day = 4
month = 4
match day:
     case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A first weekend in april")
     case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A first weekend of may")
     case _:
        print("No match")
#Code challenge
day = 3
match day:
 case 1: 
  print("Monday")
 case 2:
  print("Tuesday")
 case 3:
  print("Wednesday")
 case _:
  print("Other day")
         