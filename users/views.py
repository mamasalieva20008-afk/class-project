
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'users/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = Student.objects.all()
        search = self.request.GET.get('q', '').strip()
        group = self.request.GET.get('group', '').strip()

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(middle_name__icontains=search)
            )

        if group:
            queryset = queryset.filter(group__icontains=group)

        return queryset


class StudentDetailView(DetailView):
    model = Student
    template_name = 'users/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_form.html'
    success_url = reverse_lazy('student-list')
    login_url = '/admin/login/'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_form.html'
    success_url = reverse_lazy('student-list')
    login_url = '/admin/login/'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'users/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    login_url = '/admin/login/'

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import StudentSerializer


class StudentAPIViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('group').all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]