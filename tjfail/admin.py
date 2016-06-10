from django.contrib import admin

from tjfail.models import Fail

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Approve selected Fails'


def reject(modeladmin, request, queryset):
    queryset.update(approved=False)
reject.short_description = 'Reject selected Fails'


class FailAdmin(admin.ModelAdmin):
    search_fields = ['body__icontains']
    list_display = ['body', 'favorite_teacher', 'year', 'approved']
    list_filter = ['year', 'approved']
    actions = [approve, reject]

admin.site.register(Fail, FailAdmin)

