import os, django, csv
#from subprocess import check_output

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from rooms.models        import *
from reviews.models      import *
from users.models        import *
from reservations.models import *

CSV_PATH_CATEGORIES         = 'csv/categories.csv'
CSV_PATH_ROOMS              = 'csv/rooms.csv'
CSV_PATH_ROOM_IMAGES        = 'csv/room_images.csv'
CSV_PATH_AMENITY_TYPES      = 'csv/amenity_types.csv'
CSV_PATH_AMENITIES          = 'csv/amenities.csv'
CSV_PATH_ROOM_AMENITIES     = 'csv/room_amenities.csv'
CSV_PATH_HOUSE_RULES        = 'csv/house_rules.csv'
CSV_PATH_ROOM_HOUSE_RULES   = 'csv/room_house_rules.csv'
CSV_PATH_ROOM_SCHEDULES     = 'csv/room_schedules.csv'
CSV_PATH_USERS              = 'csv/users.csv'
CSV_PATH_WISHLISTS          = 'csv/wishlists.csv'
CSV_PATH_WHSHLIST_ROOMS     = 'csv/wishlist_rooms.csv'
CSV_PATH_REVIEWS            = 'csv/reviews.csv'
CSV_PATH_REVIEW_IMAGES      = 'csv/review_images.csv'
CSV_PATH_RESERVATIONS       = 'csv/reservations.csv'
CSV_PATH_RESERVATION_STATUS = 'csv/reservation_statuses.csv'
CSV_PATH_RESERVATION_ITEMS  = 'csv/reservation_items.csv'

def insert_categories():
    with open(CSV_PATH_CATEGORIES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        
        for row in data_reader:
            Category.objects.create(
                type = row[0]
            )
            
def insert_users():
    with open(CSV_PATH_USERS) as in_file:	
        data_reader = csv.reader(in_file)	
        next(data_reader, None)		        
        for row in data_reader:
            User.objects.create(
                nickname      = row[0],
                email         = row[1],	
                password      = row[2],	
                profile_image = row[3],	
                gender        = row[4],	
                bio           = row[5],	
                birthdate     = row[6],	
                is_superhost  = row[7],	
                kakao_id      = row[8],	
                github_id     = row[8],	
            )

def insert_rooms():
    with open(CSV_PATH_ROOMS) as in_file:	
        data_reader = csv.reader(in_file)	
        next(data_reader, None)
        for row in data_reader:
            Room.objects.create(
                name               = row[0],
                description        = row[1],	
                district           = row[2],	
                neighberhood       = row[3],	
                price              = row[4],	
                address            = row[5],	
                guests             = row[6],	
                beds               = row[7],	
                bedrooms           = row[8],	
                baths              = row[9],	
                check_in_time      = row[10],	
                check_out_time     = row[11],	
                is_instant_booking = row[12],	
                latitute           = row[13],	
                longitute          = row[14],	
                user_id            = row[15],	
                category_id        = row[16],	
            )
            
def insert_room_images():
    with open(CSV_PATH_ROOM_IMAGES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            RoomImage.objects.create(
                image_url = row[0],
                room_id   = row[1],
            )

def insert_amenity_types():
    with open(CSV_PATH_AMENITY_TYPES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            AmenityType.objects.create(
                name = row[0]
            )

def insert_amenities():
    with open(CSV_PATH_AMENITIES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Amenity.objects.create(
                name            = row[1],
                amenity_type_id = row[0],
                icon_url        = row[2]
            )

def insert_room_amenities():
    with open(CSV_PATH_ROOM_AMENITIES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            RoomAmenity.objects.create(
                room_id    = row[0],
                amenity_id = row[1]
            )

def insert_house_rules():
    with open(CSV_PATH_HOUSE_RULES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            HouseRule.objects.create(
                name     = row[0],
                icon_url = row[1]
            )

def insert_room_house_rules():
    with open(CSV_PATH_ROOM_HOUSE_RULES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            RoomHouseRule.objects.create(
                room_id       = row[0],
                house_rule_id = row[1]
            )

def insert_room_schedules():
    with open(CSV_PATH_ROOM_SCHEDULES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            RoomSchedule.objects.create(
                check_in  = row[0],
                check_out = row[1],
                room_id   = row[2]
            )

def insert_wishlists():
    with open(CSV_PATH_WISHLISTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Wishlist.objects.create(
                name    = row[0],
                user_id = row[1]
            )

def insert_wishlist_rooms():
    with open(CSV_PATH_WHSHLIST_ROOMS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            WishlistRoom.objects.create(
                room_id     = row[0],
                wishlist_id = row[1]
            )
            
def insert_reviews():
    with open(CSV_PATH_REVIEWS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Review.objects.create(
                content          = row[0],
                accuracy         = row[1],
                communication    = row[2],
                cleanliness      = row[3],
                location         = row[4],
                check_in         = row[5],
                cost_performance = row[6],
                user_id          = row[7],
                room_id          = row[8]
            )

def insert_review_images():
    with open(CSV_PATH_REVIEW_IMAGES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            ReviewImage.objects.create(
                image_url = row[0],
                review_id = row[1]
            )             
    
def insert_reservation_status():
    with open(CSV_PATH_RESERVATION_STATUS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            ReservationStatus.objects.create(
                status = row[0]
            )

def insert_reservation():
    with open(CSV_PATH_RESERVATIONS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Reservation.objects.create(
                reservation_code      = row[0],
                reservation_status_id = row[1],
                check_in              = row[2],
                check_out             = row[3],
                user_id               = row[4],
                room_id               = row[5],
            )

def insert_reservation_items():
    with open(CSV_PATH_RESERVATION_ITEMS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            ReservationItem.objects.create(
                guests           = row[0],
                room_schedule_id = row[1],
                reservation_id   = row[2]
            )
    
def insert_test():
    pass

if __name__ == "__main__":
    # insert_categories()
    # insert_users()
    # insert_rooms()
    # insert_room_images()
    # insert_amenity_types()
    # insert_amenities()
    # insert_room_amenities()
    # insert_house_rules()
    insert_room_house_rules()
    # insert_room_schedules()
    # insert_wishlists()
    # insert_wishlist_rooms()
    # insert_reviews()
    # insert_review_images()
    # insert_reservation_status()
    # insert_reservation()
    # insert_reservation_items()
    # insert_test()
    insert_test()