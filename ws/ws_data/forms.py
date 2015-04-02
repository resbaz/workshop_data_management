from django import forms
from .models import Students, Organisation, Person, Workshop, Helpers, Instructor, Applicants


class StudentsForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = ['workshop', 'person', 'grade', 'organisation', 'career_stage', 'attendance', 'dietary_requirements']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StudentsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StudentsForm, self).is_valid()

    def full_clean(self):
        return super(StudentsForm, self).full_clean()

    def clean_workshop(self):
        workshop = self.cleaned_data.get("workshop", None)
        return workshop

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_grade(self):
        grade = self.cleaned_data.get("grade", None)
        return grade

    def clean_organisation(self):
        organisation = self.cleaned_data.get("organisation", None)
        return organisation

    def clean_career_stage(self):
        career_stage = self.cleaned_data.get("career_stage", None)
        return career_stage

    def clean_attendance(self):
        attendance = self.cleaned_data.get("attendance", None)
        return attendance

    def clean_dietary_requirements(self):
        dietary_requirements = self.cleaned_data.get("dietary_requirements", None)
        return dietary_requirements

    def clean(self):
        return super(StudentsForm, self).clean()

    def validate_unique(self):
        return super(StudentsForm, self).validate_unique()

    def save(self, commit=True):
        return super(StudentsForm, self).save(commit)


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = ['title', 'location', 'department']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(OrganisationForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(OrganisationForm, self).is_valid()

    def full_clean(self):
        return super(OrganisationForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_location(self):
        location = self.cleaned_data.get("location", None)
        return location

    def clean_department(self):
        department = self.cleaned_data.get("department", None)
        return department

    def clean(self):
        return super(OrganisationForm, self).clean()

    def validate_unique(self):
        return super(OrganisationForm, self).validate_unique()

    def save(self, commit=True):
        return super(OrganisationForm, self).save(commit)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'other', 'email', 'dob', 'gender_identity']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PersonForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PersonForm, self).is_valid()

    def full_clean(self):
        return super(PersonForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_other(self):
        other = self.cleaned_data.get("other", None)
        return other

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_dob(self):
        dob = self.cleaned_data.get("dob", None)
        return dob

    def clean_gender_identity(self):
        gender_identity = self.cleaned_data.get("gender_identity", None)
        return gender_identity

    def clean(self):
        return super(PersonForm, self).clean()

    def validate_unique(self):
        return super(PersonForm, self).validate_unique()

    def save(self, commit=True):
        return super(PersonForm, self).save(commit)


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ['title', 'description', 'date_held', 'teaching_hours', 'catering']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(WorkshopForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(WorkshopForm, self).is_valid()

    def full_clean(self):
        return super(WorkshopForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_date_held(self):
        date_held = self.cleaned_data.get("date_held", None)
        return date_held

    def clean_teaching_hours(self):
        teaching_hours = self.cleaned_data.get("teaching_hours", None)
        return teaching_hours

    def clean_catering(self):
        catering = self.cleaned_data.get("catering", None)
        return catering

    def clean(self):
        return super(WorkshopForm, self).clean()

    def validate_unique(self):
        return super(WorkshopForm, self).validate_unique()

    def save(self, commit=True):
        return super(WorkshopForm, self).save(commit)


class HelpersForm(forms.ModelForm):

    class Meta:
        model = Helpers
        fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HelpersForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HelpersForm, self).is_valid()

    def full_clean(self):
        return super(HelpersForm, self).full_clean()

    def clean_workshop(self):
        workshop = self.cleaned_data.get("workshop", None)
        return workshop

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_organisation(self):
        organisation = self.cleaned_data.get("organisation", None)
        return organisation

    def clean_career_stage(self):
        career_stage = self.cleaned_data.get("career_stage", None)
        return career_stage

    def clean_dietary_requirements(self):
        dietary_requirements = self.cleaned_data.get("dietary_requirements", None)
        return dietary_requirements

    def clean(self):
        return super(HelpersForm, self).clean()

    def validate_unique(self):
        return super(HelpersForm, self).validate_unique()

    def save(self, commit=True):
        return super(HelpersForm, self).save(commit)


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['workshop', 'person', 'organisation', 'career_stage', 'dietary_requirements']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(InstructorForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(InstructorForm, self).is_valid()

    def full_clean(self):
        return super(InstructorForm, self).full_clean()

    def clean_workshop(self):
        workshop = self.cleaned_data.get("workshop", None)
        return workshop

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_organisation(self):
        organisation = self.cleaned_data.get("organisation", None)
        return organisation

    def clean_career_stage(self):
        career_stage = self.cleaned_data.get("career_stage", None)
        return career_stage

    def clean_dietary_requirements(self):
        dietary_requirements = self.cleaned_data.get("dietary_requirements", None)
        return dietary_requirements

    def clean(self):
        return super(InstructorForm, self).clean()

    def validate_unique(self):
        return super(InstructorForm, self).validate_unique()

    def save(self, commit=True):
        return super(InstructorForm, self).save(commit)


class ApplicantsForm(forms.ModelForm):

    class Meta:
        model = Applicants
        fields = ['workshop', 'person', 'applicationDate', 'organisation', 'career_stage', 'dietary_requirements']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ApplicantsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ApplicantsForm, self).is_valid()

    def full_clean(self):
        return super(ApplicantsForm, self).full_clean()

    def clean_workshop(self):
        workshop = self.cleaned_data.get("workshop", None)
        return workshop

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_applicationDate(self):
        applicationDate = self.cleaned_data.get("applicationDate", None)
        return applicationDate

    def clean_organisation(self):
        organisation = self.cleaned_data.get("organisation", None)
        return organisation

    def clean_career_stage(self):
        career_stage = self.cleaned_data.get("career_stage", None)
        return career_stage

    def clean_dietary_requirements(self):
        dietary_requirements = self.cleaned_data.get("dietary_requirements", None)
        return dietary_requirements

    def clean(self):
        return super(ApplicantsForm, self).clean()

    def validate_unique(self):
        return super(ApplicantsForm, self).validate_unique()

    def save(self, commit=True):
        return super(ApplicantsForm, self).save(commit)
