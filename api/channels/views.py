import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


def get_formatted_time(now):
    return now.strftime('%H:%M:%S %d/%m/%Y')


@api_view(['POST'])
def receive_channel_message(request):
    data = request.data
    h = data.get('h')
    bat = data.get('bat')
    net = data.get('net')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    device_id = data.get('device_id')

    re_settings = data.get('re_settings', False)
    print(re_settings)

    if all((h, bat, net, latitude, longitude, device_id)):
        return Response(
            {
                'request': 'success',
                'datetime': get_formatted_time(datetime.datetime.now())
            },
            status=HTTP_201_CREATED
        )
    return Response(
        {
            'request': 'error',
            'datetime': get_formatted_time(datetime.datetime.now() + datetime.timedelta(hours=5))
        },
        status=HTTP_400_BAD_REQUEST
    )
