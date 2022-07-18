from django.forms import ModelForm
from .models import WellDevice
from apps.exist_devices.models import Device


class WellDeviceAdminForm(ModelForm):
    class Meta:
        model = WellDevice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WellDeviceAdminForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(type='well')
