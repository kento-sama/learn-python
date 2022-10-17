def do_stuff_with_number(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            do_stuff_with_number(0)


catch_this()


actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        name = actor["name"].split()
        actor["last_name"] = name[1]
        return actor["last_name"]


get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
