# from rest_framework.response import Response
# from .models import Note
# from .serializers import NoteSerializer
# import json

# def getNotes(request):
#     notes = Note.objects.all().order_by("-updated")
#     serializers = NoteSerializer(notes, many=True)
#     return Response(serializers.data)

# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# def createteNote(request):
#     data = json.loads(request.body)
#     print(data)
#     note = Note.objects.create(body=data["body"])
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# def updateNote(request, pk):
#         data = json.loads(request.body)
#         print(data)
#         note = Note.objects.get(id=pk)
#         serializer = NoteSerializer(instance=note, data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return serializer.data

# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response("Note was successfully deleted")