from django.db import models


class Video(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='제목'
    )
    embed = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='동영상 주소'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일'
    )

    def __str__(self):
        return self.title
