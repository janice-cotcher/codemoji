# winking face
# following a tutorial to build a winking emoji face.
# adapted from https://teacherslearningcode.trinket.io/introduction-to-python-graphics-with-processingpy#/code-moji/getting-started


def head():
    """Emoji Head"""
    fill(255, 218, 0)  # yellow
    ellipse(300, 300, 400, 400)  # circle

def open_mouth():
    """Open black mouth"""
    fill(0, 0, 0)  # black
    arc(300, 400, 200, 100, 0, PI)  # semi-circle

def tongue():
    """Red tongue"""
    fill(255, 0, 0)  # red
    arc(300, 400, 120, 160, 0, PI)  # tongue

def eye(x):
    """single eye"""
    fill(255, 255, 255)  # white
    ellipse(x, 300, 150, 150)  # circle
    # Pupil
    fill(0, 0, 0)  # black
    ellipse(x, 300, 50, 50)  # circle


def wink():
    """ Winking Eye"""
    fill(0)  # black
    arc(200, 300, 125, 60, PI, TWO_PI)  # the winking eye


def setup():
    size(600, 600)  # Size of our sketch
    background(100, 100, 100)  # Background colour
    noStroke()  # Removes the outline around our shapes
    head()
    eye(200)
    # right eye
    eye(400)
    open_mouth()


def draw():
    """the function is responsible for creating the emoji and making it wink"""
    return

    
def keyTyped():
    head()
    # right eye
    eye(400)
    open_mouth()
    # left eye
    wink()
    tongue()


def keyReleased():
    head()
    eye(200)
    # right eye
    eye(400)
    open_mouth()
