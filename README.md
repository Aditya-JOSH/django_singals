First assignment
When we hit the /run-test/ URL after commenting out the signal for comment and user, the log shows:

Creating a post...
Signal received, starting sleep...
Signal processing finished.
Post created successfully.
Time taken to create the post: 5.01 seconds

This indicates that the signal processing is synchronous with the post creation, taking a total of 5.01 seconds.


When we hit the /create-comment/ URL after commenting out the signal for post and user, the log shows:

Main thread: Thread-1 (process_request_thread)
Signal is running in thread: Thread-1 (process_request_thread)

This confirms that the signal is running in the same thread as the request processing, demonstrating synchronous execution.

When we hit the /create-user/ URL after commenting out the signal for comment and post, the log shows:

Signal received, raising exception to test transaction rollback.
Error caught: Testing transaction rollback with signal.
Total users in the database: 14

This shows that the transaction was rolled back due to the signal exception, leaving the user count unchanged at 14.

Second assignment
Second assignment is on master branch.