#!/usr/local/bin python

import urllib
import urllib2
import re
import threading
import pygame
from playsound import playsound


def playSound():
    # Add File Path to sound file
    sound_file = "/Users/dhilip/Desktop/1000Hz-5sec.mp3"
    playsound(sound_file)
    return;

def Connect2Web():
  # Add URL to scrub
  aResp = urllib2.urlopen("https://in.bookmyshow.com/buytickets/baahubali-2-the-conclusion-tamil-coimbatore/movie-coim-ET00042450-MT/20170428");
  web_pg = aResp.read();

# Replace with text you want to search
  pattern = "Fun Cinemas"
  m = re.search(pattern, web_pg)
  if m:
    print "Found"
    playSound()
  else:
    print "Nothing found"
    # Currently set for 10 minutes( 10 * 60 = 600 seconds). Modify value here. 
    threading.Timer(600,Connect2Web).start()
    return;

Connect2Web()