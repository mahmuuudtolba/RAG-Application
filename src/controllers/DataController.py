from .BaseController import BaseController
from fastapi import UploadFile
from .ProjectController import ProjectController
from models import ResponseSignal
import os
import re

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576


    def validate_uploaded_file(self , file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE*self.size_scale :
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        

        return True , ResponseSignal.FILE_UPLOAD_SUCCESS.value
    

    def generate_unique_filepath(self , origin_file_name:str , project_id):
        random_key = self.generate_random_string() 
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_file_name = self.get_clean_file_name(orig_file_name=origin_file_name)

        new_file_path = os.path.join(
            project_path , 
            random_key + "_" + cleaned_file_name
        )


        while os.path.exists(new_file_path):
            random_key = self.generate_random_string() 
            new_file_path = os.path.join(
            project_path , 
            random_key + "_" + cleaned_file_name
        )
            
        print("new_file_path : " , new_file_path)
        print("file_id : " , random_key + "_" + cleaned_file_name)

            
        return new_file_path ,  random_key + "_" + cleaned_file_name




    def get_clean_file_name(self, orig_file_name: str):
        # Replace spaces with underscores first
        orig_file_name = orig_file_name.strip().replace(" ", "_")
        
        # Keep only alphanumeric characters, underscores, and dots
        cleaned_file_name = re.sub(r"[^\w.]", "", orig_file_name)
        
        return cleaned_file_name
