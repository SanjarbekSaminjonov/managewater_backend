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
def receive_well_message(request):
    data = request.data
    height = data.get('level')
    meneral = data.get('meneral')
    net = data.get('net')
    bat = data.get('bat')
    temperature = data.get('temp')
    is_charging = data.get('charging')

    device_id = data.get('device_id')

    if all((height, meneral, net, bat, temperature, is_charging, device_id)):
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
            'datetime': get_formatted_time(datetime.datetime.now())
        },
        status=HTTP_400_BAD_REQUEST
    )

