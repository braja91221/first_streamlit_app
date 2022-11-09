import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#for error message handling

streamlit.title('My Parents New Health Diner')
streamlit.header('Breakfast Menu')
streamlit.text('\U0001F348 omega 3 & Blueberry oatmeal')
streamlit.text('\U0001F340 Kale, Spinach & Rocket Smoothie')
streamlit.text('\U0001F347 Hard-Boiled Free-Range Egg')
streamlit.text('\U0001F951 Avacodo Toast')
streamlit.header('\U0001F34C Build Your Own Fruit Smoothie')

#pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatable code block called function
def get_fruitvice_data(this_first_choice):
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice )
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       return fruitvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
#import requests
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("please select a fruit to get information.")
        #streamlit.write('The user entered ', fruit_choice)
        #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    else:
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice )
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       back_from_function= get_fruitvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
    
       #streamlit.dataframe(fruitvice_normalized)
       #streamlit.text(fruityvice_response.json())
      
except URLError as e:
  streamlit.error()

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)


#import snowflake.connector
streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
    #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    #my_cur = my_cnx.cursor()
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
 #my_data_rows = my_cur.fetchall()
#my_data_row = my_cur.fetchone()
#streamlit.text("The fruit load list contains:")

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
#streamlit.dataframe(my_data_row)
#streamlit.text(my_data_row)
streamlit.stop()
#Allow the end user to add a fruit to yhe list
def insert_row_snowflake(new_fruit):
       with my_cnx.cursor() as my_cur:
              my_cur.execute("insert into fruit_load_list values('from streamlit')")
              return "Thanks for adding" + new_fruit
     
add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function=insert_roe_snowflake(add_my_fruit)
     streamlit.text(back_from_function)
                                    
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values('from streamlit')")
