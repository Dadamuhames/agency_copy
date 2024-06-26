from custom.views import BasedListView, BaseForm
from service.models import SurveyAnswer, SurveyQuestion
from custom.models import Languages
from django.db import transaction


# question list
class QuestionList(BasedListView):
    model = SurveyQuestion
    template_name = "admin/questions/list.html"
    search_fields = ['question']


# question form
class QuestionForm(BaseForm):
    model = SurveyQuestion
    template_name = "admin/questions/form.html"
    success_url = "question_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['answers_titles'] = None
        answer_ids = []

        instance = self.get_object()

        if instance:
            answers = instance.answers.order_by("order")

            answers_data_titles = {}

            for answer in answers:
                answer_ids.append(answer.id)
                answers_data_titles[str(answer.order)] = answer.answer

            context["answers_titles"] = answers_data_titles
            context["answers_ids"] = enumerate(answer_ids, start=1)

        return context

    def get_field_data(self, field, index):
        data = {}

        for lang in self.langs:
            key = f"{field}[{lang.code}][{index}]"
            data[lang.code] = self.request.POST.get(key, "")

        return data

    def get_answer_data(self, index, question):
        data = {}

        data["answer"] = self.get_field_data("answer", index)
        data['order'] = int(index)
        data["question"] = question

        return data


    @transaction.atomic
    def form_isvalid(self, form):
        super().form_isvalid(form)

        self.image_keys = []
        self.langs = Languages.objects.filter(active=True)
        form.save()

        for index in range(1, 5):
            id = self.request.POST.get(f"id[{index}]", "")
            answer_data = self.get_answer_data(index, form)

            try:
                answer = None

                if id and id.isnumeric():
                    answer = SurveyAnswer.objects.filter(id=int(id)).first()

                if answer != None:
                    for attr, value in answer_data.items():
                        setattr(answer, attr, value)

                else:
                    answer = SurveyAnswer(**answer_data)

                answer.full_clean()
                answer.save()

            except Exception as e:
                error = {"index": index, "error": str(e)}
                print(e)
                raise Exception(error)

        return form
