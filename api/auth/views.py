from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)


@api_view(['POST'])
def signup_user(request):
    data = request.data

    username = data.get('username')
    password = data.get('password')
    telegram_id = data.get('telegram_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    region = data.get('region')
    city = data.get('city')
    org_name = data.get('org_name')

    if all((username, password)):
        if not get_user_model().objects.filter(username=username).exists():
            user = get_user_model().objects.create_user(
                username=username,
                password=password
            )

            if telegram_id is not None:
                user.telegram_id = telegram_id

            if first_name is not None:
                user.first_name = first_name

            if last_name is not None:
                user.last_name = last_name

            if region is not None:
                user.region = region

            if city is not None:
                user.city = city

            if org_name is not None:
                user.org_name = org_name

            user.save()

            return Response({'success': 'user successfully created'}, status=HTTP_201_CREATED)

        return Response({'error': 'this phone number already exists'}, status=HTTP_400_BAD_REQUEST)

    return Response({'error': 'phone number and password must not be null'}, status=HTTP_400_BAD_REQUEST)
