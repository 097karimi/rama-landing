# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy dependencies file to the working directory
COPY requirements.txt /code/


# Install Python dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the working directory
COPY . /code/

# Run migrations and collect static files (if needed)
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput  # Uncomment if you're serving static files directly from Django

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]