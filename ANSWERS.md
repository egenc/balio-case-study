# Configuration Engine Explanation & Deployment Guide  

## 1. Why the Configuration Engine Was Built This Way  

### Framework & Design Choices  

#### FastAPI:  
- **Async Support**: Handles concurrent requests efficiently.  
- **Automatic Documentation**: Generates Swagger/OpenAPI docs at `/docs`.  
- **Pydantic Validation**: Ensures data integrity via `CustomFieldCreate` and `EmailCadenceCreate` schemas.  

### Database Design  

#### Tables:  
- **CustomField**: Stores HubSpot field configurations (`field_name`, `field_type`, `field_value`).  
- **EmailCadence**: Manages Upso email workflows (`cadence_name`, `timing`, `template`).  
- **Auditability**: Includes `id`, `created_at`, and `updated_at` for tracking changes.  

### API Endpoints  

#### RESTful Design:  
- **`POST /add_custom_field`**: Creates new HubSpot fields.  
- **`PUT /modify_custom_field/{field_id}`**: Updates only `field_name` (per the task’s requirement).  
- **`POST /add_email_cadence`** and **`PUT /modify_email_cadence/{cadence_id}`**: Manage Upso email cadences.  

### Mock Integrations  

#### Simplicity:  
- `mock_hubspot_api_call` and `mock_upso_api_call` simulate third-party API interactions.  
- Focuses on configuration logic without external dependencies.  

### Recommendations for Improvement  

#### Uniqueness Checks:  
```python
# Add this check in /add_custom_field  
existing_field = db.query(CustomField).filter(CustomField.field_name == custom_field.field_name).first()  
if existing_field:  
    raise HTTPException(status_code=400, detail="Field name already exists")  
```

## 2. Deployment Strategy  

### Infrastructure Setup  

#### 1. Runtime  
- Use **Uvicorn** or **Hypercorn** ASGI servers.
  - Uvicorn and Hypercorn are ASGI (Asynchronous Server Gateway Interface) servers.
  - They help the FastAPI app handle multiple requests at the same time (asynchronously).
  - They are fast, lightweight, and optimized for handling API requests efficiently.

#### 2. Dockerization
 :bowtie: I also created a Dockerfile in this repo. We can create an image, push to a registry like ECR. Please check my Medium articles as I step-by-step explained how to do it.Links:


 - https://medium.com/@erdal.genc09/ready-to-go-spark-nlp-environment-in-sagemaker-studio-614055fad6f3
 - https://medium.com/@erdal.genc09/github-action-to-automate-build-push-for-dockerfiles-repository-to-quay-io-docker-registry-9ebbf6007e2

```dockerfile
FROM python:3.9  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY . .  
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  
```

#### 3. Database
I used SQL Alchemy to make it fast. However, PostgreSQL is appropriate for production-ready environments.

```python
import os  
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL", "postgresql://user:password@db:5432/mydb")  
```

#### Production Deployment

##### 1. Cloud Providers:
 - AWS: Deploy to ECS (Elastic Container Service) or EKS (Kubernetes).
 - GCP: Use Cloud Run or GKE.

##### 2. Reverse Proxy:

- Use Nginx for SSL termination and load balancing.

##### 3 .CI/CD Pipeline (GitHub Actions Example):

```yaml
name: Deploy  
on: [push]  
jobs:  
  deploy:  
    runs-on: ubuntu-latest  
    steps:  
      - name: Checkout code  
        uses: actions/checkout@v2  
      - name: Build and push Docker image  
        uses: docker/build-push-action@v2  
        with:  
          context: .  
          push: true  
          tags: myregistry/orchestra-engine:latest  
```

#### Monitoring & Security
##### Observability:

- Integrate Prometheus + Grafana for metrics (latency, error rates).

- Use `prometheus-fastapi-instrumentator` for FastAPI metrics.

##### Security:

- Add OAuth2 with `fastapi.security.OAuth2PasswordBearer`.

- Encrypt secrets using AWS Secrets Manager or HashiCorp Vault.

- Enable HTTPS via Let’s Encrypt.

