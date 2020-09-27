from django.db import models
from django.template.defaultfilters import slugify

from googletrans import Translator
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название категории'
    )
    image = models.ImageField(
        verbose_name='Фото для категории'
    )
    slug = models.SlugField(
        verbose_name='Название категории в ссылке',
        blank=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        trans = Translator()
        result = trans.translate(
            self.title,
            src='ru',
            dest='en'
        )
        self.slug = slugify(result.text)
        super(Category, self).save(*args, **kwargs)


class Recipe (models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название рецепта'
    )
    description = RichTextField(
        config_name='default',
        verbose_name='Описание рецепта'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Категория'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )
    slug = models.SlugField(
        verbose_name='Название рецепта в ссылке',
        blank=True
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.title} ({self.category})'

    def save(self, *args, **kwargs):
        trans = Translator()
        result = trans.translate(
            self.title,
            src='ru',
            dest='en'
        )
        self.slug = slugify(result.text)
        super(Recipe, self).save(*args, **kwargs)


class Section (models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Название секции'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='section',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

    def __str__(self):
        return f'{self.title}'


class Ingredient (models.Model):
    KG_CHOICE = 'kg'
    GR_CHOICE = 'gr'
    LT_CHOICE = 'l'
    ML_CHOICE = 'ml'
    CUP_CHOICE = 'cup'
    TBSP_CHOICE = 'tbsp'
    TSP_CHOICE = 'tsp'
    PC_CHOICE = 'pc'

    MEASURE_CHOICES = (
        (KG_CHOICE, 'кг.'),
        (GR_CHOICE, 'гр.'),
        (LT_CHOICE, 'л.'),
        (ML_CHOICE, 'мл.'),
        (CUP_CHOICE, 'ст.'),
        (TBSP_CHOICE, 'ст. л.'),
        (TSP_CHOICE, 'ч. л.'),
        (PC_CHOICE, 'шт.'),
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Название ингредиента'
    )
    amount = models.FloatField(
        verbose_name='Количество ингредиента'
    )
    measure = models.CharField(
        max_length=50,
        choices=MEASURE_CHOICES,
        default='',
        verbose_name='Мера ингредиента'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='ingredient',
        verbose_name='Секция'
    )
    slug = models.SlugField(
        verbose_name='Название рецепта в ссылке',
        blank=True
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        trans = Translator()
        result = trans.translate(
            self.title,
            src='ru',
            dest='en'
        )
        self.slug = slugify(result.text)
        super(Ingredient, self).save(*args, **kwargs)


class Method (models.Model):
    description = RichTextField(
        config_name='default',
        verbose_name='Шаг'
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Дополнительное фото'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='method',
        verbose_name='Секция'
    )

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'

    def __str__(self):
        return f'{self.description}'
