# GeoPulse :earth_americas:

GeoPulse is an open-source project aimed at helping test geographic load balancing across different cloud platforms. By deploying GeoPulse in your AWS and Azure regions, you can quickly check which region you're accessing from any location, making it an excellent tool for debugging issues with geographically distributed systems.

Currently, GeoPulse supports AWS and Azure platforms.

## Getting Started :rocket:

### Prerequisites

To get started with GeoPulse, you'll need:

- Docker
- AWS or Azure account

### Deployment

GeoPulse is designed to be deployed in a Docker container. There are Dockerfiles available for both AWS and Azure environments.

1. Build the Docker image:

    AWS:
    ```
    cd aws
    docker build -t geopulse-aws .
    ```
    
    Azure:
    ```
    cd azure
    docker build -t geopulse-azure .
    ```

2. Run the Docker container:

    AWS:
    ```
    docker run -d -p 80:80 geopulse-aws
    ```
    
    Azure:
    ```
    docker run -d -p 80:80 geopulse-azure
    ```

Open a web browser and navigate to the public IP address or DNS of the instance. You should see a page displaying the region, availability zone, and cloud provider.

## Contributing :handshake:

Contributions are always welcome! Whether you're fixing bugs, improving the documentation, or proposing new features, your contributions are appreciated. Before contributing, please read our [Contributing Guidelines](LINK-TO-YOUR-CONTRIBUTING-GUIDELINES).

## License :balance_scale:

GeoPulse is licensed under the [MIT License](LICENSE).
# GeoPulse
