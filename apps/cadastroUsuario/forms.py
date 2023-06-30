from django import forms

class CadastroForms(forms.Form):
    nome=forms.CharField(
        label='Nome', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    
    cpf=forms.CharField(
        label='CPF', 
        required=True, 
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: 123.456.789-12',
            }
        )
    )

    login=forms.CharField(
        label='Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaos',
            }
        )
    )

    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha',
            }
        ),
    )
