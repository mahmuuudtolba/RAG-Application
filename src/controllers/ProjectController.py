from .BaseController import BaseController
from fastapi import UploadFile , status 
from models import ResponseSignal
from fastapi.responses import JSONResponse
import os 
import aiofiles


class ProjectController(BaseController):

    def __init__(self):
        super().__init__()



    def get_project_path(self , project_id :str):
        project_path = os.path.join(
            self.file_dir , 
            project_id
        )

        if not os.path.exists(project_path):
            os.makedirs(project_path)

        return project_path
    

        

