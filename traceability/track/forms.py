# D:\Shubham\TRACEABILITY\Traceability_python\traceability\track\forms.py
from django import forms
from .models import TorqueData

class TorqueDataForm(forms.ModelForm):
    class Meta:
        model = TorqueData
        fields = [
            'part_number',
            'date',
            'time',
            'shift',
            'station1_torque1',
            'station1_torque2',
            'station1_torque3',
            'station1_status',
            'station2_torque1',
            'station2_torque2',
            'station2_torque3',
            'station2_status',
            'station3_torque1',
            'station3_torque2',
            'station3_torque3',
            'station3_status',
            'station4_torque1',
            'station4_torque2',
            'station4_torque3',
            'station4_status',
        ]
