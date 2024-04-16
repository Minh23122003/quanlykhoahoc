from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from courses.models import Category, Course, Lesson, User, Tag, Comment, Like
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class MyCourseadminSite(admin.AdminSite):
    site_header = 'Courseapp Online'


    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()


    def stats_view(self, request):
        course_stats = Category.objects.annotate(c=Count('course__id')).values('id', 'name', 'c')
        return TemplateResponse(request, 'admin/stats.html', {
            'course_stats': course_stats
        })


admin_site = MyCourseadminSite(name='CourseApp')


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'created_date', 'name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}' />")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }


admin_site.register(Category)
admin_site.register(Course, MyCourseAdmin)
admin_site.register(Lesson)
admin_site.register(User)
admin_site.register(Tag)
admin_site.register(Comment)
admin_site.register(Like)