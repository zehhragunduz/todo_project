from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kullanıcı bilgisi
    title = models.CharField(max_length=200)  # Görev başlığı
    description = models.TextField(blank=True)  # İsteğe bağlı açıklama
    completed = models.BooleanField(default=False)  # Tamamlandı mı?
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi

    def __str__(self):
        return self.title
