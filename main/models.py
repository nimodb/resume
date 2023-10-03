from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


class Skill(models.Model):

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ['-score']

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(null=True, validators=[
        MinValueValidator(0), MaxValueValidator(100),], help_text='Value must be between 0 and 100.')
    image = models.ImageField(upload_to='skills')
    is_key_skill = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    ion_icon = models.CharField(max_length=80, blank=True, null=True)
    link = models.URLField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        blank=True, null=True, upload_to="avatar")
    surname = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    moreBio = RichTextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    socialMedia = models.ManyToManyField(SocialMedia, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'
        ordering = ["-timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="testimonials")
    timestamp = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
    name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateField(blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="certificates")
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.creator


class Profession(models.Model):

    class Meta:
        verbose_name_plural = 'Professions'
        verbose_name = 'Profession'

    title = models.CharField(max_length=80, blank=True, null=True)
    icon = models.ImageField(
        blank=True, null=True, upload_to="professions")
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Education(models.Model):

    class Meta:
        verbose_name_plural = 'Educations'
        verbose_name = 'Education'
        ordering = ['-year']

    title = models.CharField(max_length=80, blank=True, null=True)
    year = models.CharField(max_length=15)
    image = models.ImageField(upload_to="educations")
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Experience(models.Model):

    class Meta:
        verbose_name_plural = 'Experiences'
        verbose_name = 'Experience'
        ordering = ['-year']

    title = models.CharField(max_length=80, blank=True, null=True)
    year = models.CharField(max_length=15)
    image = models.ImageField(upload_to="experience")
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Clients(models.Model):

    class Meta:
        verbose_name_plural = 'Clients'
        verbose_name = 'Client'

    client = models.CharField(max_length=80, blank=True, null=True)
    logo = models.ImageField(upload_to="Clients")
    is_active = models.BooleanField(default=True)
