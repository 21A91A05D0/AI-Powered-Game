# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:11:00 2025

@author: PRAVEEN
"""

# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
import json

# these expect to find a .env file at the directory above the lesson.                                                         # the format for that file is (without the comment)                                                                           # API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def save_world(world, filename):
    with open(filename, 'w') as f:
        json.dump(world, f)

def load_world(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def get_together_api_key():
    load_env()
    together_api_key = os.getenv("TOGETHER_API_KEY")
    if not together_api_key:
        raise ValueError("TOGETHER_API_KEY not found in environment variables")
    return together_api_key