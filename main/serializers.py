from rest_framework import serializers
from .models import Profile, Social, Address, Resume, Education, Work, Skill, Interest, Portfolio, Project, Testimonial


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"
        read_onlyfields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        read_onlyfields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        read_onlyfields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
        read_onlyfields = "__all__"


class SkillSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        read_onlyfields = "__all__"


class InterestSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"
        read_onlyfields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_onlyfields = "__all__"


class TestimonialSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"
        read_onlyfields = "__all__"


# =====   =======  =======   =======   =========   =========  ======


class PortfolioSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='portfolio',
    #     lookup_field='pk'
    # )
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"
        read_onlyfields = "__all__"


class ResumeSerialzer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='resume',
    #     lookup_field='pk'
    # )
    education = EducationSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)
    skills = SkillSerialzer(many=True, read_only=True)
    interests = InterestSerialzer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
        read_onlyfields = "__all__"


class ProfileSerialzer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='profile',
    #     lookup_field='pk'
    # )
    social = SocialSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    resume = ResumeSerialzer(read_only=True)
    portfolio = PortfolioSerializer(read_only=True)
    testimonials = TestimonialSerialzer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
        read_onlyfields = "__all__"
