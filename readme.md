Тестовое задание на вакансию python(junior) разработчика

Запуск контейнера:<br>
В командной строке копируем репозиторий вводим:<br>
```
`md NewDir`
`cd NewDir`
`git clone https://github.com/Shukik85/TestWorkAPI.git`
`cd TestWorkAPI`
`docker compose up --build`
```
Запустится NGINX сервер в локальной сети<br>
Далее создадим суперпользователя Django<br>
`docker compose exec api python manage.py createsuperuser`<br>
Запустится интерактивная консоль с предложением ввести имя пользователя email(не обязательно) и пароль.<br>
<br>
По адресу `http://localhost/` находится панель DjangoRestFramework (DRF)<br>
Пока ДБ пустая, переход по адресу `http://localhost/quiz/` будет выдавать ошибку.<br>
Для заполннения БД сделайте GET запрос указанный ниже<br>
<br>
API:<br>
Для обращения к API из браузера нужно ввести в адресной строке `http://localhost/quiz/api/?questions_num=10`<br>
Где `questions_num` имя переменной, которая определяет количество запрашиваемых объектов.<br>
<br>
Для обращения из терминала(либо специальной программы) можно делать POST запрос в формате `form`<br>
На примере программы `https://httpie.io/docs/cli/main-features`:<br>
<br>
`http -a name:password --form post http://localhost/quiz/api/ questions_num:=10`<br>
Для отправки формы через POST запрос, нужно авторизоваться.<br>
