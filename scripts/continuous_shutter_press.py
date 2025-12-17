import os
import sys
from dotenv import load_dotenv
import requests
import json
import time


load_dotenv()


BASE_URL=os.getenv('CAMERA_URL')
SHOOTING_API_PATH='/shooting/control/shutterbutton/manual'

API_URL=f'{BASE_URL}{SHOOTING_API_PATH}'


def press_shutter_button(auto_focus=False):
    data = {
        'action': 'full_press',
        'af': auto_focus
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    requests.post(url=API_URL, headers=headers, data=json.dumps(data))    


def release_shutter_button(auto_focus=False):
    data = {
        'action': 'release',
        'af': auto_focus
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    requests.post(url=API_URL, headers=headers, data=json.dumps(data))


print('--- CONTINUOUS SHUTTER PRESS ---\n')
number_of_photos = int(input('How many photos do you want to take?\n'))
delay_in_seconds = int(input('What is the delay between each photo in seconds?\n'))

confirm = input('\nDo you confirm those two values are correct? Y/n\n')

if not (confirm == '' or confirm.upper() == 'Y'):
    sys.exit()
    

try:

    for i in range(number_of_photos):
        print(f'Taking photo number {(i+1)} of {number_of_photos}')
        
        press_shutter_button()
        release_shutter_button()
        time.sleep(delay_in_seconds)

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    release_shutter_button()
    sys.exit()
