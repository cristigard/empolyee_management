from django.shortcuts import render
from .models import Employee, Group, Membership, Files, DeletedEmployee, Role
from .forms import EmployeeForm, GroupForm, MembershipForm, FilesForm, RoleForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import FileResponse
import os


class RoleUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Role 
    template_name = 'emp/role-update.html'
    form_class = RoleForm
    context_object_name = 'role'
    success_url = reverse_lazy('list-role')
    success_message = "Role updated successfully."


class RoleCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Role 
    template_name = 'emp/role-add.html'
    form_class = RoleForm
    success_url = reverse_lazy('list-role')
    success_message = "Role created successfully."


class RoleDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Role 
    template_name = 'emp/role-delete.html'
    context_object_name = 'role'
    success_url = reverse_lazy('list-role')
    success_message = "Role deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class RoleListView(LoginRequiredMixin,ListView):
    model = Role 
    template_name = 'emp/role-list.html'
    context_object_name = 'roles'


class DeletedEmployeeListView(LoginRequiredMixin,ListView):
    model = DeletedEmployee 
    template_name = 'emp/deleted-employees-list.html'
    context_object_name = 'employees'


def download_file(request,pk):
    path = get_object_or_404(Files, pk=pk).file.url
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = BASE_DIR + path
    response = FileResponse(open(file_path, 'rb'))
    return response


def upload_file(request,pk):
    form = FilesForm()
    employee = Employee.objects.get(pk=pk)
    if request.method == "POST":
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            file_name = form.cleaned_data.get('file_name')
            Files.objects.create(file=file, file_name= file_name, employee=employee)
            messages.success(request, f'File {file} uploaded successfully!')
            return render(request, 'emp/upload-file.html',{"form":form, 'employee':employee})
    else:
        form = FilesForm()
    return render(request, 'emp/upload-file.html',{'form':form, 'employee':employee})


class FileDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Files
    template_name = 'emp/delete-file.html'
    context_object_name = 'file'
    success_message = "File deleted successfully."
    
    def get_success_url(self):
        employee_pk = self.get_object().employee.pk
        return reverse_lazy('employee-detail', kwargs={'pk': employee_pk})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class GroupCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Group 
    template_name = 'emp/group-add.html'
    form_class = GroupForm
    success_url = reverse_lazy('list-groups')
    success_message = "Group created successfully."


class GroupListView(LoginRequiredMixin,ListView):
    model = Group 
    template_name = 'emp/group-list.html'
    context_object_name = 'groups'


class GroupUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Group 
    template_name = 'emp/group-update.html'
    form_class = GroupForm
    context_object_name = 'group'
    success_url = reverse_lazy('list-groups')
    success_message = "Group updated successfully."


class GroupDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Group 
    template_name = 'emp/group-delete.html'
    context_object_name = 'group'
    success_url = reverse_lazy('list-groups')
    success_message = "Group deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class MembershipCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Membership
    template_name = 'emp/add-to-group.html'
    form_class = MembershipForm
    success_url = reverse_lazy('list-groups')
    success_message = "Membership created successfully."

	#add user to form before save in db
    def form_valid(self, form):
        form.instance.employee = Employee.objects.get(pk = self.kwargs.get('pk'))
        return super().form_valid(form)
        
    #add extra context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(pk = self.kwargs.get('pk'))
        return context



class MembershipDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Membership 
    template_name = 'emp/membership-delete.html'
    context_object_name = 'membership'
    form_class = MembershipForm
    success_url = reverse_lazy('list-groups')
    success_message = "Membership deleted successfully."
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class EmployeeCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Employee
    template_name = 'emp/employee-add.html'
    form_class = EmployeeForm
    success_message = "Employee created successfully."

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'emp/employee-list.html'
    context_object_name = 'employees'


class EmployeeDetailView(LoginRequiredMixin,DetailView):
    model = Employee
    template_name = 'emp/employee-detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.filter(employee=context['employee'])
        return super().get_context_data(**context)


class EmployeeUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Employee
    template_name = 'emp/employee-update.html'
    context_object_name = 'employee'
    success_message = "Employee was updated successfully."
    form_class = EmployeeForm


class EmployeeDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Employee
    template_name = 'emp/employee-delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')
    success_message = "Employee deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
