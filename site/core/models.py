from django.db import models

# 1. Заставка (видео + логотип + название)
class Hero(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='hero_video/')
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return "Заставка сайта"


class MainPageNews(models.Model):
    news = models.ForeignKey("News", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Новость на главной: {self.news.title}"



class HistoryLineMain(models.Model):
    image = models.ImageField("Изображение", upload_to="history_line/")
    description = models.TextField("Описание", blank=True)
    is_active = models.BooleanField("Активная", default=False)  # ← ТОЛЬКО ЭТО!
    
    class Meta:
        verbose_name = "Main history line"
        verbose_name_plural = "Main history line"

    def __str__(self):
        return f"Историческая линия #{self.id}"



# 2. Краткая информация о проекте
class ProjectInfo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ImageField(upload_to='project_info/')
    link_text = models.CharField(max_length=50, default="Команда проекта")

    def __str__(self):
        return "Информация о проекте"


# 3. Новости
class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    excerpt = models.TextField("Краткое описание")
    content = models.TextField("Полный текст", blank=True)
    image = models.ImageField("Изображение", upload_to="news_images/")
    url = models.URLField("Ссылка на новость", blank=True)
    published_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    is_main = models.BooleanField("Главная новость", default=False)

    class Meta:
        ordering = ['-is_main', '-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_main:
            News.objects.filter(is_main=True).exclude(pk=self.pk).update(is_main=False)
        super().save(*args, **kwargs)




# 4. Исторические линии (краткое описание)
class HistoryLine(models.Model):
    title = models.CharField(max_length=200, blank=True)  
    image = models.ImageField(upload_to='history/')
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  

    class Meta:
        ordering = ['order'] 

    def __str__(self):
        return self.title or f"Историческая линия #{self.id}"



# 5. Детальная страница линии
class HistoryDetail(models.Model):
    history = models.OneToOneField(HistoryLine, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='history/photos/')
    quote = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"Описание: {self.history.title}"


# 6. Партнёры


class Partner(models.Model):
    name = models.CharField("Название", max_length=200)
    logo = models.ImageField("Логотип", upload_to="partners/")
    description = models.TextField("Описание", blank=True)
    url = models.URLField("Ссылка", blank=True)

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField("Название", max_length=200)
    logo = models.ImageField("Логотип", upload_to="organizers/")
    description = models.TextField("Описание", blank=True)
    url = models.URLField("Ссылка", blank=True)  

    def __str__(self):
        return self.name




# 7. Команда проекта
class TeamMember(models.Model):
    name = models.CharField("Имя", max_length=200)
    role = models.CharField("Роль", max_length=200)
    position = models.CharField("Должность", max_length=200, blank=True)
    image = models.ImageField("Фото", upload_to='team_images/')
    social_link = models.URLField("Ссылка на соцсеть", blank=True)

    def __str__(self):
        return self.name



# 8. Контакты
class Contacts(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    legal_info = models.TextField()

    def __str__(self):
        return "Контакты проекта"
