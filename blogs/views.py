from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404



# blogs = [
#     {
#         "id":1,
#         "title":"Why is it difficult to start cyber security",
#         "content":"It is only because it is hard"
#     },
#     {
#         "id":2,
#         "title": "The Importance of Regular Exercise for Mental Health",
#         "content":"In today's fast-paced world, mental health has become a crucial topic of discussion"
#     },
#     {
#         "id":3,
#         "title":"5 Delicious and Nutritious Smoothie Recipes for a Healthy Boost",
#         "content":"Smoothies are a fantastic way to pack a lot of nutrition into a single meal or snack"
#     },
# ]
@api_view(http_method_names = ["GET", "POST"])
def homepage(request):

    if request.method == "POST":
        data = request.data
        response = {"message":"Hello World", "data":data}
    return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message":"Hello World"}
    return Response(data = response, status = status.HTTP_200_OK)

# @api_view(http_method_names=["GET", "POST"])
# def list_blogs(request:Request):
#     blogs = Blog.objects.all()

#     if request.method == "POST":
#         data = request.data

#         serializer = BlogSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message":"Blog Created",
#                 "data":serializer.data
#             }

#             return Response(data = response, status=status.HTTP_201_CREATED)
        
#         return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = BlogSerializer(instance = blogs, many = True)
#     response = {
#         "message":"blogs",
#         "data":serializer.data
#     }

#     return Response(data = response, status=status.HTTP_200_OK)

class BlogListCreateView(generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """
    a view for creating and listing blogs
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



    # def get(self, request: Request):
    #     blog = Blog.objects.all()

    #     serializer = self.serializer_class(instance = blog, many = True)

    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    # def post(self, request: Request, *args, **kwargs):
    #     data = request.data


    #     serializer = self.serializer_class(data=data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         response = {
    #             "message":"Blog created",
    #             "data":serializer.data
    #         }
    #         return Response(data = response, status=status.HTTP_201_CREATED)

    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlogRetrieveUpdateDeleteView(generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get(self, request:Request, blog_id:int):
    #     blog = get_object_or_404(Blog, pk= blog_id)

    #     serializer = self.serializer_class(instance=blog)

    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    # def put(self, request:Request, blog_id:int):
    #     blog = get_object_or_404(Blog, pk= blog_id)

    #     data = request.data
    #     serializer = self.serializer_class(instance=blog, data=data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         response = {
    #             "message":"Blog updated",
    #             "data":serializer.data
    #         }

    #         return Response(data=response, status=status.HTTP_200_OK)
        
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request:Request, blog_id:int):
    #     blog = get_object_or_404(Blog, pk= blog_id)

    #     blog.delete()

    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(http_method_names=["GET"])
# def blog_detail(request:Request, blog_id:int):
#     blog = get_object_or_404(Blog, pk = blog_id)

#     serializer = BlogSerializer(instance=blog)

#     response = {
#         "message": "Blog",
#         "data": serializer.data
#     }

#     return Response(data = response, status=status.HTTP_200_OK)



# @api_view(http_method_names=["PUT"])
# def update_blog(request:Request, blog_id:int):
#     blog = get_object_or_404(Blog, pk = blog_id)

#     data = request.data

#     serializer = BlogSerializer(instance = blog, data = data)

#     if serializer.is_valid():
#         serializer.save()

#         response = {
#             "message":"Blog updated successfully",
#             "data":serializer.data
#         }
#         return Response(data = response, status=status.HTTP_200_OK)

#     return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(http_method_names=["DELETE"])
# def delete_blog(request:Request, blog_id:int):
#     blog = get_object_or_404(Blog, pk = blog_id)

#     # blog.delete
#     return  Response(status=status.HTTP_204_NO_CONTENT)

