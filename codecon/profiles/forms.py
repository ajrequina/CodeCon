from django import forms

from profiles.models import Profile


class ProfilePhotoForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_photo', 'owner', )


class CoverPhotoForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('cover_photo', 'owner', )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_photo', 'cover_photo', 'owner', )
