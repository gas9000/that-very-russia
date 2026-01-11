from django.contrib import admin
from .models import Partner, Organizer, HistoryLine, TeamMember, News, MainPageNews, HistoryLineMain


@admin.register(MainPageNews)
class MainPageNewsAdmin(admin.ModelAdmin):
    list_display = ("news", "order")
    list_editable = ("order",)



@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


@admin.register(HistoryLine)
class HistoryLineAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'position')
    search_fields = ('name', 'role')



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_main')
    list_filter = ('is_main',)
    search_fields = ('title', 'excerpt')



@admin.register(HistoryLineMain)
class HistoryLineMainAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "image", "description")  # ← добавили is_active