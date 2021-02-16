import src.data.data_utils as du
import logging

# Define module level logger
log = logging.getLogger(__name__)

class Camera:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    
