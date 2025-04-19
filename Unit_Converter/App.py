import streamlit as st

def unit(value: float, unit_from: str, unit_to: str):

    if unit_from ==  "kilometer" and unit_to == "meter":
        return value * 1000
    
    elif unit_from == "meter" and unit_to == "kilometer":
        return value * 0.001
    
    elif unit_from == "kilogram" and unit_to == "gram":
        return value * 1000
    
    elif unit_from == "gram" and unit_to == "kilogram":
        return value * 0.001
    else:
        return "conversion is not correct"
    
# result1 = unit(1, "kilometer", "meter")    
# print("The value of meter is", result1)
# result2 = unit(5, "meter", "kilometer")    
# print("The value of kilometer is", result2)

def main():

    st.title("Unit Converter")
    st.write("Welcome to unit converter:")
    value = st.number_input ("Enter the value you want to convert:", min_value=0.0)
    unit_from = st.text_input("Enter the value you want to convert from (e.g: meter, kilometer, gram, kilogram)")
    unit_to = st.text_input("Enter the value you want from conversion from (e.g: meter, kilometer, gram, kilogram)")
    
    if st.button("Convert"):
        result = unit (value, unit_from, unit_to)
        st.write("Converted value", result)


    # print("Unit converter")
    # print("Welcome to unit converter")
    # value = float (input("Enter the value you want to convert:"))
    # unit_from = input("Enter the value you want to convert from (e.g: meter, kilometer, gram, kilogram)")
    # unit_to = input("Enter the value you want from conversion from (e.g: meter, kilometer, gram, kilogram)")
    # result = unit (value, unit_from, unit_to)
    
    # print("value",value)
    # print("unit_from",unit_from)
    # print("unit_to",unit_to)
    # print("Converted Value", result)
main()
