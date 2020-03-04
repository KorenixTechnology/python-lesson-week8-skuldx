import io, sys
import random
import textwrap

try:
    from hw_week8 import hw_week8
except ImportError:
    from hw_week8_solution import hw_week8

class Test:
    def test_function(self, capsys):

        user_input = """\
        r
        p
        s
        q
        """

        expected_output = """\
        ROCK, PAPER, SCISSORS
        0 Wins, 0 Losses, 0 Ties
        Enter your move: (r)ock (p)aper (s)cissors or (q)uit
        ROCK versus...
        ROCK
        It is a tie!
        0 Wins, 0 Losses, 1 Ties
        Enter your move: (r)ock (p)aper (s)cissors or (q)uit
        PAPER versus...
        ROCK
        You win!
        1 Wins, 0 Losses, 1 Ties
        Enter your move: (r)ock (p)aper (s)cissors or (q)uit
        SCISSORS versus...
        ROCK
        You lose!
        1 Wins, 1 Losses, 1 Ties
        Enter your move: (r)ock (p)aper (s)cissors or (q)uit
        """

        random.seed(22)
        sys.stdin = io.StringIO(textwrap.dedent(user_input))
        hw_week8()
        captured = capsys.readouterr()
        assert captured.out == textwrap.dedent(expected_output)

    def setup_method(self):
        self.orig_stdin = sys.stdin

    def teardown_method(self):
        sys.stdin = self.orig_stdin
