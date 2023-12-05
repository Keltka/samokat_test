import sender_stand_request

def test1():
    track=sender_stand_request.create_order()
    user_response=sender_stand_request.get_order(track)
    assert user_response.status_code == 200