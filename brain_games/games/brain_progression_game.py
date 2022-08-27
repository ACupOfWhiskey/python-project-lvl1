#!/usr/bin/env python3
from brain_games.game_engine.common_logic import greetings_user
from brain_games.game_engine.common_logic import asking_user_name
from brain_games.game_engine.common_logic import brain_progression_task
from brain_games.game_engine.common_logic import brain_progression_logic


def brain_progression_game():
    greetings_user()
    asking_user_name()
    brain_progression_task()
    brain_progression_logic()
