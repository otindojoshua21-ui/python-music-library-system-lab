class Song:
    # Class attributes to track global song data
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """Initialize a new Song instance and update class attributes"""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call class methods to update tracking
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one"""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add a new genre to the genres list (ensure no duplicates)"""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add a new artist to the artists list (ensure no duplicates)"""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update genre_count dictionary with genre frequency"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update artist_count dictionary with artist frequency"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1