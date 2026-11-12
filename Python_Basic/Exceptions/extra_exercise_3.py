def values_list():
    list_values =['10', 'apple', '5.5', 'n/a', '20', 'Alvaro']
    return list_values

def sum_list_values(data_list):
    add_counter = 0
    print()
    print("***** Function Results *****")
    print("----------------------------")
    print()
    for data_value in data_list:
        try:
            convert_list_element = float(data_value)
            print(f"{convert_list_element}. Added successfully.")
            add_counter += convert_list_element
        except ValueError:
            print(f"Invalid element: {data_value!r}")    
    print()
    print(f"The total sum is: {add_counter} ")
    print()

def main():
    sum_list_values(values_list())

if __name__ == "__main__":
    main()