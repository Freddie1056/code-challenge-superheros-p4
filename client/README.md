# Superheroes React Client

This is a React frontend application that connects to a Flask backend for managing superheroes, their powers, and their relationships. The app allows users to view a list of heroes, powers, and hero-power associations, fetched from the Flask API.

## Features

- View a list of superheroes.
- View a list of superpowers.
- View the hero-power associations.

## Project Structure

client/
│
├── public/                   # Public static files
├── src/                      # Source code for the React app
│   ├── components/           # Reusable components
│   ├── services/             # API service functions
│   │   └── api.js            # API handling (axios requests)
│   ├── App.js                # Main component rendering heroes, powers, etc.
│   └── index.js              # App entry point
├── .env                      # Environment variables (API URL)
└── package.json              # Project dependencies and scripts



## Technologies Used

- **React**: JavaScript library for building user interfaces.
- **Axios**: Promise-based HTTP client for the browser to make API requests.
- **Flask**: Python web framework for the backend (not part of this repo, but required).

## Requirements

To run this project locally, you'll need:

- Node.js installed
- Flask API running on `http://localhost:5555` (or another URL if you've set up a different server)

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the `client` directory**:

    ```bash
    cd client
    ```

3. **Install dependencies**:

    ```bash
    npm install
    ```

4. **Set up the environment**:

   Create a `.env` file in the `client` directory with the following content:

    ```bash
    REACT_APP_API_URL=http://localhost:5555
    ```

   This ensures that your React app is pointing to the Flask backend.

5. **Start the React app**:

    ```bash
    npm start
    ```

   The React app will run on `http://localhost:3000`. Open this URL in your browser.

## API Setup

This project relies on a Flask API backend that should be running to provide data to the frontend. Ensure that you have the API running locally on `http://localhost:5555`. The API endpoints are:

- `GET /heroes` - Fetches all superheroes.
- `GET /powers` - Fetches all powers.
- `GET /hero_powers` - Fetches the hero-power associations.

If the API is hosted on a different URL, update the `.env` file to point to the correct `REACT_APP_API_URL`.

## Usage

Once the app is running:

1. **Heroes**: You'll see a list of superheroes fetched from the API.
2. **Powers**: A list of superpowers will also be displayed.
3. **Hero Powers**: The relationships between superheroes and their powers will be shown.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

## Future Improvements

- Add more features like creating, updating, or deleting heroes and powers.
- Implement search functionality.
- Add styling using CSS or libraries like Material-UI.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
