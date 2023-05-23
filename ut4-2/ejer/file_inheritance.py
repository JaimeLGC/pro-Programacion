class File:
    def __init__(self, path: str):
        self.path = path
        self.contents = []

    def add_content(self, content: str) -> None:
        self.contents.append(content)

    @property
    def size(self) -> int:
        size = 0
        for item in self.contents:
            size += len(item)
        return size

    def info(self) -> str:
        f"{self.path} [size={self.size}B]"


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    def info(self) -> str:
        print(
            f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s"
        )


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple
    ):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    def info(self) -> str:
        print(
            f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s\nDimensions: {self.dimensions}"
        )


file2 = VideoFile(
    "/home/python/vanrossum.mp4", "h264", (23.5454, 31.4343), 487, (1920, 1080)
)
file2.add_content("audio/ogg")
file2.add_content("video/webm")
file2.info()
