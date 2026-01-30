# Complete DevOps Project - Time Printer Application

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Docker](https://img.shields.io/badge/Docker-enabled-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-ready-326CE5)
![License](https://img.shields.io/badge/license-MIT-green)

A simple Flask web application that displays the current time in Nigeria (GMT+1) with an integrated About Me page. This project demonstrates a complete DevOps pipeline implementation using modern cloud-native technologies.

## 🌟 Features

- **Real-time Clock**: Displays current time in West Africa Time (GMT+1)
- **About Me Page**: Professional portfolio section showcasing DevOps skills
- **Responsive Design**: Beautiful gradient UI that works on all devices
- **Containerized**: Fully dockerized application
- **Cloud-Native**: Deployed on Kubernetes with GitOps principles

## 🚀 Live Demo

Access the application:
- **Time Page**: `http://localhost:8080/`
- **About Page**: `http://localhost:8080/about`

## 📋 Prerequisites

- Python 3.9+
- Docker
- Kubernetes (Minikube/Kind/Cloud Provider)
- Helm 3.x
- kubectl
- Terraform (for infrastructure)

## 🛠️ Tech Stack

### Application
- **Backend**: Flask (Python web framework)
- **Timezone**: pytz library for GMT+1 handling
- **Frontend**: HTML5, CSS3 (embedded)

### DevOps Tools
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **GitOps**: ArgoCD
- **CI/CD**: GitHub Actions
- **IaC**: Terraform
- **Package Management**: Helm
- **Container Registry**: Docker Hub

## 📁 Project Structure
```
Complete-DevOps-Project/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container image definition
├── .github/
│   └── workflows/
│       └── pipeline.yaml          # CI/CD pipeline
├── complete-devops-project-time-printer/
│   ├── Chart.yaml                 # Helm chart metadata
│   ├── values.yaml                # Helm values
│   └── templates/
│       ├── deployment.yaml        # K8s deployment
│       ├── service.yaml           # K8s service
│       └── httproute.yaml         # HTTPRoute config
├── terraform-configs/             # Infrastructure as Code
└── README.md                      # This file
```

## 🏃 Quick Start

### Local Development

1. **Clone the repository**
```bash
   git clone https://github.com/cloudlumanex/Complete-DevOps-Project.git
   cd Complete-DevOps-Project
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python app.py
```

4. **Access the app**
   - Open browser: `http://localhost:8080`

### Docker Deployment

1. **Build the image**
```bash
   docker build -t lumanex/complete-devops-project:latest .
```

2. **Run the container**
```bash
   docker run -p 8080:8080 lumanex/complete-devops-project:latest
```

3. **Access the app**
   - Open browser: `http://localhost:8080`

### Kubernetes Deployment

1. **Start Minikube** (if using local cluster)
```bash
   minikube start
```

2. **Deploy using Helm**
```bash
   helm install time-printer ./complete-devops-project-time-printer
```

3. **Port forward to access**
```bash
   kubectl port-forward svc/complete-devops-project-time-printer 8080:80
```

### ArgoCD GitOps Deployment

1. **Install ArgoCD**
```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

2. **Apply the Application manifest**
```bash
   kubectl apply -f argocd-application.yaml
```

3. **Access ArgoCD UI**
```bash
   kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for automated CI/CD:

### Pipeline Stages

1. **Build**: 
   - Checks out code
   - Builds Docker image with short SHA tag
   
2. **Push**: 
   - Authenticates with Docker Hub
   - Pushes image to registry
   
3. **Deploy**: 
   - Updates Helm chart values with new image tag
   - Commits and pushes changes
   - ArgoCD automatically syncs the deployment

### Triggering the Pipeline

Push to main branch:
```bash
git add .
git commit -m "Update application"
git push origin main
```

## 📊 Monitoring

Check application status:
```bash
# View pods
kubectl get pods -n default

# View logs
kubectl logs -f deployment/complete-devops-project-time-printer

# Check ArgoCD sync status
argocd app get complete-devops-project
```

## 🔧 Configuration

### Environment Variables

The application uses the following configuration:
- **Port**: 8080 (configurable in `app.py`)
- **Timezone**: Africa/Lagos (GMT+1)
- **Debug Mode**: Enabled in development

### Helm Values

Customize deployment in `values.yaml`:
```yaml
replicaCount: 1
image:
  repository: lumanex/complete-devops-project
  tag: latest
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
```

## 🧪 Testing

### Local Testing
```bash
# Test the application
curl http://localhost:8080

# Test about page
curl http://localhost:8080/about
```

### Container Testing
```bash
# Test container health
docker ps
docker logs <container-id>
```

### Kubernetes Testing
```bash
# Check deployment
kubectl get deployments

# Check pods
kubectl get pods

# Test service
kubectl port-forward svc/complete-devops-project-time-printer 8080:80
```

## 🐛 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Find process using port 8080
lsof -i :8080
# Kill the process
kill -9 <PID>
```

**ArgoCD sync issues**
```bash
# Force sync
argocd app sync complete-devops-project --force

# Check application health
argocd app get complete-devops-project
```

**Docker build fails**
```bash
# Clean build cache
docker system prune -a
# Rebuild
docker build --no-cache -t lumanex/complete-devops-project:latest .
```

## 📝 Dependencies
```txt
Flask==3.0.0
pytz==2024.1
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Lumanex**
- Email: techlumanex@gmail.com
- GitHub: [@cloudlumanex](https://github.com/cloudlumanex)
- Location: Lagos, Nigeria 🇳🇬

## 🙏 Acknowledgments

- Flask documentation
- Kubernetes community
- ArgoCD project
- DevOps best practices community

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Helm Documentation](https://helm.sh/docs/)
- [Docker Documentation](https://docs.docker.com/)

## 🗺️ Roadmap

- [ ] Add health check endpoint
- [ ] Implement metrics with Prometheus
- [ ] Add logging with ELK stack
- [ ] Implement caching with Redis
- [ ] Add database for storing timestamps
- [ ] Create admin dashboard
- [ ] Add API endpoints
- [ ] Implement authentication

---

**Made with ❤️ by Lumanex in Lagos, Nigeria**