from django.db import models
from django.utils import timezone
import random

class GuessNumbers(models.Model):
# 테이블 만들기, 상속받기. model(class) 에 있는 함수같은거 바로 쓰겠다는

    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    num_lottos = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46)) # 1~45 까지의 숫자들이 들어있는 리스트

        for _ in range(0, self.num_lottos): # range(0,5) -> 0 1 2 3 4
            random.shuffle(origin) # 1~45 숫자를 섞기
            guess = origin[:5] # 섞인 상태에서 앞의 6개 추출
            guess.sort()

            self.lottos += str(guess) + '\n' # 줄바꿈기호

        self.update_date = timezone.now()
        self.save()
        # 여기서 save를 해주면 generate save 후엔 save 안 해도 됨

    def __str__(self): # 관리자페이지에서 하나하나행을 보여줄 때 형식 지정
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
        # pk 자동으로 만들어짐
