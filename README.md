# Odoo 16 Membership Management Module (Community Edition)

This project provides a fully functional Membership Management Module for Odoo 16 CE, packaged with a complete Docker-based setup.

## Features

- Member data management (English & Arabic names, first/last name)
- Branch management with many-to-many relationship
- Membership status workflow (draft, approved, blacklist)
- Membership renewal tracking (based on latest Sales Order)
- Role-based access control with two groups:
  - Membership User
  - Membership Manager
- Full Docker deployment for local development

## Docker Deployment

### Prerequisites

- Docker installed on your system
- Docker Compose installed

### Steps to Run
# Clone the repository
git clone https://github.com/roydesignabad/code.git

# Navigate to project folder
cd code

# Build and run containers
docker compose up
# code