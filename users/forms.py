
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'middle_name',
            'birth_date',
            'gender',
            'phone',
            'address',
            'photo',
            'student_id',
            'group',
            'specialty',
            'course',
            'admission_year',
            'education_form',
            'funding',
            'status',
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        student = super().save(commit=False)
        if not student.pk:
            student.set_unusable_password()
        if commit:
            student.save()
        return student
