###############################################################################################################
#    pyStub   Copyright (C) <2021-23>  <Kevin Scott>                                                             #                                                                                                             #
#    A skeleton program for a python command line script.                  .                                  #
#                                                                                                             #
#                                                                                                             #
#     For changes see history.txt                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2021-23>  <Kevin Scott>                                                                      #
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

from plyer import notification

import src.myTimer as myTimer
import src.myConfig as myConfig
import src.myLogger as myLogger
import src.myLicense as myLicense
import src.utils.stubUtils as stubUtils
import src.args as args

############################################################################################### __main__ ######

if __name__ == "__main__":

    myConfig = myConfig.Config()                   # Need to do this first.

    LGpath  = "data\\" +myConfig.NAME +".log"      #  Must be a string for a logger path.
    logger  = myLogger.get_logger(LGpath)          #  Create the logger.
    timer   = myTimer.Timer()                      #  Create a timer.
    icon    = "resources\\tea.ico"                 #  icon used by notifications
    timeout = 5                                    #  timeout used by notifications in seconds

    try:
        timer.Start()
        stubUtils.logPrint(logger, False, "-" * 100, "info")
        stubUtils.logPrint(logger, True, f"{myConfig.NAME} {myConfig.VERSION} .::. Started at {timer.rightNow}", "info")
        if myConfig.NOTIFICATION:
            notification.notify(myConfig.NAME, message, myConfig.NAME, icon, timeout)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    args.parseArgs(myConfig.NAME, myConfig.VERSION, logger)     #  **  Need to catch arguments if required.  **

    myLicense.printShortLicense(myConfig.NAME, myConfig.VERSION)

    try:
        timeStop = timer.Stop
        stubUtils.logPrint(logger, True, f"{myConfig.NAME} {myConfig.VERSION} .::. Completed in {timeStop}", "info")
        if myConfig.NOTIFICATION:
            notification.notify(myConfig.NAME, message, myConfig.NAME, icon, timeout)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    exit(0)
