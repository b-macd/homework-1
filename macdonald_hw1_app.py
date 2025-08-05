#! ./macdonald_hw1.py
import datetime as dt
import random
import streamlit as st

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'user_age' not in st.session_state:
    st.session_state.user_age = None
if 'user_fname' not in st.session_state:
    st.session_state.user_fname = None
if 'user_lname' not in st.session_state:
    st.session_state.user_lname = None
if 'kids_prompt' not in st.session_state:
    st.session_state.kids_prompt = None


extreme_sports = [
    "Skydiving",
    "Bungee Jumping",
    "Rock Climbing",
    "Whitewater Rafting",
    "Surfing",
    "Snowboarding",
    "Mountain Biking",
    "Scuba Diving",
    "BASE Jumping",
    "Paragliding"
    "Pickleball"
]

def generate_extreme_sport():
  """Generates a random extreme sport option."""
  return random.sample(extreme_sports, k=3)

col1, col2, col3 = st.columns([1,7,1])

with col2:

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; padding: 10px;">
        <h1 style = "text-align: center; margin: 0;">MacDonald Python Homework 1</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

if st.session_state.form_submitted == False:
        
    user_input_form = st.form("Please fill out the following information")

    with user_input_form:
        st.session_state.user_age = st.number_input("Current Age")
        st.session_state.user_fname = st.text_input('First Name')
        st.session_state.user_lname = st.text_input('Last Name')
        st.session_state.kids_prompt = st.selectbox('Do you have kids?', options=['Yes', 'No'])
        submit_button = st.form_submit_button('Submit')
    
    if submit_button:
        st.session_state.form_submitted = True
        st.rerun()


if st.session_state.form_submitted == True:
    current_year = dt.date.today().year
    birth_year = current_year-st.session_state.user_age
    first_username_option = f'{st.session_state.user_fname}'+'.'+f'{st.session_state.user_lname}'
    second_username_option = f'{st.session_state.user_fname[0]}'+'.'+f'{st.session_state.user_lname}'
    third_username_option = f'{st.session_state.user_fname}'+'.'+f'{st.session_state.user_lname}'+f'{random.randint(1,10)}'
    life_used_up = st.session_state.user_age / 73.4
    life_left = 1-life_used_up

    st.info(f'''#### You were born in {int(birth_year)}
- You most likely graduated highschool in {int(birth_year+18)} or {int(birth_year+19)}''')
    st.info(f'''#### Here are some possible usernames and each associated email address:
            
    1. {first_username_option} - {first_username_option.lower()+'@gmail.com'}
    2. {second_username_option} - {second_username_option.lower()+'@gmail.com'}
    3. {third_username_option} - {third_username_option.lower()+'@gmail.com'}''')

    if life_used_up <= .49:
        st.success(f'''#### Based on the average life expectancy of 73.4, you still have {life_left:.2%} of your life left.
- You've got more than half your life left, don't waste it!''')
    elif life_used_up >= .50 and life_used_up <= .75:
        st.warning(f"""#### Based on the average life expectancy of 73.4, you have used up {life_used_up:.2%} of your life.\n
- It's all downhill from here!
- Maybe look into a Corvette...""")
    else:
        

        if st.session_state.kids_prompt.lower() == 'yes':
            st.error(f'''### Based on the average life expectancy of 73.4, you have {life_left:.2%} of your life left.
- Maybe give your kids a hug today.. You know, in case you don't make it to tomorrow''')

        else:
            extreme_sports_choices = generate_extreme_sport()
            st.error(f'''### Based on the average life expectancy of 73.4, you have {life_left:.2%} of your life left.
            
#### Go have fun! Here are some extreme sports that you should try while you still have time:   
 
- {extreme_sports_choices[0]}
- {extreme_sports_choices[1]}
- {extreme_sports_choices[2]}''')


