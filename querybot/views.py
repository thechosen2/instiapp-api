from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets
from querybot.models import Query, UnresolvedQuery
from querybot.serializers import QuerySerializer, UnresolvedQuerySerializer
from roles.helpers import login_required_ajax

class QueryBotViewset(viewsets.ViewSet):

    @classmethod
    # @login_required_ajax
    def search(cls, request):
        """Get Search Results."""
        queryset = Query.objects.all()
        return Response(QuerySerializer(queryset, many=True).data)

    @classmethod
    # @login_required_ajax
    def ask_question(cls, request):
        """New Question Asked."""
        ques = request.data.get('question', '')
        cat = request.data.get('category', '')
        if ques == '':
            return Response({'error': 'Question cannot be blank.'})

        new_q = UnresolvedQuery(question = ques, category = cat)
        new_q.save()
        return Response(UnresolvedQuerySerializer(new_q).data)

    @classmethod
    # @login_required_ajax
    def add_answer(cls, request):
        """New Answer Added."""
        ques = request.data.get('question', '')
        ans = request.data.get('answer', '')
        cat = request.data.get('category', '')
        s_cat = request.data.get('sub_category', '')
        s_s_cat = request.data.get('sub_sub_category', '')

        if '' in [ques, ans, cat]:
            return Response({'error': 'question, answer and category fields are required.'})
        
        new_q = Query(question = ques, answer = ans, category = cat, sub_category = s_cat, sub_sub_category = s_s_cat)
        new_q.save()
        return Response(QuerySerializer(new_q).data)