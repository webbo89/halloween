#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


def tell_my_name(ghost_name):
    print("eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeee {} eeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n"
          "eeeeeeeeeeeeeeeeeeeeeee \n".format(ghost_name)
          )
    for letter in ghost_name:
        print("~{letter}~".format(letter=letter))
