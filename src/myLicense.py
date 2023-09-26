###############################################################################################################
#    myLicense.py   Copyright (C) <2020-2023>  <Kevin Scott>                                                       #
#                                                                                                             #
#    Two methods to print out License information, one short and one long.                                    #
#    One method to either print text to screen or a file.                                                     #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2020-2023>  <Kevin Scott>                                                                      #
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

from src.console import console

from rich import print
from rich.text import Text
from rich.panel import Panel

########################################################################################### printSortLicense ######
def printShortLicense(Name, Version):
    text = Text()
    text.append(f"This program comes with ABSOLUTELY NO WARRANTY; for details type `{Name} -l'.\n")
    text.append("This is free software, and you are welcome to redistribute it under certain conditions.")
    console.print(Panel.fit(text, title=f"{Name} {Version}", subtitle="Copyright (C) 2023  Kevin Scott"))

########################################################################################### printLongLicense ######
def printLongLicense(Name, Version):
    print(f"""
    {Name} {Version}  Copyright (C) 2020-2021  Kevin Scott

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either myVERSION 3 of the License, or
    (at your option) any later VERSION.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """, end="")
