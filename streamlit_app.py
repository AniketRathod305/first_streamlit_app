import streamlit
   
streamlit.title('My Parents New Healthy Diner')
streamlit.header('π₯£Breakfast Favorites')
streamlit.text('π₯ Omega 3 & Blueberry Oatmeal')
streamlit.text('π Kale,Spinach & Rocket Smoothie')
streamlit.text('π₯π Hard-Boiled Free-Range Egg')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')


import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
