from django.http import HttpResponse
import requests
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticatedOrReadOnly,
)
from restquiz.models import Quiz
from restquiz.serializers import CategorySerialiser, QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quiz to be viewed or edited.
    """

    queryset = Quiz.objects.prefetch_related("category")
    serializer_class = QuizSerializer
    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly,
        IsAuthenticatedOrReadOnly,
    ]

    @action(methods=["post", "get"], detail=False, url_path="api", url_name="api")
    def get_quiz(self, request, *args, **kwargs):
        if request.data.__contains__("questions_num") or request.GET.__contains__(
            "questions_num"
        ):
            questions_num = (
                int(float(request.data["questions_num"]))
                if request.method == "post"
                else int(float(request.GET["questions_num"]))
            )
            query = self.queryset.order_by("-id")[:questions_num]
            tmp = QuizSerializer(query, many=True)
            tmp = tmp.data
            response = JSONRenderer().render(tmp)
            data = requests.api.get(
                f"https://jservice.io/api/random?count={questions_num}"
            ).json()
            for item in data:
                cat = CategorySerialiser(data=item["category"])
                quiz = QuizSerializer(data=item)
                if cat.is_valid() and quiz.is_valid():
                    cat.save()
                    answer = quiz.save()
                    if not answer:
                        request.data["questions_num"] = 1
                        self.get_quiz(request=request)
                else:
                    request.data["questions_num"] = 1
                    self.get_quiz(request=request)
            return HttpResponse(content=response, content_type="application/json")
        return HttpResponse()
