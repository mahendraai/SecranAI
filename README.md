# SecranAI

SecranAI is a web application designed to scan and analyze secrets across various cloud platforms, including AWS, Azure, and GCP. It provides a user-friendly interface for managing and visualizing sensitive information.

## Project Structure

```
SecranAI
├── backend
│   └── app
│       ├── main.py               # Entry point of the FastAPI application
│       ├── api
│       │   └── routes.py         # API routes for the application
│       ├── services
│       │   ├── aws.py            # AWS scanning logic
│       │   ├── azure.py          # Azure scanning logic
│       │   ├── gcp.py            # GCP scanning logic
│       │   └── analyzer.py       # Risk scoring engine
│       ├── models
│       │   └── secrets.py        # SQLAlchemy models
│       ├── db
│       │   ├── session.py        # Database session management
│       │   └── schema.sql        # Database schema
├── frontend
│   ├── pages
│   │   ├── index.tsx             # Landing page
│   │   ├── dashboard.tsx         # Secret dashboard
│   │   └── login.tsx             # Authentication login
│   ├── components
│   │   ├── SecretTable.tsx       # Component for displaying secrets
│   │   └── CloudConnect.tsx      # OAuth connection forms
│   ├── utils
│   │   └── api.ts                # Axios API client
│   ├── styles
│   │   └── globals.css           # Global CSS styles
│   ├── public                    # Static assets
│   ├── tailwind.config.js        # Tailwind CSS configuration
│   └── next.config.js            # Next.js configuration
├── docker-compose.yml            # Local development setup
├── .env.example                  # Example environment variables
└── README.md                     # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- Docker (for local development)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/SecranAI.git
   cd SecranAI
   ```

2. Set up the backend:
   - Navigate to the `backend` directory and install the required packages:
     ```
     cd backend
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory and install the required packages:
     ```
     cd frontend
     npm install
     ```

4. Configure environment variables:
   - Copy the `.env.example` file to `.env` and fill in the necessary values.

### Running the Application

- To run the backend:
  ```
  cd backend
  uvicorn app.main:app --reload
  ```

- To run the frontend:
  ```
  cd frontend
  npm run dev
  ```

### Usage

- Access the application at `http://localhost:3000` for the frontend.
- The backend API will be available at `http://localhost:8000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.