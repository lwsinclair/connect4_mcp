from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from src.connect4 import Connect4
from mcp.server.fastmcp import FastMCP, Context
from dataclasses import dataclass

@dataclass
class GameContext:
    game: Connect4

@asynccontextmanager
async def produce_game(server: FastMCP)-> AsyncIterator[GameContext]:
    game = Connect4()
    yield GameContext(game=game)

# Initialize FastMCP server
mcp = FastMCP("connect4", lifespan=produce_game)

@mcp.tool()
def play_connect4(ctx: Context)->str:
    """
    Starts a game of connect 4, one should be polite and ask who plays first.
    Can also restart game...
    """
    game = ctx.request_context.lifespan_context.game
    game.restart()
    return str(game.board)

@mcp.tool()
def move_connect4(col: int, ctx: Context)->str:
    """
    Plays a move of connect 4 if is legal. This tool is to be used if the assistant wants to play,
    or to play the move of the user, by the assistant.

    Args:
        col: Column to set the move (0 to 6) 7 columns
    """
    game = ctx.request_context.lifespan_context.game
    if game != None:
        win = game.drop_piece(col)
        if not win:
            if game.no_moves():
                return str(game.board)+f"\n No more moves. Game is a DRAW!"
            return str(game.board)
        else:
            return str(game.board)+f"\n Player {game.current_player} WON!"
    else:
        return "Game hasn't started yet. Use better the tool play_connect4"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
