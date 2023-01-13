from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
import json
#from .utils import getNote, getNotes, updateNote, deleteNote, createteNote

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(["GET", "POST"])
def getNotes(request):

    if request.method == "GET":
        notes = Note.objects.all().order_by("-updated")
        serializer = NoteSerializer(notes, many=True)
        
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        note = Note.objects.create(body=data["body"])
        serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE', "GET"])
def getNote(request, pk):

    if request.method == "GET":
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response("Note was successfully deleted")



# @api_view(["Get"])
# def getNotes(request):
#     notes = Note.objects.all().order_by("-updated")
#     serializers = NoteSerializer(notes, many=True)
#     return Response(serializers.data)


# @api_view(["GET"])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# @api_view(["POST"])
# def createteNote(request):
#     data = json.loads(request.body)
#     print(data)
#     note = Note.objects.create(body=data["body"])
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT', 'DELETE', "GET"])
# def updateNote(request, pk):
#         data = json.loads(request.body)
#         print(data)
#         note = Note.objects.get(id=pk)
#         serializer = NoteSerializer(instance=note, data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response("Note was successfully deleted")