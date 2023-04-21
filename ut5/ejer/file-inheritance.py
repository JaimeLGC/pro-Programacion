class File:
    def __init__(self, path: str):
        self.path = path
        self.content = []

    def add_content(self, content: str):
        self.content.append(content)

    @property
    def size(self):
        size = 0
        for item in self.content:
            size += len(item)
        return size

    @property
    def info(self):
        print(vars(self))


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple
    ):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self):
        print(
            f"{self.path} [size={self.size}B]\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s\nDimensions: {self.dimensions}"
        )


file1 = File("abcd")
file1.add_content("fdfd")
file1.add_content("fdf")
file1.add_content("fd")

file2 = VideoFile(
    "/home/python/vanrossum.mp4", "h264", (23.5454, 31.4343), 487, (1920, 1080)
)
file2.add_content("audio/ogg")
file2.add_content("video/webm")
file2.info
