OTUS Homework 3 Сайт "Мой блог"
===========================

# Оглавление

- [Описание](#guide)
- [Домашнее задание](#homework)

# Описание

Без регистрации невозможно посмотреть содержимое блога. Есть возможнолсть зарегистриоваться, требования: имя не меньше 3 символов, пароль не меньше 4.
Без регистрации доступна страница с контактами автора. После входа под своей учеткой можно просматривать как все посты, так и по отдельности.
Для написания постов необходимо создать и зайти под пользователем `admin`.
```
puthon3 start.py
```
и далее следовать указаниям.

Тесты находятся в файле `test_game.py`

# Домашнее задание

Сайт "Мой блог"
Цель: В этой самостоятельной работе тренируем умения: 1. Использовать ORM 2. Создавать простую верстку на html/css/js 3. Использовать Flask 4. Использовать docker
Данное домашнее задание это мини проект "Мой блог" рассчитано на материал следующих занятий:
ORM, SQLAlchemy
Введение в werkzeug; Flask
Знакомство с Front-end частью курса. Основы HTML, CSS, методологии верстки. Немного Bootstrap 4
Werkzeug; Flask + SQLAlchemy. Работа с моделями данных
Связь контейнеров в docker. Сборка проекта на Flask

1. Создать новый проект в репозитории
2. Придумать тему блога. Она может быть любая какая вам более интересна (например экзотические птицы, занятия workout-ом, искусство, ...)
3. С помощью SQLAlchemy создать модели данных для блога, например (Post, User, ...) и все другие, которые вы считаете важными
4. Установить связи между моделями
5. Создать следующие страницы и переходы между ними: главная страница, все посты (они могут быть сразу на главной), 1 пост, контакты.
6. Создать любые другие страницы которые вы считаете нужными
7. В зависимости от выбранной темы создать дизайн для страниц
Можно использовать bootstrap, можно самим написать css, можно использовать любой другой способ
8. Хорошо будет добавить регистрацию и авторизацию пользователя на сайте
9. Можно добавить любой новый полезный функционал
10. Написать небольшой readme как работает система
11. Реализовать запуск проекта в docker
12. Сдать дз в виде ссылки на репозиторий
Критерии оценки: Задание считается выполненным, когда:
На сайте есть минимум 2 страницы (все посты и 1 пост), есть переходы между ними сайт работает без ошибок
10 баллов

Дополнительно:
от 0 до 5 баллов, в зависимости от сложности и качества верстки
Есть авторизация - 2 балла
Есть регистрация - 1 балл
Есть readme - 1 балл
Есть возможность запустить в docker - 1 балл


Итого 10 + 5 + 2 + 1 + 1 + 1 = 20 максимум баллов
