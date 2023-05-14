class File:
    def __init__(self, path: str):
        self.path = self
        self.contents = []

    def add_content(self, content: str):
        self.contents.append(content)

    @property
    def size(self):
        sizes = (len(c) for c in self.contents)
        return sum(sizes)

    @property
    def info(self):
        return f"{self.path} [size={self.size()}B]"


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple[float], duration: int):
        super().__init__(path)
        self.path = path
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self):
        return f"{self.path} [size={self.size}\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s]"


class VideoFile(MediaFile):
    def __init__(
        self,
        path: str,
        codec: str,
        geoloc: tuple[float],
        duration: int,
        dimensions: tuple[int],
    ):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s\nDimensions: {self.dimensions}"
