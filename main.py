import datetime
from requests_html import HTMLSession
from datetime import timedelta

# parameters
from_city = "Dhaka"
to_city = "Sylhet"

date = datetime.datetime.today()
delta_time = timedelta(days=1)
print('\n')
print(f"**   {from_city} ->> {to_city}   **")
print('\n')
for i in range(11):

    black_day = True

    if i != 0:
        date += delta_time

    formatted_date = date.strftime("%d-%b-%Y")
    print(f">>>>><<<<<<<<<<<<< {formatted_date} <<<<<<<<<<<<<<<<<<<<<<<")
    print('\n')

    host_url = f"https://eticket.railway.gov.bd/booking/train/search/en?fromcity={from_city}&tocity={to_city}&doj={formatted_date}&class=S_CHAIR"
    #url = 'https://eticket.railway.gov.bd/booking/train/search/en?fromcity=Dhaka&tocity=Bhairab_Bazar&doj=30-Jun-2023&class=S_CHAIR'

    session = HTMLSession()
    response = session.get(host_url)

    response.html.render(sleep=1, keep_page=True)

    body = response.html.find('body', first=True)
    trains = body.find('.row.single-trip-wrapper.list_rows')
    #print(len(trains))

    # each train
    for train in trains:
        found_first_seat = False
        train_name = train.find('h2', first=True).text
        seat_types = train.find('.single-seat-class')
        for seat_type in seat_types:
            seat_class_name = seat_type.find('.seat-class-name', first=True).text
            seat_count = int(seat_type.find('.all-seats', first=True).text)
            if seat_count > 0:
                black_day = False
                if found_first_seat is False:
                    print(f"{train_name}")
                    print('---------------------------------')
                print(f"{seat_class_name:<25}{seat_count}")
                found_first_seat = True

        if found_first_seat:
            print("\n")

    if black_day:
        print("NO SEATS AVAILABLE")
    print('\n')