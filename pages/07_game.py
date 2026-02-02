import streamlit as st
import random

st.set_page_config(page_title="Mini Game", page_icon="🎮")

st.title("🎮 The Randomizer Arena")

# 1. INITIALIZE GAME STATE (The Memory)
# We only want to pick a number ONCE, not every time you click.
if 'target_number' not in st.session_state:
    st.session_state['target_number'] = random.randint(1, 100)
    st.session_state['attempts'] = 0
    st.session_state['game_over'] = False
    st.session_state['message'] = "I've picked a number between 1 and 100."

# 2. THE GAMEPLAY LOOP (Triggered by Buttons)
def check_guess():
    # Grab the user's input from the session state widget
    guess = st.session_state.my_guess
    st.session_state['attempts'] += 1

    if guess < st.session_state['target_number']:
        st.session_state['message'] = f"📉 Too Low! (Guess: {guess})"
    elif guess > st.session_state['target_number']:
        st.session_state['message'] = f"📈 Too High! (Guess: {guess})"
    else:
        st.session_state['message'] = f"🎉 CORRECT! The number was {guess}."
        st.session_state['game_over'] = True

# 3. RENDER THE UI
st.info(st.session_state['message'])

if not st.session_state['game_over']:
    # The Input
    st.number_input("Enter your guess:", min_value=1, max_value=100, key="my_guess")
    
    # The Trigger
    st.button("Submit Guess", on_click=check_guess)
else:
    st.success(f"You won in {st.session_state['attempts']} attempts!")
    if st.button("Play Again"):
        # Hard Reset
        del st.session_state['target_number']
        st.rerun()