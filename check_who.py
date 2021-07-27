# __  __           _        _
#|  \/  | __ _  __| | ___  | |__  _   _
#| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |
#| |  | | (_| | (_| |  __/ | |_) | |_| |
#|_|  |_|\__,_|\__,_|\___| |_.__/ \__, |
#                                 |___/
# ____              _   _
#/ ___|  __ _ _ __ | |_(_) __ _  __ _ ____
#\___ \ / _` | '_ \| __| |/ _` |/ _` |_  /
# ___) | (_| | | | | |_| | (_| | (_| |/ /
#|____/ \__,_|_| |_|\__|_|\__,_|\__, /___|
#                               |___/
# Git - https://github.com/santiagz

import requests
import time
import re
import subprocess
from conf import chat_id, BOT_API, car_name

regex = r"(\d+\-\d+\-\d+\s+\d+\:\d+)\s\((\d+\.\d+\.\d+\.\d+)"
headers = {'Content-type': 'application/json', }

def get_sign():
    subp = subprocess.Popen("who", shell=True, stdout=subprocess.PIPE)
    result = subp.stdout.read()
    return result

if __name__ == "__main__":
    main_storage = ['10.0.6.17']
    while 1:
        res = get_sign()
        matches = re.finditer(regex, res.decode('utf-8'), re.MULTILINE)
        finds = []
        for matchNum, match in enumerate(matches, start=1):

            tmplist = []
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                tmplist.append(match.group(groupNum))
            finds.append(tmplist)

        for elem in finds:
            if elem[1] not in main_storage:
                req = requests.get('https://ipinfo.io/' + elem[1] + '?token=ce6bd03aa6f28d')
                country = req.json()
                if "country" in country:
                    response = requests.post(
                        'https://api.telegram.org/bot'+BOT_API+
                        '/sendMessage?chat_id='+chat_id+'&text= ATTENTION!\n🍯 HoneyPot\n\nCar: '+car_name+'\n\n💻 Signed in '
                        'from\n🔫IP: ' + elem[1] + '\n🏴 From country: ' + country[
                            "country"] + '\n\n⏱️At (local time): ' + elem[0], headers=headers)
                    main_storage.append(elem[1])
                else:
                    response = requests.post(
                        'https://api.telegram.org/bot'+BOT_API+
                        '/sendMessage?chat_id='+chat_id+'&text= ATTENTION!\n🍯 HoneyPot\n\nCar: '+car_name+'\n\n💻 Signed in from\n🔫IP: ' +
                        elem[1] + '\n🏴 LOCAL IP' + '\n\n⏱️At (local time): ' + elem[
                            0], headers=headers)
                    main_storage.append(elem[1])
        time.sleep(3)
