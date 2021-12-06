document.addEventListener('DOMContentLoaded', () => {
    loadAllPosts();
});

// Function that gets all posts from database and displays only 10 at a time 
function loadAllPosts() {
    // Get all posts from database with a fetch statement
    // TODO

    // Put posts into their own divs
    const indivPostsDiv = document.createElement('div');
    indivPostsDiv.id = '#indiv-posts';
    indivPostsDiv.style.border = 'solid 2px lightgrey';
    indivPostsDiv.style.borderRadius = '3px';
    indivPostsDiv.style.marginLeft = '1vw';
    indivPostsDiv.style.marginRight = '1vw';
    indivPostsDiv.style.padding = '5px';
    var indivPostsContent = `<div id="username">
                                <a href={% url 'profile' %}>Joe</a>
                            </div> 
                            <div id="content">
                                Hi there!
                            </div> 
                            <div id="date-time">
                                March 29, 2020, 11:40 p.m.
                            </div> 
                            <div id="like-button">
                                <button class="btn btn-primary btn-sm" id="like-button">Like</button>
                                <p id="number-likes">0</p>
                            </div>`;
    indivPostsDiv.innerHTML = indivPostsContent;
    
    // Append indivPostsDiv to the HTML div all-posts
    document.querySelector('#all-posts').append(indivPostsDiv);
}