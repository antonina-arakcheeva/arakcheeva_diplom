# Антонина Аракчеева, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_get_order_by_track():
    track = sender_stand_request.post_new_order()
    get_response = sender_stand_request.get_order_track(track.json()["track"])
    assert get_response.status_code == 200
