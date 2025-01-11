# Use the Amazon Linux 2-based Lambda runtime base image
FROM public.ecr.aws/lambda/python:3.9
RUN echo "delete cache:1"
# Copy application files
COPY . ${LAMBDA_TASK_ROOT}
WORKDIR ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Lambda function handler
CMD ["app.lambda_handler"]
