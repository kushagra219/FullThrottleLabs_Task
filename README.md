# FullThrottleLabs_Task
Task on Django Rest Framework deployed on Heroku domain https://fullthrottlelabs-task.herokuapp.com/activity/

## Python Libraries Used - 
* Django
* Django Rest Framework
* Gunicorn (deployment)

## Documentation of "activity" app

### activity/models.py - 
* It contains two models User model and ActivityPeriod Model

### activity/serilizers.py - 
* It contains two serializers UserSerializer and ActivityPeriodSerializer

### activity/views.py - 
* It contains UserActivityView generics view which is based on Task.json file given for reference 

### activity/urls.py
* It contains the url for the above view deployed as https://fullthrottlelabs-task.herokuapp.com/activity/

## Reference Links
* https://www.django-rest-framework.org/
