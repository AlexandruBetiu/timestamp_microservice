from django.http import JsonResponse
from datetime import datetime

def convert_to_utc(request, input_value=None):

    if input_value == None:
        utc_now = datetime.utcnow()
        unix_now = int(utc_now.timestamp()*1000)
        utc_time_now = utc_now.strftime('%a, %d %b %Y %H:%M:%S GMT')
        response_data = {'unix': unix_now, 'utc': utc_time_now}
        return JsonResponse(response_data)
    else:
        try:
        # Try to parse input_value as an integer (Unix timestamp)
            unix_timestamp = int(input_value)
            utc_datetime = datetime.utcfromtimestamp(unix_timestamp/1000)
            utc_time = utc_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')
            response_data = {'unix': unix_timestamp, 'utc': utc_time}
            return JsonResponse(response_data)
        except:
            try:
                # Try to parse input_value as a date string (YYYY-MM-DD)
                date_obj = datetime.strptime(input_value, '%Y-%m-%d')
                unix_timestamp = int(date_obj.timestamp())
                utc_time = date_obj.strftime('%a, %d %b %Y %H:%M:%S GMT')
                response_data = {'unix': unix_timestamp, 'utc': utc_time}
                return JsonResponse(response_data)
            except:
                # If neither parsing succeeds, return an error response
                return JsonResponse({'error': 'Invalid Date'}, status=400)
