from django.contrib import admin
from .models import Profile, Address, Social, Resume, Education, Work, Skill, Interest, Portfolio, Project, Testimonial

# Register your models here.


class ProfileDependentModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Limit Objects to those that belong to the request's user."""
        qs = super(ProfileDependentModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(profile__user=request.user)


class ResumeDependentModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Limit Objects to those that belong to the request's user."""
        qs = super(ResumeDependentModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(resume__profile__user=request.user)


class PortfolioDependentModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Limit Objects to those that belong to the request's user."""
        qs = super(PortfolioDependentModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(portfolio__profile__user=request.user)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Only show single profile that belong to the request's user."""
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(user=request.user)


@admin.register(Address)
class AddressAdmin(ProfileDependentModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(ProfileDependentModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(ProfileDependentModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(ResumeDependentModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(ResumeDependentModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(ResumeDependentModelAdmin):
    pass


@admin.register(Interest)
class InterestAdmin(ResumeDependentModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(ProfileDependentModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(PortfolioDependentModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(ProfileDependentModelAdmin):
    pass
