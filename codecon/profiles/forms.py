from django import forms

from profiles.models import Profile


class ProfilePhotoForm(forms.ModelForm):
    profile_photo = forms.FileField(required=False)

    class Meta:
        model = Profile
        fields = ('profile_photo',)

    def save(self, commit=True):
        instance = super(ProfilePhotoForm, self).save(commit=commit)

        print(self.cleaned_data)
        if self.cleaned_data["profile_photo"]:
            instance.my_profile.profile_photo = self.cleaned_data["profile_photo"]
            instance.my_profile.save()


class CoverPhotoForm(forms.ModelForm):
    cover_photo = forms.FileField(required=False)

    class Meta:
        model = Profile
        fields = ('cover_photo',)

    def save(self, commit=True):
        instance = super(CoverPhotoForm, self).save(commit=commit)

        print("COVER PHOTO FORM")
        print(self.cleaned_data)
        if self.cleaned_data["cover_photo"]:
            instance.my_profile.cover_photo = self.cleaned_data["cover_photo"]
            instance.my_profile.save()


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_photo', 'cover_photo',)
