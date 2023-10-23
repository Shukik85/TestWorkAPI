Тестовое задание на вакансию python(junior) разработчика

Запуск контейнера:<br>
В командной строке копируем репозиторий вводим:
`md NewDir`
`cd NewDir`
`git clone https://github.com/Shukik85/TestWorkAPI.git`
`cd TestWorkAPI`
`docker compose up --build`
Запустится NGINX сервер в локальной сети
Далее создадим суперпользователя Django
`docker compose exec api python manage.py createsuperuser`
Запустится интерактивная консоль с предложением ввести имя пользователя email(не обязательно) и пароль.

По адресу `http://localhost/` находится панель DjangoRestFramework (DRF)
Пока ДБ пустая, переход по адресу `http://localhost/quiz/` будет выдавать ошибку.
Для заполннения БД сделайте GET запрос указанный ниже

API:
Для обращения к API из браузера нужно ввести в адресной строке `http://localhost/quiz/api/?questions_num=10`

Для обращения из терминала(либо специальной программы) можно делать POST запрос в формате `form`
На примере программы `https://httpie.io/docs/cli/main-features`:

`http -a name:password --form post http://localhost/quiz/api/ questions_num:=10`
Для отправки формы через POST запрос, нужно авторизоваться.
