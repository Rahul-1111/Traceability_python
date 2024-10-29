from django.contrib import admin
from .models import TorqueData

class TorqueDataAdmin(admin.ModelAdmin):
    # Display specific fields as columns in the admin table
    list_display = (
        'id',  # You can add 'id' to track each record easily
        'date', 'time', 
        'station1_torque1', 'station1_torque2', 'station1_torque3', 'station1_status',
        'station2_torque1', 'station2_torque2', 'station2_torque3', 'station2_status',
        'station3_torque1', 'station3_torque2', 'station3_torque3', 'station3_status',
        'station4_torque1', 'station4_torque2', 'station4_torque3', 'station4_status',
    )
    list_filter = ('date', 'station1_status', 'station2_status', 'station3_status', 'station4_status')  # Add filters

# Register the model and custom admin view
admin.site.register(TorqueData, TorqueDataAdmin)
