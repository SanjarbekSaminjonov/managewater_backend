import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from apps.wells.models import WellDevice, WellDeviceMessage


def get_formatted_time(now):
    return now.strftime('%H:%M:%S %d/%m/%Y')


@api_view(['POST'])
def receive_well_message(request):
    data = request.data
    h = data.get('level')
    mineral = data.get('meneral')
    temperature = data.get('temp')
    bat = data.get('bat')
    is_charging = data.get('charging')
    net = data.get('net')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    device_id = data.get('device_id')

    device = WellDevice.objects.filter(device_id=device_id).first()

    if all((h, mineral, temperature, bat, is_charging, net, latitude, longitude, device)):
        WellDeviceMessage.objects.create(
            device=device,
            h=h,
            mineral=mineral,
            temperature=temperature,
            bat=bat,
            is_charging=bool(int(is_charging)),
            net=net
        )

        device.latitude = latitude
        device.longitude = longitude
        device.save()

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
