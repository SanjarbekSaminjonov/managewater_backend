from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ChannelDeviceForm, ChannelDeviceEditForm, ChannelDeviceVolumeForm
from .models import ChannelDevice, ChannelMessage, ChannelDeviceVolumeTable


@login_required(login_url='login')
def master_home_page(request):
    channel_devices = ChannelDevice.objects.filter(master=request.user)
    context = {
        'channel_devices': channel_devices
    }
    return render(request, 'channels_master/index.html', context)


@login_required(login_url='login')
def device_detail(request, device_id):
    channel_devices = ChannelDevice.objects.filter(master=request.user)
    selected_device = channel_devices.filter(device_id=device_id).first()
    if selected_device is None:
        return render(request, 'home/404.html')
    context = {
        'selected_device': selected_device,
        'selected_device_volume_table':
            ChannelDeviceVolumeTable.objects.filter(device_id=selected_device.device_id).order_by('tens')
    }
    return render(request, 'channels_master/channel_device_detail.html', context)


@login_required(login_url='login')
def delete_channel_device(request, device_id):
    channel_devices = ChannelDevice.objects.filter(master=request.user)
    selected_device = channel_devices.filter(device_id=device_id).first()
    if selected_device is not None:
        selected_device.delete()
    return redirect('master_dashboard')


@login_required(login_url='login')
def edit_channel_device_data(request, device_id):
    channel_devices = ChannelDevice.objects.filter(master=request.user)
    selected_device = channel_devices.filter(device_id=device_id).first()
    if selected_device is not None:

        if request.method == 'POST':
            form = ChannelDeviceEditForm(data=request.POST, instance=selected_device)
            if form.is_valid():
                form.save()
                return redirect('device_detail', selected_device.device_id)

        form = ChannelDeviceEditForm(instance=selected_device)
    else:
        form = ChannelDeviceEditForm()
    context = {
        'device_id': selected_device.device_id,
        'title': 'Edit channel device',
        'form': form
    }
    return render(request, 'channels_master/add_or_edit_device.html', context)


@login_required(login_url='login')
def add_new_device(request):
    form = ChannelDeviceForm()

    if request.method == 'POST':
        form = ChannelDeviceForm(data=request.POST)

        if form.is_valid():
            form.save(master=request.user)
            return redirect('master_dashboard')

    context = {
        'title': 'Add channel device',
        'form': form
    }

    return render(request, 'channels_master/add_or_edit_device.html', context)


@login_required(login_url='login')
def add_new_row_for_volume_table(request, device_id):
    last_row = ChannelDeviceVolumeTable.objects.filter(device_id=device_id).order_by('tens').last()
    if last_row is None:
        obj = ChannelDeviceVolumeTable.objects.create(device_id=device_id, tens=0)
    else:
        obj = ChannelDeviceVolumeTable.objects.create(device_id=device_id, tens=last_row.tens + 10)
    return redirect('edit_new_row_for_volume_table', obj.id)


@login_required(login_url='login')
def edit_new_row_for_volume_table(request, row_id):
    obj = ChannelDeviceVolumeTable.objects.filter(pk=row_id).first()
    if obj is not None:
        device_id = obj.device_id
        if request.method == 'POST':
            form = ChannelDeviceVolumeForm(data=request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('volume_table', device_id)
        context = {
            'title': 'Edit row',
            'device_id': device_id,
            'form': ChannelDeviceVolumeForm(instance=obj),
            'selected_device_volume_table':
                ChannelDeviceVolumeTable.objects.filter(device_id=device_id).order_by('tens')
        }

        return render(request, 'channels_master/edit_row_volume_table.html', context)

    return redirect('master_dashboard')


@login_required(login_url='login')
def delete_new_row_for_volume_table(request, row_id):
    obj = ChannelDeviceVolumeTable.objects.filter(pk=row_id).first()
    if obj is not None:
        device_id = obj.device_id
        obj.delete()
        return redirect('volume_table', device_id)

    return redirect('master_dashboard')


@login_required(login_url='login')
def volume_table(request, device_id):
    context = {
        'title': 'Device rows',
        'device_id': device_id,
        'selected_device_volume_table':
            ChannelDeviceVolumeTable.objects.filter(device_id=device_id).order_by('tens')
    }

    return render(request, 'channels_master/edit_row_volume_table.html', context)


@login_required(login_url='login')
def last_messages(request, device_id):
    context = {
        'title': 'Device rows',
        'device_id': device_id,
        'selected_device_messages':
            ChannelMessage.objects.filter(device_id=device_id).order_by('-created_at')[:10]
    }

    return render(request, 'channels_master/last_channel_messages.html', context)
