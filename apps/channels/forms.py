from django.forms import ModelForm
from .models import ChannelDevice, ChannelDeviceVolumeTable
from apps.exist_devices.models import Device


class ChannelDeviceAdminForm(ModelForm):
    class Meta:
        model = ChannelDevice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChannelDeviceAdminForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(type='channel')


class ChannelDeviceForm(ModelForm):
    class Meta:
        model = ChannelDevice
        fields = ('device', 'name', 'phone_number', 'height')

    def __init__(self, *args, **kwargs):
        super(ChannelDeviceForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(is_active=False).filter(type='channel')

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-full mt-3 p-1 border-gray-900 rounded-md ' \
                                                  'focus:border-indigo-600 focus:ring focus:ring-opacity-40' \
                                                  'focus:ring-indigo-500 border-2 border-black border-slate-500'

    def save(self, master=None, commit=True):
        obj = super(ChannelDeviceForm, self).save(commit=False)
        if master:
            obj.master = master
        if commit:
            obj.save()
        return obj


class ChannelDeviceEditForm(ModelForm):
    class Meta:
        model = ChannelDevice
        fields = ('device', 'name', 'phone_number', 'height', 'height_conf', 'latitude', 'longitude')

    def __init__(self, *args, **kwargs):
        super(ChannelDeviceEditForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-full mt-3 p-1 border-gray-900 rounded-md ' \
                                                  'focus:border-indigo-600 focus:ring focus:ring-opacity-40' \
                                                  'focus:ring-indigo-500 border-2 border-black border-slate-500'


class ChannelDeviceVolumeForm(ModelForm):
    class Meta:
        model = ChannelDeviceVolumeTable
        fields = (
            'tens', 'zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine'
        )

    def __init__(self, *args, **kwargs):
        super(ChannelDeviceVolumeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-32 -mt-1 p-1 border-gray-900 rounded-md ' \
                                                  'focus:border-indigo-600 focus:ring focus:ring-opacity-40' \
                                                  'focus:ring-indigo-500 border-2 border-black border-slate-500'
