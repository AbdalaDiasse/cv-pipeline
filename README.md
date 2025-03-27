# DeepVisionStream: Scalable DeepStream-Based CV Framework

**DeepVisionStream** is a modular, scalable, and production-ready computer vision framework based on NVIDIA DeepStream. It is designed for edge (Jetson) and server (dGPU) deployments, supporting multi-camera management, real-time inference, analytics modules, Kafka/Redis messaging, API control, and monitoring.

## 🚀 Features

- ✅ Dynamic camera stream add/remove via REST API
- 🎯 Modular analytics: Object Counting, Intrusion Detection, Heatmaps, Classification, Dwell Time, Parking Detection
- ⚙️ DeepStream + TensorRT for GPU-accelerated inference
- 📦 Model version management (local & Triton-ready)
- 🔌 Kafka + Redis output integration
- 🔍 Prometheus + Grafana monitoring
- ☁️ Kubernetes & Docker deployment (Jetson & dGPU ready)

## 📁 Project Structure

```
├── apps/               # Analytics modules (object counting, intrusion, etc.)
├── core/               # Pipeline, camera manager, message broker, model manager
├── api/                # FastAPI backend for control & monitoring
├── configs/            # YAML/JSON configs for cameras, models, zones
├── deploy/             # K8s manifests, docker-compose, Jetson setup
├── monitoring/         # Prometheus, Grafana configs
├── docs/               # Architecture diagrams, setup guides
├── tests/              # Unit/integration tests
└── README.md
```

## 🧪 Prebuilt Applications

| Module              | Description                                          |
|---------------------|------------------------------------------------------|
| Object Counting     | Per-class object count with tracking                |
| Intrusion Detection | Alert on entry into ROIs                            |
| Heatmap             | Generate spatial heatmap from detections            |
| Classification      | Object attributes via secondary models              |
| Dwell Time          | Monitor object time spent in zones                  |
| Parking Detection   | Detect free/occupied parking spots                  |

## ⚙️ Setup

### 1. Clone and install dependencies
```bash
git clone https://github.com/your-org/deepvisionstream.git
cd deepvisionstream
```

### 2. Build Docker images
```bash
docker build -t dvs-api ./api
docker build -t dvs-pipeline ./core
```

### 3. Run locally with Docker Compose
```bash
docker-compose up
```

### 4. Or deploy to Jetson + GPU cluster via K8s
```bash
# example (inside deploy/k8s/)
kubectl apply -f dvs-api.yaml
kubectl apply -f dvs-pipeline.yaml
```

## 🔌 API Usage (FastAPI)

- `POST /cameras/`: Add new camera stream
- `DELETE /cameras/{id}`: Remove stream
- `GET /cameras/`: List active cameras
- `PUT /cameras/{id}/modules`: Update analytics modules
- `GET /health`: Liveness check
- `GET /metrics`: Prometheus metrics

Swagger docs auto-generated at:
```
http://localhost:8000/docs
```

## 🧠 Model Management

- Models stored in `/models/{name}/version.engine`
- Use `PUT /models/` to switch version
- Triton integration optional (future-ready)

## 📊 Monitoring

- Prometheus + Grafana dashboards
- GPU, FPS, event count, stream status

## 🧱 Requirements

- NVIDIA DeepStream SDK 6.x
- Docker & NVIDIA Container Toolkit
- JetPack (Jetson) or CUDA (x86)
- Redis or Kafka for output (optional)

## 🤝 Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/my-feature`)
3. Commit changes
4. Open Pull Request

## 📄 License

MIT License © 2025 Your Company or Org

