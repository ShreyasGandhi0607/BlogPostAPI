from pydantic import BaseModel, Field
from typing import Annotated, Optional
from datetime import datetime

class PostCreate(BaseModel):

    title : Annotated[str, Field(..., description='title of the blog post')]
    content : Annotated[str, Field(..., description='Content of the post')]
    author : Annotated[str, Field(..., description='Name of the author')]


class Post(PostCreate):
    id : Annotated[str, Field(description='Id of the post')]
    created_at : Annotated[datetime, Field(default_factory=datetime.utcnow,description='Time of creation of post')]


class UpdatePost(BaseModel):
    title : Annotated[Optional[str], Field(default=None)]
    content : Annotated[Optional[str], Field(default=None)]
    author : Annotated[Optional[str],Field(default=None)]
