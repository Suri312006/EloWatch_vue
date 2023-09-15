should be a model that stores user data for each person who access the server

keep it inside the main models?

what would they want to store?

- visited summoners
- etc

I see, you want to allow anyone to access your website without requiring them to sign up or log in, and instead assign them a UUID and an access token to identify and store data associated with them. To achieve this, you can use Django's middleware and session management along with a custom model to store data linked to UUIDs. Here's a high-level approach to implement this:

1. **Create a Custom Model for Anonymous Users:**
    
    Create a model to store data associated with anonymous users. This model should include fields for the UUID and any data you want to store.
    
    pythonCopy code
    
    `from django.db import models  class AnonymousUserData(models.Model):     uuid = models.UUIDField(unique=True)     data = models.JSONField()`
    
2. **Middleware to Assign UUID and Access Token:**
    
    Create a middleware to assign UUIDs and access tokens to anonymous users. This middleware should run for every request and check if the user is anonymous. If they are, generate a UUID and an access token and store them in the session.
    
    pythonCopy code
    ```
```python
    import uuid  
    class AnonymousUserMiddleware:     
	    def __init__(self, get_response):         
		    self.get_response = get_response      
		
		def __call__(self, request):         
			if not request.user.is_authenticated:             
				if 'uuid' not in request.session:  
					request.session['uuid'] = str(uuid.uuid4())  # Assign a UUID 
					request.session['access_token'] = generate_access_token()  # Implement your access token generation logic            
				 else:                 # If UUID and access token already exist in session, retrieve them                 
					 uuid = request.session['uuid']                 
					 access_token = request.session['access_token']             
					 request.anonymous_uuid = uuid  # Attach UUID and access token to the request object          
					 response = self.get_response(request)         
					 return response

```

3. **Use the Middleware:**
    
    Add the `AnonymousUserMiddleware` to your Django middleware settings in `settings.py`:
    
    pythonCopy code
    
    `MIDDLEWARE = [     # ...     'yourapp.middleware.AnonymousUserMiddleware',     # ... ]`
    
4. **Store Data Linked to UUID:**
    
    In your views, when anonymous users interact with your website, you can access the UUID and access token from the request object and use them to store and retrieve data in your `AnonymousUserData` model.
    
    ```python

from django.shortcuts import render 
from yourapp.models import AnonymousUserData  
def some_view(request):     # Access the UUID and access token     
	uuid = request.anonymous_uuid     
	access_token = request.session['access_token']      # Store or retrieve data linked to the UUID data, 
	created = AnonymousUserData.objects.get_or_create(uuid=uuid)     # ...      
	return render(request, 'your_template.html', {'data': data})`
    ```

With this approach, anonymous users can access your website without signing up or logging in. Each user is assigned a UUID and an access token, and you can use these identifiers to store and retrieve data associated with them in your `AnonymousUserData` model.


The approach I provided should work for allowing anonymous users to access your website, assigning them a UUID and an access token, and storing data associated with their UUID in your database. However, it's essential to implement the details correctly and test thoroughly to ensure it functions as intended in your specific Django project.

Here are some additional considerations and suggestions:

1. **Access Token Generation**: In the middleware, I mentioned using `generate_access_token()` to create access tokens. You should implement this function according to your security requirements. It should generate secure and unique access tokens for each anonymous user.
    
2. **Data Storage**: Make sure that the `AnonymousUserData` model includes the necessary fields to store the data you want to associate with each UUID. You may need to customize this model further based on your specific data requirements.
    
3. **Session Configuration**: Ensure that your Django project's session settings (in `settings.py`) are configured correctly to use database-backed sessions if you want to store session data in the database. Here's an example session configuration:
    
    pythonCopy code
    
    `SESSION_ENGINE = "django.contrib.sessions.backends.db" SESSION_COOKIE_NAME = "your_session_cookie_name"`
    
4. **Testing**: Thoroughly test your implementation to verify that UUIDs and access tokens are assigned correctly, data is stored and retrieved as expected, and the overall functionality meets your requirements.
    
5. **Security**: Keep in mind that anonymous users will be accessing your website without authentication. Ensure that you do not expose sensitive information or functionality to anonymous users inadvertently. Implement any necessary security measures to protect your site and data.
    
6. **Scalability**: Consider the scalability of this approach. If your website receives a high volume of traffic from anonymous users, you may need to optimize your database and session management for performance.
    

Remember that this approach provides a way for anonymous users to access your website and store data associated with them, but it may not be suitable for all use cases. You should assess your project's specific requirements and security considerations before implementing it.