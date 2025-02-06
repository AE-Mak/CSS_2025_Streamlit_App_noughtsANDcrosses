# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 2025

@author: AEM
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import random

# # Defining and initialising the global variables
# #fact_idx = 1 # index for choosing the game's fact
# fact_idx = random.randint(1, 49)

# Session state initialization
if 'page' not in st.session_state:
    st.session_state.update({
        'page': 'welcome',
        'games_played': 0,
        'results': [],
        'player_name': '',
        'board': [''] * 9,
        'current_player': 'Human',
    })
    
# Check if the random fact index already exists in the session state
if 'fact_idx' not in st.session_state:
    # If not, choose a random number between 0 and 48 (for 49 fun facts)
    st.session_state.fact_idx = random.randint(0, 48)


WIN_COMBOS = [
    [0,1,2], [3,4,5], [6,7,8],  # Rows
    [0,3,6], [1,4,7], [2,5,8],  # Columns
    [0,4,8], [2,4,6]            # Diagonals
]

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #b2f2e2, #cce5ff);
}
.centered {
    text-align: center;
    margin: auto;
}
.pulse-text {
    animation: pulse 1.5s infinite;
    font-size: 2.5em !important;
}
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.1);}
    100% {transform: scale(1);}
}
.champion-banner {
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)


def check_winner(board):
    # Check for a winner first
    for combo in WIN_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]  # 'X' or 'O'
    
    # Check for a draw (no empty cells left, and no winner found)
    if '' not in board:
        return #'Draw'
    
    return None  # Game continues


def computer_move():
    empty_cells = [i for i, cell in enumerate(st.session_state.board) if cell == '']
    
    if empty_cells:  # Check if there are available moves
        return random.choice(empty_cells)
    else:
        return None  # No available moves

def reset_game(): 
    #global fact_idx
    #fact_idx = random.randint(1, 49)
    st.session_state.board = [''] * 9
    st.session_state.current_player = 'Human' if st.session_state.games_played % 2 == 0 else 'Computer'

def welcome_page():
    col1, col2, col3 = st.columns([1,3,1])
    left, middle1, middle2, middle3, right = st.columns(5)
    with col2:
        tic_tac_toe_gif = 'Tic_tac_toe_GIPHY.gif'
        # tic_tac_toe_gif_link  = https://upload.wikimedia.org/wikipedia/commons/7/7d/Tic-tac-toe-animated.gif
        st.image(tic_tac_toe_gif, use_container_width=True)
        st.markdown("<h1 class='centered'>🎮 Noughts & Crosses Arena </h1>", unsafe_allow_html=True)
        if middle2.button("START GAME 🕹️", key="start", help="Click to begin!"):
            st.session_state.page = 'name_input'
            st.rerun()
            
def name_input_page():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown("<h2 class='centered'>🪪 Player Identification</h2>", unsafe_allow_html=True)
        st.session_state.player_name = st.text_input("Enter your name:")
        if st.session_state.player_name:
            reset_game()
            st.session_state.page = 'game'
            st.rerun()

def game_page():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown(f"<h2 class='centered'>🏁 {st.session_state.player_name}'s Challenge</h2>", unsafe_allow_html=True)
        st.subheader(f"Round :blue[{st.session_state.games_played + 1}] of 7")
        fun_facts = [
                " The first computer bug was a real moth! 🦋",
                " COBOL was designed by a Navy officer! ⚓",
                " The first programmer was Ada Lovelace! 👩‍💻",
                " Java was originally called Oak! 🌳",
                " Git was created by Linus Torvalds! 🐧",
                " There are 700+ programming languages! 🗣️",
                " Emoji domains exist! 😃.ws",
                " Stack Overflow launched in 2008! 💡",
                " Hello World dates back to 1974! 👋",
                " JavaScript was created in 10 days! ⏳",
                " HTML isn’t a programming language! 📄",
                " Google's first storage was in Lego! 🧱",
                " Mark Zuckerberg made Facebook in PHP! 📘",
                " The first website is still online! 🌍",
                " Ctrl+C & Ctrl+V invented in 1973! ⌨️",
                " The first 1GB hard drive cost $40,000! 💾",
                " Computers use binary because of electricity! ⚡",
                " CSS debuted in 1996! 🎨",
                " The first computer was powered by vacuum tubes! 💡",
                " The first video game console was released in 1952! 🎮",
                " Hackers once controlled 100,000 printers! 🖨️",
                " GitHub has over 100 million repositories! 🗄️",
                " The first computer weighed 27 tons! ⚖️",
                " NASA still uses 1970s code in space! 🚀",
                " CAPTCHA helps train AI! 🤖",
                " Unicode has over 143,000 characters! 🔤",
                " Linux runs on Mars rovers! 🛸",
                " Python overtook Java in popularity in 2018! 📊",
                " ‘Debugging’ came from removing a bug! 🐞",
                " DNS translates domains to IP addresses! 🌐",
                " The first video game was in 1958! 🎮",
                " C was developed in 1972! 🏗️",
                " PHP originally stood for ‘Personal Home Page’! 🏠",
                " Most ATMs run on Windows XP! 🏦",
                " The first iPhone had 128MB RAM! 📱",
                " Google processes 8.5B searches daily! 🔍",
                " AI can generate code now! 🤯",
                " Minecraft is written in Java! 🟫",
                " The longest domain name has 63 characters! 🔡",
                " MacOS is based on Unix! 🍏",
                " JavaScript has ‘NaN’ for Not-a-Number! 🔢",
                " Perl was called the ‘Swiss Army knife’! 🔪",
                " The ‘null’ reference is a billion-dollar mistake! 💸",
                " The first computer virus was ‘Creeper’! 🦠",
                " Twitter started as ‘Twttr’! 🐦",
                " NASA’s Apollo code is on GitHub! 🚀",
                " COBOL still runs banks today! 🏦",
                " 404 error means page not found! ❌",
                " Some programmers prefer dark mode! 🌙"
            ]
        
        winner = check_winner(st.session_state.board)
        
        fact_idx = st.session_state.fact_idx
        
        fact_container = st.container()
        fact_container.markdown(
                f"<div style='background-color: lightblue; padding: 10px; height: 100px; width: 100%; "
                f"position: fixed; bottom: 0; left: 0; text-align: center; font-size: 20px; display: flex; "
                f"align-items: center; justify-content: center; overflow: hidden;'>"
                f"<strong>Did you know?</strong><span style='margin-left: 10px;'>{fun_facts[fact_idx]}</span></div>", 
                unsafe_allow_html=True
            )
        cols = st.columns(3)
        for i in range(9):
            with cols[i%3]:
                if st.button(st.session_state.board[i] or ' ', 
                           key=f"cell_{i}", disabled=st.session_state.board[i] != ''):
                    if st.session_state.current_player == 'Human':
                        st.session_state.board[i] = 'X'
                        st.session_state.current_player = 'Computer'
                        st.rerun()

        if st.session_state.current_player == 'Computer':
            move = computer_move()
            if move is not None:
                st.session_state.board[move] = 'O'  # Assume 'O' is the computer's move
            else:
                st.warning("No moves left! The game is a draw.")
                handle_game_end(winner)

            st.session_state.board[move] = 'O'
            st.session_state.current_player = 'Human'
            st.rerun()

        
        if winner or ('' not in st.session_state.board) or ():
            # fact_idx = random.randint(1, 49)
            handle_game_end(winner)

def handle_game_end(winner):
    st.session_state.games_played += 1
    result = 'Human' if winner == 'X' else 'Computer' if winner == 'O' else 'Draw'
    st.session_state.results.append(result)

    # After 7 rounds, calculate the overall winner
    if st.session_state.games_played == 7:
        calculate_overall_winner()

    if st.session_state.games_played < 7:
        reset_game()
        st.rerun()
    else:
        st.session_state.page = "winner's page"
        st.rerun()

def calculate_overall_winner():
    df = pd.DataFrame({
        'Game': range(1, 8),
        'Result': st.session_state.results
    })
    human_wins = df['Result'].eq('Human').sum()
    computer_wins = df['Result'].eq('Computer').sum()
    draws = df['Result'].eq('Draw').sum()

    # Determine the overall winner
    if (human_wins > computer_wins) and (draws < 4):
        st.session_state.overall_winner = st.session_state.player_name
    elif (human_wins == computer_wins) or (draws > 4):
        st.session_state.overall_winner = "Draw"
    elif (human_wins < computer_wins) and (draws < 4):
        st.session_state.overall_winner = 'Computer'

def player_s_winning_page():
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if 'overall_winner' not in st.session_state:
            st.container("No overall winner determined yet. It is a draw.")
            if st.button("🔄 Play Again", key="restart"):
                st.session_state.clear()
                st.rerun()
            
            return

        overall_winner = st.session_state.overall_winner
        
        if overall_winner == st.session_state.player_name:
            st.markdown(
                f"""
                <style>
                    .pulse-text {{
                        font-weight: bold;
                        text-align: center;
                        font-size: 24px;
                        animation: pulse 1.5s infinite;
                        display: inline-block;
                    }}
                    .confetti {{
                        display: inline-block;
                        vertical-align: middle;
                    }}
                    @keyframes pulse {{
                        0% {{
                            transform: scale(1);
                        }}
                        50% {{
                            transform: scale(1.1);
                        }}
                        100% {{
                            transform: scale(1);
                        }}
                    }}
                </style>
                <div class='pulse-text'> Excellent job {overall_winner}! You outsmarted the code! <span class="confetti">🎉🎉🎉</span></div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()
            next_page_stats = st.button("Let's Celebrate and Get the Statistics", help="Click twice to celebrate and see the stats!")
            if next_page_stats:
                st.session_state.page = 'stats'
                st.rerun()
        else:
            st.session_state.page = 'stats'
            st.rerun()

def stats_page():
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if 'overall_winner' not in st.session_state:
            st.error("No overall winner determined yet. It is a draw.")
            if st.button("🔄 Play Again", key="restart"):
                st.session_state.clear()
                st.rerun()
            return

        overall_winner = st.session_state.overall_winner
        
        st.markdown("<div class='champion-banner'>🏆 Winner: " + 
                   f"{overall_winner} 🏆</div>", unsafe_allow_html=True)

        # Create the pie chart for victory distribution
        df = pd.DataFrame({
            'Game': range(1, 8),
            'Result': st.session_state.results
        })

        result_counts = df['Result'].value_counts().reset_index()
        result_counts.columns = ['Result', 'Count']

        fig_pie = px.pie(result_counts, names='Result', values='Count', title='Overall Match Results')
        st.plotly_chart(fig_pie, use_container_width=True)

        # Create the plot for the player's winning streak
        fig = px.line(df, x='Game', y=df['Result'].eq('Human').cumsum(),
                      title="Your Winning Streak 📈", 
                      labels={'y': 'Cumulative Wins', 'Game': 'Game Number'})

        st.plotly_chart(fig, use_container_width=True)

        if st.button("🔄 Play Again", key="restart"):
            st.session_state.clear()
            st.rerun()
        

pages = {
    'welcome': welcome_page,
    'name_input': name_input_page,
    'game': game_page,
    "winner's page": player_s_winning_page,
    'stats': stats_page
}
pages[st.session_state.page]()
