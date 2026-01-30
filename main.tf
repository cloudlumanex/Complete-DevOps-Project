terraform{
    required_providers {
      minikube ={
        source = "scott-the-programmer/minikube"
        version = "0.6.0"
      }
    }
}

provider "minikube" {
    # Configuration options
    kubernetes_version = "v1.27.4"
}

resource "minikube_cluster" "minikube_docker" {
  driver = "docker"
  cluster_name = "complete-devops-project"
  addons = [
    "default-storageclass",
    "storage-provisioner",
  ]
}