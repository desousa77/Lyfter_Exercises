def strings_list():
    str_list = ['4', '20', 'hola', '10', '5.2','50','Alvaro']
    return str_list

def convert_to_int(list_of_str):
    
    list_to_int = []
    print("***** Results *****")
    print("--------------------------------------")
    
    for str_to_convert  in list_of_str:
        try:
            new_int = int(str_to_convert)
            list_to_int.append(new_int)        
            print(f" {str_to_convert!r}, converted to: {new_int}.")
        except ValueError:
            print(f"Could not convert the element: {str_to_convert!r}")
    print()
    print(f"New Integer list: {list_to_int}") 
    print()       

def main():    
    convert_to_int(strings_list())
    

if __name__ == "__main__":
    main()  