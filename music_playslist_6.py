class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Playlist:
    def __init__(self):
        self.current = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.current:
            self.current = new_song
        else:
            temp = self.current
            while temp.next:
                temp = temp.next
            temp.next = new_song
            new_song.prev = temp

    def remove_song(self, title):
        temp = self.current
        while temp:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.current:
                    self.current = temp.next or temp.prev
                return True
            temp = temp.next
        return False

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current
        return None

    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current
        return None

    def current_song(self):
        return self.current if self.current else None


playlist = Playlist()
playlist.add_song("Shape of You", "Ed Sheeran")
playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Blinding Lights", "The Weeknd")

print("Current:", playlist.current_song())
playlist.next_song()
print("Next:", playlist.current_song())
playlist.previous_song()
print("Previous:", playlist.current_song())
playlist.remove_song("Shape of You")
print("After removal:", playlist.current_song())