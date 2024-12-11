from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile

class ProfileList(APIView):
    """
    List all profiles.
    No create view as profile creation is handled by Django signals.
    """

    def get(self, request, *args, **kwargs):
        queryset = Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
        ).order_by('-created_at')

        profiles_data = [
            {
                "id": profile.id,
                "owner": profile.owner.username,
                "bio": profile.bio,
                "location": profile.location,
                "profile_picture": request.build_absolute_uri(profile.profile_picture.url) if profile.profile_picture else None,
                "posts_count": profile.posts_count,
                "created_at": profile.created_at,
                "updated_at": profile.updated_at,
            }
            for profile in queryset
        ]

        return Response(profiles_data)


class ProfileDetail(APIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Profile.objects.annotate(
                posts_count=Count('owner__post', distinct=True),
            ).get(pk=pk)
        except Profile.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        profile = self.get_object(pk)
        if not profile:
            return Response({"error": "Profile not found"}, status=404)

        self.check_object_permissions(request, profile)

        # Format data manually
        profile_data = {
            "id": profile.id,
            "owner": profile.owner.username,
            "bio": profile.bio,
            "location": profile.location,
            "profile_picture": request.build_absolute_uri(profile.profile_picture.url) if profile.profile_picture else None,
            "posts_count": profile.posts_count,
            "created_at": profile.created_at,
            "updated_at": profile.updated_at,
        }
        return Response(profile_data)

    def put(self, request, pk, *args, **kwargs):
        profile = self.get_object(pk)
        if not profile:
            return Response({"error": "Profile not found"}, status=404)

        self.check_object_permissions(request, profile)

        profile.bio = request.data.get("bio", profile.bio)
        profile.location = request.data.get("location", profile.location)
        if "profile_picture" in request.FILES:
            profile.profile_picture = request.FILES["profile_picture"]
        profile.save()

        profile_data = {
            "id": profile.id,
            "owner": profile.owner.username,
            "bio": profile.bio,
            "location": profile.location,
            "profile_picture": request.build_absolute_uri(profile.profile_picture.url) if profile.profile_picture else None,
            "posts_count": profile.posts_count,
            "created_at": profile.created_at,
            "updated_at": profile.updated_at,
        }
        return Response(profile_data)
