from django import forms
# 데이터베이스를 채우기 위한 문서 양식을 만들기 위해
from .models import GuessNumbers

class PostForm(forms.ModelForm):
# ModelForm = 데이터베이스
    # 지극한 약속임! 변수도 지켜줘야됨
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text')
        # 테이블 중에 받아내고 싶은 정보
