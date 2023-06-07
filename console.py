import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

pdb.set_trace()
artist1 = Artist('Weezer')
artist2 = Artist('Eels')
artist_repository.save(artist1)
artist_repository.save(artist2)
all_artists = artist_repository.select_all()
one_artist = artist_repository.select(artist1.id)
artist_repository.update(artist1.id)
artist_repository.delete(artist2.id)


album1 = Album('The Blue Album', 'Rock', artist1)
album2 = Album('Pinkerton', 'Rock', artist1)
album_repository.save(album1)
album_repository.save(album2)
all_albums = album_repository.select_all()
one_album = album_repository.select(album1.id)
album_list = album_repository.albums_by_artist(artist1)
album_repository.update(album1)
album_repository.delete(album2)


