# //finding the length of a tuple
tup1 = ("Mary","Wambui","Grace","Martha")
print(len(tup1))
tup2 = ("Nairobi","Kigali","Lagos",)
print(len(tup2))

#//concatenation of tuples
tup3 = tup1 + tup2
print(tup3)

#//index of elements in a tuple
tup4 = ("apple","mango","banana","kiwi","watermelon")
print(tup4[2])
print(tup4[-1])

#//slicing tuples
print(tup4 [0:3])
print(tup4 [2:-1])

#//adding items in a tuple
mountains = ("Mt.Everest","Mt.Kenya","Mt.Longonot")
y = list(mountains)
y.append("Mt.Kilimanjaro")
mountains = tuple(y)
print(mountains)

#//removing items from a tuple
continents = ("Africa","Asia","Europe","Australia","North America","South America")
c = list(continents)
c.remove("Australia")
continents = tuple(c)
print(continents)