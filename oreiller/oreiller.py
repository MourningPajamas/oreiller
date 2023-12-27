
try:
    from PIL import Image
    from PIL import ImageDraw
except ImportError:
    pass

class Oreiller:
    image = None
    _images = []

    @classmethod
    def open(cls, *args, **kwargs):
        img = Image.open(*args, **kwargs)
        cls._images.append(img)
        return img
    
    @classmethod
    def new(cls, *args, **kwargs):
        img = Image.new(*args, **kwargs)
        cls._images.append(img)
        cls.image = img
        return img
    
    @classmethod
    def line(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        draw.line(*args, **kwargs)


    @classmethod
    def oline(cls, x1, y1, x2, y2, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        shape = [(x1, y1), (x2, y2)]
        draw.line(shape, **kwargs)

    @classmethod
    def cleanup(cls):
        for img in cls._images:
            img.close()