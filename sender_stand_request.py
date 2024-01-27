import requests
import configuration
import data


def post_new_order():  # создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def get_order_track(track):  # получение заказа по трэк-номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                        params={"t": track})
