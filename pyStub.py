###############################################################################################################
#    pyStub   Copyright (C) <2021>  <Kevin Scott>                                                             #                                                                                                             #
#    A skeleton program for a python command line script.                  .                                  #
#                                                                                                             #
#                                                                                                             #
#     For changes see history.txt                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2021>  <Kevin Scott>                                                                      #
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

import textwrap
import argparse

from plyer import notification

import src.myTimer as myTimer
import src.myConfig as myConfig
import src.myLogger as myLogger
import src.myLicense as myLicense
import src.utils.stubUtils as stubUtils

############################################################################################## parseArgs ######
def parseArgs():
    """  Process the command line arguments.

         Checks the arguments and will exit if not valid.

         Exit code 0 - program has exited normally, after print version, licence or help.
         Exit code 1 - program has exited normally, after Loading program working directory into file explorer.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""\
        A Python MP3 Duplicate finder.
        -----------------------
        The program will scan a given directory and report duplicate MP3 files."""),
        epilog=f" Kevin Scott (C) 2020 :: {myConfig.NAME} {myConfig.VERSION}")

    parser.add_argument("-l", "--license", action="store_true", help="Print the Software License.")
    parser.add_argument("-v", "--version", action="store_true", help="Print the version of the application.")
    parser.add_argument("-e", "--explorer", action="store_true", help="Load program working directory into file explorer.")

    args = parser.parse_args()

    if args.version:
        myLicense.printShortLicense(myConfig.NAME, myConfig.VERSION)
        logger.info(f"End of {myConfig.NAME} V{myConfig.VERSION}: version")
        print("Goodbye.")
        exit(0)

    if args.license:
        myLicense.printLongLicense(myConfig.NAME, myConfig.VERSION)
        logger.info(f"End of {myConfig.NAME} V{myConfig.VERSION} : Printed Licence")
        print("Goodbye.")
        exit(1)

    if args.explorer:
        stubUtils.loadExplorer(logger)             # Load program working directory n file explorer.
        print("Goodbye.")
        exit(0)

#  ** Need to return arguments if required  **


############################################################################################### __main__ ######

if __name__ == "__main__":

    myConfig = myConfig.Config()                   # Need to do this first.

    LGpath  = "data\\" +myConfig.NAME +".log"      #  Must be a string for a logger path.
    logger  = myLogger.get_logger(LGpath)          #  Create the logger.
    timer   = myTimer.Timer()                      #  Create a timer.
    icon    = "resources\\tea.ico"                 #  icon used by notifications
    timeout = 5                                    #  timeout used by notifications in seconds

    try:
        timeStart = timer.Start
        message = f"{myConfig.NAME} {myConfig.VERSION} .::. Started at {timeStart}"
        logger.info("-" * 100)
        print(message)
        logger.info(message)
        if myConfig.NOTIFICATION: notification.notify(myConfig.NAME, message, myConfig.NAME, icon, timeout)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    parseArgs()     #  **  Need to catch arguments if required.  **

    try:
        timeStop = timer.Stop
        message = f"{myConfig.NAME} {myConfig.VERSION} .::. Completed in {timeStop}"
        print(message)
        logger.info(message)
        if myConfig.NOTIFICATION: notification.notify(myConfig.NAME, message, myConfig.NAME, icon, timeout)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    exit(0)
