from rest_framework.request import Request
from rest_framework import viewsets, status, generics, mixins
from rest_framework.request import Request
from rest_framework.response import Response 
from .models import Blog
from blogs.serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (AllowAny, 
IsAuthenticated,
IsAuthenticatedOrReadOnly,
IsAdminUser
)
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import CurrentUserBlogSerializer
from .permissions import ReadOnly, AuthororReadOnly
from drf_yasg.utils import swagger_auto_schema


# class BlogViewset(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticated]

@api_view(http_method_names = ["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request):
    response = {"message":"Hello World"}

    if request.method == "POST":
        data = request.data
        response = {"message":"Hello World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)
        
    return Response(data = response, status = status.HTTP_200_OK)

   
class BlogListCreateView(generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """
    a view for creating and listing blogs
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        
        serializer.save(author = user)
        return super().perform_create(serializer)

    @swagger_auto_schema(
            operation_summary="List all blogs",
            operation_description="This returns a list of all blogs"
    )
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary="Create a blog",
            operation_description="Creates a blog"
    )
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    
class BlogRetrieveUpdateDeleteView(generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [AuthororReadOnly]


    @swagger_auto_schema(
            operation_summary="Retrieve a blog by id",
            operation_description="This retrieves a blog by its id"
    )
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    @swagger_auto_schema(
            operation_summary="Updates a blog by its id",
            operation_description="This updates a blog by its id"
    )
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    @swagger_auto_schema(
            operation_summary="Deletes a blog by its id",
            operation_description="This deletes a blog by its id"
    )
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(http_method_names = ["GET"])
@permission_classes([IsAuthenticated])
def get_blog_for_current_user(request:Request):
    user = request.user

    serializer = CurrentUserBlogSerializer(instance = user, 
    context =  {"request":request}
    )

    return Response(data= serializer.data, status= status.HTTP_200_OK)



class ListBlogForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get("username") or None

        queryset = Blog.objects.all()

        if username is not None:
            return Blog.objects.filter(author__username = username)
        
        return queryset



    @swagger_auto_schema(
            operation_summary="Lists blogs for a author (user)",
            operation_description="This lists blogs for an author"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)









    # def list(self, request:Request):
    #     queryset = Blog.objects.all()
    #     serializer = BlogSerializer(instance=queryset, many = True)
    #     return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    # def retrieve(self, request:Request, pk = None):
    #     blog = get_object_or_404(Blog, pk = pk)
    #     serializer = BlogSerializer(instance = blog)
    #     return Response(data = serializer.data, status = status.HTTP_200_OK)
        


# from rest_framework.response import Response
# from rest_framework import status, generics, mixins
# from rest_framework.decorators import api_view, APIView
# from .models import Blog
# from .serializers import BlogSerializer
# from django.shortcuts import get_object_or_404



# # blogs = [
# #     {
# #         "id":1,
# #         "title":"Why is it difficult to start cyber security",
# #         "content":"It is only because it is hard"
# #     },
# #     {
# #         "id":2,
# #         "title": "The Importance of Regular Exercise for Mental Health",
# #         "content":"In today's fast-paced world, mental health has become a crucial topic of discussion"
# #     },
# #     {
# #         "id":3,
# #         "title":"5 Delicious and Nutritious Smoothie Recipes for a Healthy Boost",
# #         "content":"Smoothies are a fantastic way to pack a lot of nutrition into a single meal or snack"
# #     },
# # ]
# @api_view(http_method_names = ["GET", "POST"])
# def homepage(request):

#     if request.method == "POST":
#         data = request.data
#         response = {"message":"Hello World", "data":data}
#     return Response(data=response, status=status.HTTP_201_CREATED)

#     response = {"message":"Hello World"}
#     return Response(data = response, status = status.HTTP_200_OK)

# # @api_view(http_method_names=["GET", "POST"])
# # def list_blogs(request:Request):
# #     blogs = Blog.objects.all()

# #     if request.method == "POST":
# #         data = request.data

# #         serializer = BlogSerializer(data = data)

# #         if serializer.is_valid():
# #             serializer.save()

# #             response = {
# #                 "message":"Blog Created",
# #                 "data":serializer.data
# #             }

# #             return Response(data = response, status=status.HTTP_201_CREATED)
        
# #         return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     serializer = BlogSerializer(instance = blogs, many = True)
# #     response = {
# #         "message":"blogs",
# #         "data":serializer.data
# #     }

# #     return Response(data = response, status=status.HTTP_200_OK)

# class BlogListCreateView(generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin
# ):
#     """
#     a view for creating and listing blogs
#     """
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()

#     def get(self, request:Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request:Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



#     # def get(self, request: Request):
#     #     blog = Blog.objects.all()

#     #     serializer = self.serializer_class(instance = blog, many = True)

#     #     return Response(data=serializer.data, status=status.HTTP_200_OK)
#     # def post(self, request: Request, *args, **kwargs):
#     #     data = request.data


#     #     serializer = self.serializer_class(data=data)

#     #     if serializer.is_valid():
#     #         serializer.save()

#     #         response = {
#     #             "message":"Blog created",
#     #             "data":serializer.data
#     #         }
#     #         return Response(data = response, status=status.HTTP_201_CREATED)

#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class BlogRetrieveUpdateDeleteView(generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin

# ):
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()

#     def get(self, request:Request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request:Request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request:Request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     # def get(self, request:Request, blog_id:int):
#     #     blog = get_object_or_404(Blog, pk= blog_id)

#     #     serializer = self.serializer_class(instance=blog)

#     #     return Response(data=serializer.data, status=status.HTTP_200_OK)
#     # def put(self, request:Request, blog_id:int):
#     #     blog = get_object_or_404(Blog, pk= blog_id)

#     #     data = request.data
#     #     serializer = self.serializer_class(instance=blog, data=data)

#     #     if serializer.is_valid():
#     #         serializer.save()

#     #         response = {
#     #             "message":"Blog updated",
#     #             "data":serializer.data
#     #         }

#     #         return Response(data=response, status=status.HTTP_200_OK)
        
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request:Request, blog_id:int):
#     #     blog = get_object_or_404(Blog, pk= blog_id)

#     #     blog.delete()

#     #     return Response(status=status.HTTP_204_NO_CONTENT)

# # @api_view(http_method_names=["GET"])
# # def blog_detail(request:Request, blog_id:int):
# #     blog = get_object_or_404(Blog, pk = blog_id)

# #     serializer = BlogSerializer(instance=blog)

# #     response = {
# #         "message": "Blog",
# #         "data": serializer.data
# #     }

# #     return Response(data = response, status=status.HTTP_200_OK)



# # @api_view(http_method_names=["PUT"])
# # def update_blog(request:Request, blog_id:int):
# #     blog = get_object_or_404(Blog, pk = blog_id)

# #     data = request.data

# #     serializer = BlogSerializer(instance = blog, data = data)

# #     if serializer.is_valid():
# #         serializer.save()

# #         response = {
# #             "message":"Blog updated successfully",
# #             "data":serializer.data
# #         }
# #         return Response(data = response, status=status.HTTP_200_OK)

# #     return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# # @api_view(http_method_names=["DELETE"])
# # def delete_blog(request:Request, blog_id:int):
# #     blog = get_object_or_404(Blog, pk = blog_id)

# #     # blog.delete
# #     return  Response(status=status.HTTP_204_NO_CONTENT)

