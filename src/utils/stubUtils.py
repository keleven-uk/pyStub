###############################################################################################################
#    duplicateUtils.py   Copyright (C) <2020-2021>  <Kevin Scott>                                             #                                                                                                             #                                                                                                             #
#    A number of helper and utility functions                                                                 #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2020-2021>  <Kevin Scott>                                                                 #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

import os

######################################################################################## loadExplorer() ######
def loadExplorer(logger):
    """  Load program working directory into file explorer.
    """
    try:
        os.startfile(os.getcwd(), "explore")
    except NotImplementedError as error:
        logger.error(error)
    exit(0)


def logTextLine(textLine, textFile):
    """  if the textFile is set, then write the line of text to that file, else print to screen.

         textLine needs to be a string, for f.write - NOT a path.
    """
    if textFile:
        with open(textFile, encoding='utf-8', mode="a") as f:     # Open in amend mode, important.
            f.write(textLine + "\n")
    else:
        print(textLine)
