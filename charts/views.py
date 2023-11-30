from django.shortcuts import render

# Create your views here.
# charts/views.py
# charts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChartData
import matplotlib.pyplot as plt
import json
import os

class UploadDataView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            json_data = request.data['json_data']
            chart_data, created = ChartData.objects.get_or_create(json_data=json_data)

            if created or not chart_data.chart_image:
                # Generate and save chart image
                chart_image_path = self.generate_chart(json_data)
                chart_data.chart_image = chart_image_path
                chart_data.save()

            return Response({'chart_image_url': chart_data.chart_image.url}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def generate_chart(self, json_data):
        # Ensure the 'chart_images' directory exists
        image_dir = 'chart_images'
        os.makedirs(image_dir, exist_ok=True)

        # Your code for generating chart using matplotlib or other library
        # Save the chart image and return the path
        image_path = f'{image_dir}/chart.png'
        plt.plot(json_data['x'], json_data['y'])
        plt.savefig(image_path)
        plt.close()
        return image_path
