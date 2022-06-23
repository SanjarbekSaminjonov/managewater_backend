import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from apps.channels.models import ChannelDevice, ChannelMessage


def get_formatted_time(now):
    return now.strftime('%H:%M:%S %d/%m/%Y')


@api_view(['POST'])
def receive_channel_message(request):
    data = request.data
    h1 = data.get('h1')
    h2 = data.get('h2')
    w1 = data.get('w1')
    w2 = data.get('w2')
    vol = data.get('vol')
    bat = data.get('bat')
    net = data.get('net')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    channel_device_id = data.get('basin')

    if all((h1, h2, w1, w2, vol, bat, net, channel_device_id)):
        channel_device = ChannelDevice.objects.filter(device__id=channel_device_id).first()
        if channel_device is not None:
            channel_device_message = ChannelMessage.objects.create(
                channel_device=channel_device,
                h1=h1,
                h2=h2,
                w1=w1,
                w2=w2,
                vol=vol,
                bat=bat,
                net=net
            )
            if all((latitude, longitude)):
                channel_device.latitude = latitude
                channel_device.longitude = longitude
                channel_device.save()
            return Response(
                {
                    'request': 'success',
                    'height': channel_device.height + channel_device.height_conf,
                    'phone': channel_device.phone_number,
                    'datetime': get_formatted_time(
                        channel_device_message.created_at + datetime.timedelta(hours=5)
                    )
                },
                status=HTTP_201_CREATED
            )
    return Response(
        {'request': 'error'},
        status=HTTP_400_BAD_REQUEST
    )
