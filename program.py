import csv

with open("followers.csv", 'r') as file:
    followers = csv.reader(file)
    ers = [user for user in followers]

    with open("following.csv", 'r') as file:
        following = csv.reader(file)
        ing = [user for user in following]

        unfollow = [user for user in ing if user not in ers]
        for row in unfollow:
            print(row)