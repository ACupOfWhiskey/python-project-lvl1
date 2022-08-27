#!/usr/bin/env python3
from brain_games.game_engine.common_logic import greetings_user
from brain_games.game_engine.common_logic import asking_user_name
from brain_games.game_engine.common_logic import brain_calc_task
from brain_games.game_engine.common_logic import brain_calc_logic


def brain_calc_game():
    greetings_user()
    asking_user_name()
    brain_calc_task()
    brain_calc_logic()
