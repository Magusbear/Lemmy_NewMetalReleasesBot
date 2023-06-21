from datetime import datetime, timedelta


def sortByReleaseType(type, wanted_list,wantedGenre,wantedDay,wantedMonthString):                                    # Post only specific types of releases and in order
    releases_list = []
    for data in wanted_list:
        band = data[0]
        album = data[1]
        release_type = data[2]
        if release_type.lower() == type.lower():
            releases_list.append(f'- {band} - {album} ({release_type})\n')
    return releases_list

def get_date():
    today = datetime.today()
    currentWeekday = today.weekday()
    wantedMonth = today.strftime("%B")
    wantedDay = today.strftime("%d")
    return today, currentWeekday, wantedMonth, wantedDay