from .models import Institution, Country
from rest_framework.serializers import ModelSerializer, CharField


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"

    def create(self, validated_data):
        institution = Institution.objects.create(name=validated_data["name"],
                                                 country=validated_data["country"],
                                                 email=validated_data["email"],
                                                 address=validated_data["address"],
                                                 website=validated_data["website"],
                                                 contact_person_name=validated_data["contact_person_name"],
                                                 contact_person_number=validated_data["contact_person_number"],
                                                 )
        return institution
