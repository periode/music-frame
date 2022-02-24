#!/usr/bin/python

import argparse
import time
import os

os.environ['WERKZEUG_RUN_MAIN'] = 'true'
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

if os.uname()[1] == "frame":
    import gpiozero

import pygame.mixer as mixer

from preferences import Preferences
from composition import Composition
from logger import Logger
import broker

# --------------------------------------------------------------------------------------

if os.uname()[1] == "frame":
    switch = gpiozero.Button(4)
composition = Composition()
preferences = Preferences()
logger = Logger()

def hardware_loop():
    if switch.is_pressed:
        if composition == None:
            logger.info("switch on...")
            # TODO consider if we always want to have a composition playing when we turn it on?
            # i'd tend to yes
            name = preferences.composition if preferences.composition else "gabor" 
            composition.load(name)
            composition.begin()
    else:
        if composition:
            logger.info("switch off...")
            composition.stop()
            composition = None
            preferences.update('composition', None)
            preferences.save()

def main():
    global composition
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--composition", default=None, help="composition to be played")
    parser.add_argument("-v", "--volume", default=1.0, help="volume (0.0, 1.0)")
    parser.add_argument("-d", "--debug", default=False, help="enable debug output")
    parser.add_argument("-W", "--web", default=True, help="enable web interface")
    parser.add_argument("-p", "--port", default="2046", help="port for the webapp")
    parser.add_argument("-H", "--host", default="0.0.0.0", help="host for the webapp")
    parser.add_argument("-P", "--preferences", default=None, help="load a preferences yaml file")
    args = parser.parse_args()

    if args.preferences:
        preferences.load("yaml", args.preferences)
    else:
        preferences.load("args", args)

    if preferences.debug:
        logger.setDebug()

    if preferences.composition not in Composition.fetch_compositions():
        logger.warning(f"composition {preferences.composition} is not in available compositions: {Composition.fetch_compositions()}!")
    else:
        composition.load(preferences.composition)
        composition.begin()

    if preferences.web:
        broker.preferences = preferences
        broker.spinup()

    try:
        while 1:
            if os.uname()[1] == "frame":
                hardware_loop()
            else:
                logger.debug(f'external host: {os.uname()[1]}')

            time.sleep(0.1)
    except KeyboardInterrupt:
        preferences.save()
        if composition:
            composition.stop()
        
        if mixer:
            mixer.quit()

        logger.info("...coda.\n")
        exit(0)

if __name__ == "__main__":
    logger.info("music frame v0.1")
    main()
    
