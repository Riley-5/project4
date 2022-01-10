function likePost(post) {
    var postID = post.dataset.postid;
    
    fetch(`/likePost/${postID}`, {
        method: 'PUT',
        body: JSON.stringify({
            like: 1
        })
    })
    .then(response => response.json())
    .then(likes => {
        document.querySelector(`#number-likes${postID}`).innerHTML = likes;
    })
}

