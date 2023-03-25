function deleteBook(bookId) {
    fetch('/delete-book', {
        method: 'POST',
        body: JSON.stringify({ bookId: bookId }),
    }).then((_res) => {
        window.location.href='/';
    });
}

function deleteUser(userId) {
    fetch('/delete-user', {
        method: 'POST',
        body: JSON.stringify({ userId: userId }),
    }).then((_res) => {
        window.location.href='/';
    });
}