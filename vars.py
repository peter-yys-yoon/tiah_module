import cv2

"--------------------------------"
# PROJECT_PATH = '/home/peter/extra/Workspace/codes/ictlight'  # OBAMA


"----------------------------- VIDEO -----------------------------"
XVID = cv2.VideoWriter_fourcc(*'XVID')

VIDEO_EXT_LIST = ['mp4', 'avi']

"----------------------------- FONT -----------------------------"
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_THICKNESS = 1

"----------------------------- KEYS  -----------------------------"

BBOX_XY = 'bbox'
BBOX_WH = 'bbox_wh'
BBOX_L_XY = 'bbox_l_wh'
TRACK_ID = 'track_id'

UPPER = 'upper'
LOWER = 'lower'
MEAN = 'mean'

LENGTH = 'length'
FOURCC = 'fourcc'
WIDTH = 'width'
HEIGHT = 'height'
FPS = 'fps'

"----------------------------- COLOR  -----------------------------"
COLOR_RED = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)
COLOR_ORANGE = (0, 129, 255)
COLOR_YELLOW = (15, 217, 255)
COLOR_MAGENTA = (255, 0, 255)
COLOR_LIGHT_GREEN = (9, 249, 17)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)



"----------------------------- COLOR  -----------------------------"

FHD='fhd'
HD='hd'
VGA='vga'
QVGA='qvga'
resolution_set = {
    FHD: (1920, 1080), # 16:9
    HD: (1280, 720), # 16:9
    VGA: (640, 480), # 4:3
    QVGA: (320, 240) # 4:3
}
