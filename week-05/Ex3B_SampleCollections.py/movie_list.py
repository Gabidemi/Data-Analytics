FavMovies = ['7 Deadly Sins', 'JJK', 'Demon Slayer', 'KPop Demon Hunters', 'Bubble']

print(f'The list fav_movies includes my top {len(FavMovies)} favorite movies.')
print(FavMovies)

# One list is alphabetically sorted
# The other list is not sorted alphabetically
print('-' * 20)
print("Alphabetical Vs Non Alphabetical")
print('-' * 20)

print(sorted(FavMovies))
print(FavMovies)

# The .sort method sorted the movies alphabetically and stores them even when called again.
# the sorted() only worked on the list, but did not update the list when you run it again 
print('-' * 20)
print(".Sort vs Sorted()")
print('-' * 20)

FavMovies.sort()
print(FavMovies)

print('-' * 20)
print("Added new movie")
print('-' * 20)
FavMovies.append('Kabaneri of the Iron Fortress')
print(f'This updated list fav_movies includes my top {len(FavMovies)} favorite movies.')
print(FavMovies)