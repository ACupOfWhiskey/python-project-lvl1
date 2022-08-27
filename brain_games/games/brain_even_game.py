#!/usr/bin/env python3
from brain_games.game_engine.common_logic import greetings_user
from brain_games.game_engine.common_logic import asking_user_name
from brain_games.game_engine.common_logic import brain_even_task
from brain_games.game_engine.common_logic import brain_even_logic


def brain_even_game():
    greetings_user()
    asking_user_name()
    brain_even_task()
    brain_even_logic()