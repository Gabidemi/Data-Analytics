candy = ('Milky Way', 'Lollipops', 'Snickers')
flavors = ('Milk Chocolate', 'Strawberry', 'Chocolate')

CandyStash = set()
CandyStash.add(flavors[0] + ' ' + candy[0])
CandyStash.add(flavors[1] + ' ' + candy[1])
CandyStash.add(flavors[2] + ' ' + candy[2])

print(f"Today's candy options include: {CandyStash}")
# printing this multiple times, I noticed the items all change positions a few times