# Ex 1

def chk_str():
    input_int: str = input("Please, put a integer :D\n") 
    
    try:
        inpt_convrt: int = int(input_int)
        print(f"Congratulations your input is a int: {input_int}")

    except:
        raise ex

ex: Exception = Exception('The input is not a int, please try again.')

if __name__ == "__main__":
    
    num: int = chk_str()
    