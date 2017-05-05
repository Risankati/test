# -*- coding: utf-8 -*-

print "Živjo! Sem program, ki pretvarja kilometre v milje!"

while True:
    km = raw_input("KM >> MI:")
    km = float(km)
    mi = km * 0.621371
    print "{0} KM = {1} MI.".format(km, mi)

    choice = raw_input("Želiš še naprej pretvarjati? (da/ne): ")

    if choice == "da":
        print "HURA!"

    if choice == "ne":
        print "Adijo!"
        break
