from django.shortcuts import render
# api imports
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer, HotelsSerializer
from .models import Todo, Hotel
from rest_framework.views import APIView
# Create your views here.

def home(request):
    return render(request,"home.html")

class TodoVeiw(APIView):
    def get(self, request):
        obj_list = Todo.objects.all()
        serializer = TodoSerializer(obj_list, many=True)
        return Response({'status': 200,
                        'count':obj_list.count(),
                        'message':'data fetch success',
                        'data':serializer.data})
    def post(self, request):
        try :
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                print(data)
                serializer.save()
                return Response({
                'status': 200,
                'message':'post_todo route works properly',
                'data': serializer.data})

            else:
                print(serializer.errors)
                return Response({
                'status': 400,
                'message':'got errors while passing data',
                'data': serializer.errors})
        except Exception as e:
            print(e)
        return Response({'status': 200,'message':'got error'})


    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({'status':300,
                                'message':'uid not found'})
            obj = Todo.objects.get(uid = data.get('uid'))
            serializer = TodoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200,
                        'message':'data patch success',
                        'data':serializer.data})
            else:
                print(serializer.errors)
                return Response({
                'status': 400,
                'message':'got errors while passing data',
                'data': serializer.errors})

        except Exception as e:
            print(e)
            return Response({'status':400,
                                'message':'invalid uid'})

    def update(self, request):
        return Response({"status": 200,
                    "message": "update method from todoview working fine."})

    def delete(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({'status':300,
                                'message':'uid not found'})
            obj = Todo.objects.get(uid = data.get('uid'))
            serializer = TodoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                obj.delete()
                return Response({'status': 200,
                        'message':'data delete success'})
            else:
                print(serializer.errors)
                return Response({
                'status': 400,
                'message':'got errors while passing data',
                'data': serializer.errors})
        except Exception as e:
            print(e)
            return Response({'status':400,
                            'message':'invalid uid'})

# Hotels API View

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db.models import Q
# from django.shortcuts import get_object_or_404
# from .models import Hotel

# from rest_framework.permissions import AllowAny
# from rest_framework.renderers import JSONRenderer

# class HotelsView(APIView):

#     permission_classes = [AllowAny]
#     renderer_classes = [JSONRenderer] # to disable html rendering

#     def get(self, request):
#         obj_list = Hotel.objects.all()

#         # Filtering
#         hotel_id = request.GET.get('id', '').strip()
#         name = request.GET.get('name', '').strip()
#         location = request.GET.get('location', '').strip()
#         price = request.GET.get('price', '').strip()
#         rating = request.GET.get('rating', '').strip()
#         search = request.GET.get('search', '').strip()

#         if hotel_id.isdigit():
#             obj_list = obj_list.filter(id=int(hotel_id))
#         if name:
#             obj_list = obj_list.filter(name__icontains=name)
#         if location:
#             obj_list = obj_list.filter(location__icontains=location)
#         if search:
#             obj_list = obj_list.filter(Q(name__icontains=search) | Q(location__icontains=search))

#         serializer = HotelsSerializer(obj_list, many=True)
#         return Response({
#             'status': status.HTTP_200_OK,
#             'count':obj_list.count(),
#             'message': 'Successfully fetched hotel list',
#             'data': serializer.data
#         }, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = HotelsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Successfully created hotel',
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Validation error',
#             'errors': serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request):
#         hotel_id = request.data.get('id')
#         if not hotel_id:
#             return Response({'message': 'Hotel ID is required for full update'}, status=status.HTTP_400_BAD_REQUEST)

#         hotel = Hotel.objects.filter(id=hotel_id).first()
#         if not hotel:
#             return Response({'message': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = HotelsSerializer(hotel, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'message': 'Hotel fully updated',
#                 'data': serializer.data
#             }, status=status.HTTP_200_OK)
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Validation error',
#             'errors': serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         hotel_id = request.data.get('id')
#         if not hotel_id:
#             return Response({'message': 'Hotel ID is required for partial update'}, status=status.HTTP_400_BAD_REQUEST)

#         hotel = Hotel.objects.filter(id=hotel_id).first()
#         if not hotel:
#             return Response({'message': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = HotelsSerializer(hotel, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'message': 'Hotel partially updated',
#                 'data': serializer.data
#             }, status=status.HTTP_200_OK)
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Validation error',
#             'errors': serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         hotel_id = request.data.get('id')
#         if not hotel_id:
#             return Response({'message': 'Hotel ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

#         hotel = Hotel.objects.filter(id=hotel_id).first()
#         if not hotel:
#             return Response({'message': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

#         hotel.delete()
#         return Response({
#             'status': status.HTTP_204_NO_CONTENT,
#             'message': 'Hotel deleted successfully'
#         }, status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from django.shortcuts import get_object_or_404

# from .models import Hotel
# from .serializer import HotelsSerializer


# # -------------------------------------------------------------------
# # /api/hotels/ → list, filter, paginate, and create hotels
# # -------------------------------------------------------------------

class HotelsView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]  # Force JSON responses only

    def get(self, request):
        """Get list of hotels with filters, pagination, and sorting"""
        obj_list = Hotel.objects.all()

        # --- Query parameters ---
        name = request.GET.get('name', '').strip()
        location = request.GET.get('location', '').strip()
        price = request.GET.get('price', '').strip()
        rating = request.GET.get('rating', '').strip()
        min_rating = request.GET.get('min_rating', '').strip()
        max_rating = request.GET.get('max_rating', '').strip()
        min_price = request.GET.get('min_price', '').strip()
        max_price = request.GET.get('max_price', '').strip()
        search = request.GET.get('search', '').strip()
        limit = request.GET.get('limit', '').strip()
        skip = request.GET.get('skip', '').strip()
        order_by = request.GET.get('order_by', '').strip()

        # --- Apply filters ---
        if name:
            obj_list = obj_list.filter(name__icontains=name)
        if location:
            obj_list = obj_list.filter(location__icontains=location)
        if price:
            try:
                obj_list = obj_list.filter(price=float(price))
            except ValueError:
                pass
        if rating:
            try:
                obj_list = obj_list.filter(rating=float(rating))
            except ValueError:
                pass
        if min_rating:
            try:
                obj_list = obj_list.filter(rating__gte=float(min_rating))
            except ValueError:
                pass
        if max_rating:
            try:
                obj_list = obj_list.filter(rating__lte=float(max_rating))
            except ValueError:
                pass
        if min_price:
            try:
                obj_list = obj_list.filter(price__gte=float(min_price))
            except ValueError:
                pass
        if max_price:
            try:
                obj_list = obj_list.filter(price__lte=float(max_price))
            except ValueError:
                pass
        if search:
            obj_list = obj_list.filter(
                Q(name__icontains=search) | Q(location__icontains=search)
            )
        if order_by:
            obj_list = obj_list.order_by(order_by)

        # --- Pagination ---
        total_count = obj_list.count()
        try:
            skip = int(skip) if skip.isdigit() else 0
            limit = int(limit) if limit.isdigit() else total_count
        except ValueError:
            skip, limit = 0, total_count

        obj_list = obj_list[skip:skip + limit]
        serializer = HotelsSerializer(obj_list, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'count': total_count,
            'returned': len(serializer.data),
            'message': 'Successfully fetched hotel list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)



# -------------------------------------------------------------------
# /api/hotels/<id>/ → get, update, partial update, delete single hotel
# -------------------------------------------------------------------
class HotelDetailView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]

    def get_object(self, id):
        return get_object_or_404(Hotel, id=id)

    def get(self, request, id):
        """Get a single hotel by ID"""
        hotel = self.get_object(id)
        serializer = HotelsSerializer(hotel)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Successfully fetched hotel',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        """Full update of a hotel"""
        hotel = self.get_object(id)
        serializer = HotelsSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Hotel fully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Validation error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """Partial update of a hotel"""
        hotel = self.get_object(id)
        serializer = HotelsSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Hotel partially updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Validation error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete a hotel"""
        hotel = self.get_object(id)
        hotel.delete()
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'message': f'Hotel with ID {id} deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
