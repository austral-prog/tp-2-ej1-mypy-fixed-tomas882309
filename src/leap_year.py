# Replace the "ANSWER HERE" for your answer
def is_leap_year() -> bool:
    x: int= int(input("ingrese el numero:"))
    if x%4 == 0:
        if x%100 == 0:
            if x% 400 ==0:
                print(f"El año {x} es bisiesto")
                return True

            else:
                print(f"El año {x} no es bisiesto")
                return False
        else:
            print(f"El año {x} es bisiesto")
            return True
    else:
        print(f"El año {x} no es bisiesto")
        return False



