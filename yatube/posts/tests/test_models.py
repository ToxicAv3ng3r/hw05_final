from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""

        post = PostModelTest.post
        expected = post.text[:settings.SYMBOLS_IN_STR]
        self.assertEqual(expected, str(post))
        group = PostModelTest.group
        expected_group = group.title
        self.assertEqual(expected_group, str(group))

    def test_model_verbose_name(self):
        """Проверяем, что у полей модели Post корректные verbose"""
        post = PostModelTest.post
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группа поста'
        }
        for field, expected_values in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_values)

    def test_model_help_text(self):
        """Проверяем, что у полей модели Post корректные help_text"""
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Текст нового поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор поста',
            'group': 'Группа, к которой будет относиться пост'
        }
        for field, expected_values in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_values)
