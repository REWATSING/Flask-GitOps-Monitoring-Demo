# Flask Observability Demo

This project demonstrates observability for a Flask app using Prometheus and Grafana deployed via Helm and Argo CD.

## Structure

.
├── charts/
│   ├── flask-app/         # Helm chart for Flask
│   ├── prometheus/        # (Use Bitnami chart or kube-prometheus-stack)
│   └── grafana/           # (Bitnami chart or official)
├── manifests/             # Raw YAMLs if needed (ArgoCD App definitions)
├── app/                   # Simple Flask App
│   └── app.py
├── Dockerfile
└── README.md
