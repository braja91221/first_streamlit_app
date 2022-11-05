import streamlit
streamlit.title('My Parents New Health Diner')
streamlit.header('Breakfast Menu')
streamlit.text('\U0001F348 omega 3 & Blueberry oatmeal')
streamlit.text('\U0001F340 Kale, Spinach & Rocket Smoothie')
streamlit.text('\U0001F347 Hard-Boiled Free-Range Egg')
streamlit.text('\U0001F951 Avacodo Toast')
streamlit.header('\U0001F34C Build Your Own Fruit Smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

