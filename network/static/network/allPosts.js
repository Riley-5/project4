document.addEventListener('DOMContentLoaded', () => {
    loadAllPosts();
});

// Function that gets all posts from database and displays only 10 at a time 
function loadAllPosts() {
    // Get all posts from database with a fetch statement
    fetch('/allPosts')
    .then(response => response.json())
    .then(allPosts => {
        // For each post puts the post into its own div
        allPosts.forEach(allPostToDiv);
    });
}

// Puts each post into its own div
function allPostToDiv(allPost) {
    // Put posts into their own divs
    const indivPostsDiv = document.createElement('div');
    indivPostsDiv.id = '#indiv-posts';
    indivPostsDiv.style.border = 'solid 2px lightgrey';
    indivPostsDiv.style.borderRadius = '3px';
    indivPostsDiv.style.marginLeft = '1vw';
    indivPostsDiv.style.marginRight = '1vw';
    indivPostsDiv.style.padding = '5px';
    var indivPostsContent = `<div id="username">
                                <a id="profile-link" href='profile/${allPost.user}'>${allPost.user}</a>
                            </div> 
                            <div id="content">
                                ${allPost.content}
                            </div> 
                            <div id="date-time">
                                ${allPost.timestamp}
                            </div> 
                            <div id="like-button">
                                <button class="btn btn-primary btn-sm" id="like-button">Like</button>
                                <p id="number-likes">${allPost.like}</p>
                            </div>`;

    indivPostsDiv.innerHTML = indivPostsContent;
    
    // Append indivPostsDiv to the HTML div all-posts
    document.querySelector('#all-posts').append(indivPostsDiv);
}