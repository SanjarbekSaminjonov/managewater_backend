import datetime
import decimal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from apps.channels.models import ChannelDevice, ChannelMessage, ChannelDeviceVolumeTable


def get_formatted_time(now):
    return now.strftime('%H:%M:%S %d/%m/%Y')


@api_view(['POST'])
def receive_channel_message(request):
    data = request.data
    h = data.get('h')
    bat = data.get('bat')
    is_charging = data.get('charging')
    net = data.get('net')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    device_id = data.get('device_id')

    re_settings = data.get('re_settings', 0)

    device = ChannelDevice.objects.filter(device_id=device_id).first()

    if all((h, bat, is_charging, net, latitude, longitude, device)):

        new_message = ChannelMessage.objects.create(
            device=device,
            h=h,
            bat=bat,
            is_charging=bool(int(is_charging)),
            net=net
        )

        if re_settings and not bool(device.full_height):
            device.full_height = device.height + decimal.Decimal(new_message.h)
        device.latitude = latitude
        device.longitude = longitude
        device.save()

        if device.full_height is not None:
            water_height = device.full_height + device.height_conf - decimal.Decimal(new_message.h)
            water_height_ones = water_height % 10
            water_height_tens = water_height - water_height_ones

            print(water_height_tens, water_height_ones)
            volume_row = ChannelDeviceVolumeTable.objects.filter(
                device_id=device_id).filter(tens=water_height_tens).first()
            if volume_row is not None:
                print(volume_row, water_height_ones, volume_row.get_value(water_height_ones))
                new_message.water_volume = volume_row.get_value(water_height_ones)
                new_message.save()

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
