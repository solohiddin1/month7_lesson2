from django.shortcuts import render, get_object_or_404,get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Actor
from rest_framework import status
from .seializers import MovieSerializer,ActorSerializer

# Create your views here.

class MovieView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):    
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):

    def get(self,request,pk):
        movie = get_object_or_404(Movie,pk=pk)
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        movie = get_object_or_404(Movie,pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        movie = get_object_or_404(Movie,pk=pk)
        serializer = MovieSerializer(movie,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movie = get_object_or_404(Movie,pk=pk)
        if movie:
            movie.delete()
            return Response(data={"boldi":"o'chdi"},status=status.HTTP_200_OK)
        return Response(data={"brat":"yogu bunaqa kino"},status=status.HTTP_404_NOT_FOUND)

class MovieYear(APIView):
    def get(self,request,pk=None):
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        if pk:
            movies = get_list_or_404(Movie,year=pk)
        elif start and end:
            movies = Movie.objects.filter(year__range=(start,end))
        else:
            movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class MovieFromBody(APIView):
    def post(self,request):
        start = request.data["start"]
        end = request.data["end"]
        
        movies = Movie.objects.filter(year__range=(start,end))
        serializer = MovieSerializer(movies,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


# ---------------------------------------------------------------------


class ActorView(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):    
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ActorDetailView(APIView):

    def get(self,request,pk):
        actors = get_object_or_404(Actor,pk=pk)
        serializer = ActorSerializer(actors)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        actors = get_object_or_404(Actor,pk=pk)
        serializer = ActorSerializer(actors,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        actors = get_object_or_404(Actor,pk=pk)
        serializer = ActorSerializer(actors,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"Aha":"Hop"},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        actors = get_object_or_404(Actor,pk=pk)
        if actors:
            actors.delete()
            return Response(data={"boldi":"o'chdi"},status=status.HTTP_200_OK)
        return Response(data={"brat":"yogu bunaqa kino"},status=status.HTTP_404_NOT_FOUND)

# class ActorYear(APIView):
#     def get(self,request,pk=None):
#         start = request.query_params.get("start")
#         end = request.query_params.get("end")
#         if pk:
#             actors = get_list_or_404(Actor,year=pk)
#         elif start and end:
#             actors = Actor.objects.filter(year__range=(start,end))
#         else:
#             actors = Actor.objects.all()
#         serializer = ActorSerializer(actors,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)