from typing import List
from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    
    def validate(post):
        return schemas.PostVoteResponse(**post)
    
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    
def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401
    
def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/12345")
    assert res.status_code == 404
    
def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostVoteResponse(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title
    
@pytest.mark.parametrize("title, content, published", [
    ("awesome title", "content", True),
    ("2 title", "aiaia", False),
    ("3 title", "uiuiu", True),
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    
    created_post = schemas.PostCreate(**res.json())
    
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
   
def test_create_post_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts/", json={"title": "title", "content": "content"})
    
    created_post = schemas.PostCreate(**res.json())
    
    assert res.status_code == 201
    assert created_post.title == "title"
    assert created_post.content == "content"
    assert created_post.published == True
    
def test_unauthorized_create_post(client, test_posts):
    res = client.post("/posts/", json={"title": "title", "content": "content"})
    assert res.status_code == 401
    
def test_unauthorized_delete_post(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204
    
def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/4444")
    assert res.status_code == 404
    
def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[2].id}")
    assert res.status_code == 403
    
def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "update title",
        "content": "update content",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.PostResponse(**res.json())
    
    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    
def update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "update title",
        "content": "update content",
        "id": test_posts[2].id
    }
    res = authorized_client.put(f"/posts/{test_posts[2].id}", json=data)
        
    assert res.status_code == 403
    
def test_unauthorized_update_post(client, test_posts):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    
def test_update_post_non_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "update title",
        "content": "update content",
        "id": test_posts[2].id
    }
    res = authorized_client.put("/posts/4444", json=data)
    assert res.status_code == 404