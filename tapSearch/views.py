from django.shortcuts import render
from django.http import HttpResponse
from tapSearch.search import Database, InvertedIndex
import json


def index(request):

    return render(request, "tapSearch/index.html")


def highlight_term(id, term, text):
    """
    Represents the format in which output will be sent in response
    :param id:
    :param term:
    :param text:
    :return:
    """
    replaced_text = text.replace(term, "*** {term} ***".format(term=term))
    return f"Your word is present in paragraph {id}: {replaced_text}"

def data(request):
    """
    :param request:
    :return:

    Accept AJAX Request and returns where the word is present in the document.
    """
    if request.method == "POST":
        text_data = request.POST['text']
        query = request.POST['query']

        # splitting the paragraphs and assigning ids
        paragraphs = text_data.split('\n\n')
        contexts = list()

        for i in range(len(paragraphs)):
            temp = {
                "id" : i+1,
                "text" : paragraphs[i].lower()
            }
            contexts.append(temp)

        db = Database()
        index = InvertedIndex(db)

        for context in contexts:
            index.index_document(context)

        search_term = query.lower()
        result = index.lookup_query(search_term)
        answer = list()

        # append the results in a list
        for term in result.keys():
            for appearance in result[term]:
                document = db.get(appearance.docId)
                answer.append(highlight_term(appearance.docId, term, document['text']))

        return HttpResponse(json.dumps({'data': answer}), content_type="application/json")


