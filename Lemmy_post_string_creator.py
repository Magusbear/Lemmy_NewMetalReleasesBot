


def postByReleaseType(type, wanted_list,wantedGenre,wantedDay,wantedMonthString):                                    # Post only specific types of releases and in order
    for data in wanted_list:
        band = data[0]
        album = data[1]
        release_type = data[2]
        if release_type.lower() == type.lower():
            print(f'- {band} - {album} ({release_type})\n')

