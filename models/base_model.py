from datetime import datetime
import models
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    format_tm = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, format_tm)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        My_name = type(self).__name__
        My_id = self.id
        My_dict = self.__dict__
        return ("[{}] ({}) {}".format(My_name,
                                      My_id,
                                      My_dict))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        My_dict = self.__dict__.copy()
        My_dict["__class__"] = type(self).__name__
        My_dict["created_at"] = self.created_at.isoformat()
        My_dict["updated_at"] = self.updated_at.isoformat()
        return My_dict
