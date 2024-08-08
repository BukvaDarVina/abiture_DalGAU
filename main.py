from fastapi import FastAPI


# from pydantic import BaseModel
# from pydantic_extra_types.pendulum_dt import Date
# from rich.json import JSON

app = FastAPI()

# class Event(BaseModel):
#     id: int
#     event_autor_id: int
#     event_name: str
#     event_start: Date
#     event_finish: Date
#     event_description: str
#     event_imgs_urls: JSON
#     event_banner_url: str
#     application_form_id: int
#     feedback_form_id: int
#     survey_form_id: int


fake_base = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Bob"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_base if user.get("id") == user_id]


# fake_base2 = [
#     {"id": 1, "role": "admin", "name": "Bob"},
#     {"id": 2, "role": "investor", "name": "Bob"},
#     {"id": 3, "role": "trader", "name": "Matt"},
# ]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_base))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


