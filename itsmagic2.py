"""Let's look at some more complicated magic methods.

Our objects can emulate container classes. (Sometimes its easier to
just inherit from a container like dict or list.)

Fill in the implementation below to make the tests pass.

Make game pieces - they just take a name and a point.

>>> p = Piece("Player 1", Point2D(1, 1))

We can make a game grid that holds points.

>>> the_game = Game()
>>> the_game.add_piece(p)
>>> p2 = Piece("Player 2", Point2D(1, 10))
>>> the_game.add_piece(p2)

The game should be able to tell if a point is occupied and be able to
iterate over all the game pieces. You may want to see the __iter__
method and __contains__.

>>> (1, 9) in the_game
True
>>> p2.point.y = 9
>>> (1, 9) in the_game
True
>>> for piece in the_game:
...     print piece
Player1(1, 1)
Player2(1, 10)

If we were implementing an actual game each game piece might perform
an action on each turn by being called. Check out the __call__ documentation!

For now we'll just have our Piece instance print out a message:

>>> for piece in the_game:
...     piece()
Player 1 moves
Player 2 moves

"""
