Tutorial
--------
There are two types of comments, multi-line comments, and single-line comments. Single-line are started with # and multi-line comments are started with =begin and ended with =end.
```ruby
    =begin
    I'm a comment!
    =end
```
Single-line comments can be started after another thing in the same line.
```ruby
    puts "Hi!" #I'm a comment, but Hi! will still be printed to the console.
```


Exercise
--------
Using which way you like better, comment everything out EXCEPT "Don't comment me out!" still needs to be printed out.

Tutorial Code
-------------
puts "Hi!"
puts "Hi!"
puts "Hi!"
puts "Hi!"
puts "Don't comment me out!"
puts "Hi!"
puts "Hi!"

Expected Output
---------------
Don't comment me out!

Solution
--------

=begin
puts "Hi!"
puts "Hi!"
puts "Hi!"
puts "Hi!"
=end
puts "Don't comment me out!"
=begin
puts "Hi!"
puts "Hi!"
=end
