"""
Day 25: OOP - Special Dunder Methods
Focus: Customizing object behaviors with __str__, __repr__, __len__,
__add__, __eq__, and __getitem__.
"""

class Vector2D:
    """Mathematical 2D vector supporting vector addition and scalar operations."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Unambiguous representation for debugging."""
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """User-friendly representation."""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Vector addition: v1 + v2."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        """Equality comparison: v1 == v2."""
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        """Magnitude of vector: abs(v)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


class TrackPlaylist:
    """A music playlist supporting len(), indexing [], and printing."""
    def __init__(self, name: str):
        self.name = name
        self.tracks = []

    def add_track(self, title: str):
        self.tracks.append(title)

    def __len__(self) -> int:
        return len(self.tracks)

    def __getitem__(self, index: int) -> str:
        return self.tracks[index]

    def __str__(self) -> str:
        return f"Playlist '{self.name}' with {len(self.tracks)} tracks"


print("--- Vector2D Magic Methods ---")
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2

print(f"v1: {v1}")
print(f"repr(v1): {repr(v1)}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")
print(f"Magnitude of v1 abs(v1): {abs(v1):.2f}")
print(f"v1 == Vector2D(3, 4)? {v1 == Vector2D(3, 4)}")

print("\n--- TrackPlaylist Magic Methods ---")
pl = TrackPlaylist("Coding Flow")
pl.add_track("Resonance - HOME")
pl.add_track("Sunset - The Midnight")
pl.add_track("Days of Thunder - The Midnight")

print(pl)
print(f"Playlist Length: {len(pl)}")
print(f"First Track (pl[0]): {pl[0]}")
print(f"Last Track (pl[-1]): {pl[-1]}")
