from .models import StudentModel
from django import forms

class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentModel
		fields = "__all__"
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name.isalpha():
			raise forms.ValidationError("Name shud contain only alphabets") 
		if len(name)< 2:
			raise forms.ValidationError("Name shud contain min two letters")
		return name

	def clean_ms(self):
		image = self.cleaned_data.get('ms', False)
		if image.size > 2 * 1024*1024:
			raise forms.ValidationError("Image file too large(> 2mb)")
		return image
	