from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from model import Post, PostCreate, UpdatePost
import json
from datetime import datetime

app = FastAPI()
DATA_FILE = 'data/posts.json'

def load_data():
    with open(DATA_FILE,'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open(DATA_FILE,'w') as f:
        json.dump(data, f, indent=2, default=str)

def generate_next_id(data: dict) -> str:
    if not data:
        return "P001"
    numeric_ids = [int(k[1:]) for k in data.keys() if k.startswith("P") and k[1:].isdigit()]
    next_number = max(numeric_ids) + 1
    return f"P{next_number:03d}"

@app.get('/view')
def view_post():
    data = load_data()
    return data


@app.get('/view/{post_id}')
def get_post(post_id:str = Path(..., description="Id of the post in the DB",example="P001")):
    
    data = load_data()

    if post_id in data:
        return data[post_id]
    
    raise HTTPException(status_code=404, detail= "Post not found")



    
# creation of post
@app.post('/create')
def create_post(new_post:PostCreate):
    # load the data
    data = load_data()
    # generate the post id 
    post_id = generate_next_id(data)
    # create a post
    post = Post(id=post_id,created_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),**new_post.model_dump())

    # create a dictionery
    data[post_id] = post.model_dump(exclude=['id'])

    # save the data
    save_data(data=data)

    return post


# update post
@app.put('/edit/{post_id}')
def update_post(post_id:str, post_update:UpdatePost):
    data = load_data()

    if post_id not in data:
        raise HTTPException(status_code=404, detail='Post not found')
    
    existing_post_info = data[post_id]
    updated_post_info = post_update.model_dump(exclude_unset=True)

    for key, value in updated_post_info.items():
        existing_post_info[key] = value
    

    data[post_id] = existing_post_info

    save_data(data)

    return JSONResponse(status_code=200, content = {'message':'Post updated sucessfully'})



# Delete the post
@app.delete('/delete/{post_id}')
def delete_post(post_id:str):
    data = load_data()

    if post_id not in data:
        raise HTTPException(status_code=404, detail="Post not found!")
    
    del data[post_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Post deleted sucessfully'})




