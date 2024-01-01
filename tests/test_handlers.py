import json
import asyncio


# Your existing fixtures and setup code...

# Use asyncio.run to execute asynchronous tests
async def run_async_test(test_function):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_function())

# Your test function
async def test_create_user(client, get_user_from_database):
    user_data = {
        "name": "Nikolai",
        "surname": "Sviridov",
        "email": "lol@kek.com"
    }
    resp = await client.post("/user/", data=json.dumps(user_data))
    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp["name"] == user_data["name"]
    assert data_from_resp["surname"] == user_data["surname"]
    assert data_from_resp["email"] == user_data["email"]
    assert data_from_resp["is_active"] is True
    users_from_db = await get_user_from_database(data_from_resp["user_id"])
    assert len(users_from_db) == 1
    user_from_db = dict(users_from_db[0])
    assert user_from_db["name"] == user_data["name"]
    assert user_from_db["surname"] == user_data["surname"]
    assert user_from_db["email"] == user_data["email"]
    assert user_from_db["is_active"] is True
    assert str(user_from_db["user_id"]) == data_from_resp["user_id"]

# Run the asynchronous test using asyncio.run
def test_async_create_user(client, get_user_from_database):
    asyncio.run(run_async_test(lambda: test_create_user(client, get_user_from_database)))
