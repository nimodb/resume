from django.contrib import admin
from django.contrib.auth.models import User
from main.models import (UserProfile, ContactProfile, Testimonial, Media,
                         Portfolio, Blog, Certificate, Skill, SocialMedia,
                         Profession, Education, Experience, Clients, Category)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_get_full_name', 'surname')

    filter_horizontal = ('skills', 'socialMedia')

    def user_get_full_name(self, obj):
        user = User.objects.get(is_superuser=True)
        return user.get_full_name()


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'title', 'is_active')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score', 'is_active')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ion_icon', 'link')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'description', 'is_active')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'year', 'is_active')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'year', 'is_active')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
