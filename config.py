"""Загрузка переменных из .env"""
import os
from dotenv import load_dotenv


load_dotenv()

NUMBER_OF_LOGOS = int(os.getenv('NUMBER_OF_LOGOS'))
PAUSE_AMOUNT = float(os.getenv('PAUSE_AMOUNT'))
COLORS = os.getenv('COLORS').split(',')
UP_RIGHT = os.getenv('UP_RIGHT')
UP_LEFT = os.getenv('UP_LEFT')
DOWN_RIGHT = os.getenv('DOWN_RIGHT')
DOWN_LEFT = os.getenv('DOWN_LEFT')

# Список направлений
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
