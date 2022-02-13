import os

import pytest
from labyrinth import Labyrinth


def test_get_labyrinth_with_two_starts():
    with pytest.raises(ValueError):
        Labyrinth.from_file('../data/labyrinth_with_two_start.txt')


def test_get_labyrinth_with_now_wat():
    labyrinth = Labyrinth.from_file('../data/labyrinth_with_now_way.txt')
    expected = """
    ##############
    #   #        #
    # S #        #
    #      #     #
    ##########   #
    #       #F# ##
    # #########  #
    #   #  #     #
    #   #        #
    ##############
    """
    labyrinth.find_route_in_labyrinth()
    labyrinth.save_labyrinth_to_file('./test_lab.txt')

    try:
        with open('./test_lab.txt', encoding='utf-8') as f:
            saved_labyrinth: str = f.read()
        assert expected.split() == saved_labyrinth.split()
    finally:
        os.remove('./test_lab.txt')


def test_labyrinth_find_route():
    labyrinth = Labyrinth.from_file('../data/labyrinth-1.txt')
    expected = """
    ##############
    #   #________#
    # S #_ #####_#
    # ____ #  ##_#
    ######### #__#
    #       _F#_##
    # ######_ #__#
    #   #  #_###_#
    #   #   _____#
    ##############
    """
    labyrinth.find_route_in_labyrinth()
    labyrinth.save_labyrinth_to_file('./test_lab.txt')

    try:
        with open('./test_lab.txt', encoding='utf-8') as f:
            saved_labyrinth: str = f.read()
        assert expected.split() == saved_labyrinth.split()
    finally:
        os.remove('./test_lab.txt')