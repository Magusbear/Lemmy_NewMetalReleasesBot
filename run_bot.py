import metal_archives_scraper
import Lemmy_post_string_creator

wantedGenre = input("What genre releases do you want to post? ")
wantedMonth = input("Which release month (eg. june or 6)? ")
wantedDay = input("Which release day? ")

wanted_list,wantedMonthString = metal_archives_scraper.get_releaseList(wantedGenre,wantedDay,wantedMonth)

release_type_list = ["Full-length","Single","EP"]

print(f'{wantedGenre} releases for {wantedDay} of {wantedMonthString}: \n')
for type in release_type_list:                                  # cheeky way of sorting the list
    Lemmy_post_string_creator.postByReleaseType(type, wanted_list,wantedGenre,wantedDay,wantedMonthString)