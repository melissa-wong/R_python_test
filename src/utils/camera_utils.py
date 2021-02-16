import src.data.data_utils as du
from src.models.camera_model import Camera
import logging

# Define module level logger
log = logging.getLogger(__name__)

def get_camera_param():
    log.debug("Here!")
    du.test()
    camera = Camera(1) 
    return camera.get_id()

if __name__=='__main__':
    logging.basicConfig(level="DEBUG")

    get_camera_param()
