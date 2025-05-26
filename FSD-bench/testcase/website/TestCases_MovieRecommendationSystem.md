### Black Box Unit Test Cases  

#### Functionalities 1. User Registration  
- **Step**: Register with a valid username and password.  
  **Expectation**: User account is created successfully, and a confirmation message is displayed.  


#### Functionalities 2. User Login  
- **Step**: Log in with valid credentials (username and password).  
  **Expectation**: User is logged in successfully and redirected to the recommendations page.  


#### Functionalities 3. View Movie Recommendations  
- **Step**: Access the recommendations page after logging in.  
  **Expectation**: The page displays a list of movie recommendations based on user preferences.  
- **Step**: Update user preferences and revisit recommendations.  
  **Expectation**: The recommendations list updates correctly according to the new preferences.  

#### Functionalities 4. Search for Movies  
- **Step**: Search with a valid movie title.  
  **Expectation**: The software displays the correct movie(s) in the results.  
- **Step**: Search with part of a movie title.  
  **Expectation**: The software displays all movies matching the search criteria.  


#### Functionalities 5. View Movie Details  
- **Step**: Select a movie from the recommendations or search results.  
  **Expectation**: The details of the movie (title, description, rating) are displayed correctly.  
 

#### Functionalities 6. Add Movies to Favorites  
- **Step**: Add a movie to the favorites list.  
  **Expectation**: The movie is successfully added to the favorites list.  


#### Functionalities 7. View Favorites List  
- **Step**: Navigate to the favorites list after adding movies.  
  **Expectation**: The favorites list shows all added movies correctly.  


#### Functionalities 8. Remove Movies from Favorites  
- **Step**: Remove a movie from the favorites list.  
  **Expectation**: The movie is successfully removed, and the favorites list updates accordingly.  


#### Functionalities 9. Data Storage and Retrieval  
- **Step**: Verify the structure of the local text files used for storing data.  
  **Expectation**: The files meet the expected format and contain the correct data (e.g., user info, movie details).  
- **Step**: Test the retrieval of movie data from the local text file.  
  **Expectation**: The data is retrieved accurately and matches the displayed information in the app.  
