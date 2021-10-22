from django.db import models


class OrderingMixin(models.Model):

    class Meta:
        abstract = True
        ordering = ['-id']


class Profile(models.Model):
    """My profile info"""
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_url = models.URLField()
    bio = models.TextField()
    contact_message = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    resume_download = models.URLField()

    def __str__(self):
        return self.name


class Social(OrderingMixin, models.Model):
    """Social information"""
    name = models.CharField(max_length=20)
    url = models.URLField()
    class_name = models.CharField(max_length=20)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='social')

    def __str__(self):
        return self.name


class Address(models.Model):
    """Address information"""
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.PositiveIntegerField()
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.city}, {self.state}"


# =================================================================


class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    skillmessage = models.CharField(max_length=200)

    def __str__(self):
        return self.profile.__str__()


class Education(OrderingMixin, models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    graduated = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='education')

    def __str__(self):
        return self.school


class Work(OrderingMixin, models.Model):
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    years = models.CharField(max_length=40)
    description = models.TextField()
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='work')

    def __str__(self):
        return self.company


class Skill(OrderingMixin, models.Model):
    name = models.CharField(max_length=20)
    level = models.PositiveIntegerField()
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='skills')

    def level_percentage(self):
        return f"{str(self.level)}%"

    def __str__(self):
        return f"{self.name} - {self.level_percentage()}"


class Interest(OrderingMixin, models.Model):
    company_name = models.CharField(max_length=20)
    logo_url = models.URLField()
    website_url = models.URLField()
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='interests')

    def __str__(self):
        return self.company_name


# ============ PORTFOLIO ===============


class Portfolio(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.__str__()


class Project(OrderingMixin, models.Model):
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    image_url = models.URLField()
    url = models.URLField()
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


# ============= TESTIMONIAL =================


class Testimonial(OrderingMixin, models.Model):
    text = models.TextField()
    user = models.CharField(max_length=40)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='testimonials')

    def __str__(self):
        return self.user
