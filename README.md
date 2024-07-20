[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![API](https://img.shields.io/badge/API-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)
[![API Developer](https://img.shields.io/badge/API%20Developer-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)



# Pixela Habit Tracking Script

This Python script uses the Pixela API to interact with a habit-tracking graph. The script includes functionalities to create a user, create a graph, post a new value to the graph, and update an existing value on the graph.

## Technologies and Libraries Used

- **Python**: The primary programming language used to write the script.
- **Requests Library**: A simple and elegant HTTP library for Python, used to make API requests.
- **Datetime Library**: A built-in Python library used to handle date and time operations.

## Pixela API

**Pixela** is a free API that allows you to track your daily activities and visualize them in a graph format.

## Endpoints Used

- **User Creation Endpoint**:
  - `https://pixe.la/v1/users`
  - This endpoint is used to create a new user on Pixela.

- **Graph Creation Endpoint**:
  - `https://pixe.la/v1/users/<username>/graphs`
  - This endpoint is used to create a new graph for the user.

- **Post Value to Graph Endpoint**:
  - `https://pixe.la/v1/users/<username>/graphs/<graphID>`
  - This endpoint is used to post a new value to the graph.

- **Update Value in Graph Endpoint**:
  - `https://pixe.la/v1/users/<username>/graphs/<graphID>/<date>`
  - This endpoint is used to update an existing value in the graph for a specific date.

## Script Breakdown

### Imports and Constants

The script starts by importing the requests library for making HTTP requests and the datetime library for handling date operations. Constants such as `USERNAME`, `TOKEN`, `GRAPH_ID`, and `today` are defined.

### Pixela API Endpoints

The base Pixela endpoint and specific endpoints for graph operations are defined.

### User Parameters

A dictionary containing user parameters like token, username, agreement to terms of service, and age confirmation.

### Headers

Headers containing the user token are defined for authentication.

### Graph Configuration

A dictionary containing the graph configuration, including graph ID, name, unit, type, and color.

### Post New Value to Graph

A dictionary containing the date and quantity for the new value to be posted to the graph. A POST request is made to the Pixela API to post the new value.

### Update Existing Value in Graph

A dictionary containing the new quantity for the value to be updated. A PUT request is made to the Pixela API to update the existing value for the specific date.

### Links 
#### Pixela API - https://pixe.la/

