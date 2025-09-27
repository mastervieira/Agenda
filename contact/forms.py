from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError

# Create your forms here.

class ContactForm(forms.ModelForm):
    frist_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'calss':'class-a',
                'placeholder':'Insira o nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda',
    )


    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.fields['frist_name'].widget.attrs.update({
        #     'calss':'class-a',
        #     'placeholder':'Insira o nome',
        # })

    class Meta:
        model = Contact
        fields = (
             'frist_name', 'last_name', 'phone',
             'email', 'description', 'category',
             )

    def clean(self):
            # cleaned_data = self.cleaned_data
            cleaned_data = self.cleaned_data
            frist_name = cleaned_data.get('frist_name')
            last_name = cleaned_data.get('last_name')

            # self.add_error(
            #      'frist_name',
            #     ValidationError(
            #         'Mensagem de erro',
            #     )
            # )
            if frist_name == last_name:
                  self.add_error(
                'last_name',
                ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            )

                # msg = ValidationError(
                #     'Primeiro nome não pode ser igual ao segundo',
                #     code='invalid'
                # )
            
            
            # self.add_error(
            #     'frist_name',
            #     ValidationError(
            #         'Mensagem de erro 2',
            #         code='invalid'
            #     )
            # )
            # self.add_error('frist_name', msg)
            # self.add_error('last_name', msg)

            return super().clean()

    def clean_first_name(self):
        frist_name = self.cleaned_data.get('frist_name')

        if frist_name == 'ABC':
            self.add_error(
                'frist_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

            return frist_name

