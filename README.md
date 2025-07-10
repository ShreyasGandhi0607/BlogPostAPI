
## Features

- Create, Read, Update, and Delete blog posts
- Data stored in JSON
- Streamlit frontend for interaction
- FastAPI backend for API endpoints

---

## Requirements

- Python 3.11+
- FastAPI
- uvicorn
- streamlit
- requests

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/blogpost-api.git
cd blogpost-api

# Create a virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
````

---

## Run the API

```bash
fastapi dev main.py
```

Visit the docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Run the Streamlit Frontend

```bash
streamlit run app.py
```

---

## API Endpoints

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| GET    | `/view`             | Get all blog posts  |
| GET    | `/view/{post_id}`   | Get a specific post  |
| POST   | `/create`           | Create a new post   |
| PUT    | `/edit/{post_id}`   | Update a post       |
| DELETE | `/delete/{post_id}` | Delete a post       |

---

## File Structure

```
blogpost-api/
│
├── main.py              # FastAPI backend
├── app.py               # Streamlit frontend
├── models.py            # Pydantic schemas
├── data/
│   └── posts.json       # Data file
├── requirements.txt     # Python dependencies
└── README.md
```

