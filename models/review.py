from models.base_model import BaseModel


class Review(BaseModel):
    """Creates a class review that
    inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
