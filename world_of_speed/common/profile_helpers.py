from world_of_speed.profiles.models import Profile


def get_profile():
    return Profile.objects.first()