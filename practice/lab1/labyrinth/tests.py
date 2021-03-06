import os

import pytest
from labyrinth import *


def test_get_labyrinth_with_two_starts():
    labyrinth = get_labyrinth_from_file('data/labyrinth_with_two_start.txt')
    cells = find_start_and_finish_cell(labyrinth)
    assert cells is None


def test_get_labyrinth_with_no_wave():
    labyrinth = get_labyrinth_from_file('data/labyrinth_with_now_way.txt')
    expected = """
    ##############
    #   #        #
    # A #        #
    #      #     #
    ##########   #
    #       #B# ##
    # #########  #
    #   #  #     #
    #   #        #
    ##############
    """
    labyrinth = find_route_in_labyrinth(labyrinth)
    save_labyrinth_to_file(labyrinth, './test_lab.txt')

    try:
        with open('./test_lab.txt', encoding='utf-8') as f:
            saved_labyrinth: str = f.read()
        assert expected.split() == saved_labyrinth.split()
    finally:
        os.remove('./test_lab.txt')


def test_labyrinth_find_route():
    labyrinth = get_labyrinth_from_file('data/labyrinth-1.txt')
    expected = """
    ##############
    #   #........#
    # A #. #####.#
    # .... #  ##.#
    ######### #..#
    #       .B#.##
    # ######. #..#
    #   #  #.###.#
    #   #   .....#
    ##############
    """
    labyrinth = find_route_in_labyrinth(labyrinth)
    save_labyrinth_to_file(labyrinth, './test_lab.txt')

    try:
        with open('./test_lab.txt', encoding='utf-8') as f:
            saved_labyrinth: str = f.read()
        assert expected.split() == saved_labyrinth.split()
    finally:
        os.remove('./test_lab.txt')
