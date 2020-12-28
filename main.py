import re
from datetime import datetime

import aiml
import football_call

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

regexp = re.compile("##FOOTBALL##(.*)##")

# Press CTRL-C to break this loop
print("CZEŚĆ! JESTEM PIŁKARSKIM BOTEM.\nMOGĘ PODAĆ CI WYNIKI MECZÓW Z RÓŻNYCH KRAJÓW I ROZGRYWEK.")

# setting today date to kernel
today_day = str(datetime.today().day)
today_month = str(datetime.today().month)
today_year = str(datetime.today().year)
today_date = today_day + " " + today_month + " " + today_year

kernel.setPredicate("today", today_date)

while True:
    command = input("ZAPYTANIE DO BOTA: ")
    response = kernel.respond(command)
    response = response.replace(r'\n', '\n')
    match = re.search(regexp, response)

#     wyszukiwanie meczów od PODANEJ DATY do PODANEJ DATY z dowolnego kraju z dowolnych rozgrywek
    if match:
        match_info = match.group(1).split(", ")

        date_from_time_str = match_info[0]
        date_from = datetime.strptime(date_from_time_str, '%d %m %Y')

        date_to_time_str = match_info[1]
        date_to = datetime.strptime(date_to_time_str, '%d %m %Y')

        league = kernel.getPredicate("rozgrywki")

        plugin_result = football_call.get_matches_from_league(date_from, date_to, league)
        response = response[:match.start()] + plugin_result + response[match.end():]
    print(response)
