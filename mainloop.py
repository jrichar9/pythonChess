import os
import Classes
import pygame
import Board

def include(filename):
    if os.path.exists(filename):
        exec(open(filename).read())


include('Classes.py')

#playerColor = input("Would you like to be black or white chess pieces?")
playerColor = 'black'

if playerColor == 'black':
    pawn1 = Classes.Pawn('black', 'a2', pygame.image.load("images/black_pawn.png"))
    pawn2 = Classes.Pawn('black', 'b2', pygame.image.load("images/black_pawn.png"))
    pawn3 = Classes.Pawn('black', 'c2', pygame.image.load("images/black_pawn.png"))
    pawn4 = Classes.Pawn('black', 'd2', pygame.image.load("images/black_pawn.png"))
    pawn5 = Classes.Pawn('black', 'e2', pygame.image.load("images/black_pawn.png"))
    pawn6 = Classes.Pawn('black', 'f2', pygame.image.load("images/black_pawn.png"))
    pawn7 = Classes.Pawn('black', 'g2', pygame.image.load("images/black_pawn.png"))
    pawn8 = Classes.Pawn('black', 'h2', pygame.image.load("images/black_pawn.png"))
    rook1 = Classes.Rook('black', 'a1', pygame.image.load("images/black_rook.png"))
    rook2 = Classes.Rook('black', 'h1', pygame.image.load("images/black_rook.png"))
    knight1 = Classes.Knight('black', 'b1', pygame.image.load("images/black_knight.png"))
    knight2 = Classes.Knight('black', 'g1', pygame.image.load("images/black_knight.png"))
    bishop1 = Classes.Bishop('black', 'c1', pygame.image.load("images/black_bishop.png"))
    bishop2 = Classes.Bishop('black', 'f1', pygame.image.load("images/black_bishop.png"))
    queen = Classes.Queen('black', 'd1', pygame.image.load("images/black_queen.png"))
    king = Classes.King('black', 'e1', pygame.image.load("images/black_king.png"))
    computerpawn1 = Classes.Pawn('white', 'a7', pygame.image.load("images/white_pawn.png"))
    computerpawn2 = Classes.Pawn('white', 'b7', pygame.image.load("images/white_pawn.png"))
    computerpawn3 = Classes.Pawn('white', 'c7', pygame.image.load("images/white_pawn.png"))
    computerpawn4 = Classes.Pawn('white', 'd7', pygame.image.load("images/white_pawn.png"))
    computerpawn5 = Classes.Pawn('white', 'e7', pygame.image.load("images/white_pawn.png"))
    computerpawn6 = Classes.Pawn('white', 'f7', pygame.image.load("images/white_pawn.png"))
    computerpawn7 = Classes.Pawn('white', 'g7', pygame.image.load("images/white_pawn.png"))
    computerpawn8 = Classes.Pawn('white', 'h7', pygame.image.load("images/white_pawn.png"))
    computerrook1 = Classes.Rook('white', 'a8', pygame.image.load("images/white_rook.png"))
    computerrook2 = Classes.Rook('white', 'h8', pygame.image.load("images/white_rook.png"))
    computerknight1 = Classes.Knight('white', 'b8', pygame.image.load("images/white_knight.png"))
    computerknight2 = Classes.Knight('white',  'g8', pygame.image.load("images/white_knight.png"))
    computerbishop1 = Classes.Bishop('white',  'c8', pygame.image.load("images/white_bishop.png"))
    computerbishop2 = Classes.Bishop('white',  'f8', pygame.image.load("images/white_bishop.png"))
    computerqueen = Classes.Queen('white', 'd8', pygame.image.load("images/white_queen.png"))
    computerking = Classes.King('white', 'e8', pygame.image.load("images/white_king.png"))
else:
    pawn1 = Classes.Pawn('white', 'a2', pygame.image.load("images/white_pawn.png"))
    pawn2 = Classes.Pawn('white', 'b2', pygame.image.load("images/white_pawn.png"))
    pawn3 = Classes.Pawn('white', 'c2', pygame.image.load("images/white_pawn.png"))
    pawn4 = Classes.Pawn('white', 'd2', pygame.image.load("images/white_pawn.png"))
    pawn5 = Classes.Pawn('white', 'e2', pygame.image.load("images/white_pawn.png"))
    pawn6 = Classes.Pawn('white', 'f2', pygame.image.load("images/white_pawn.png"))
    pawn7 = Classes.Pawn('white', 'g2', pygame.image.load("images/white_pawn.png"))
    pawn8 = Classes.Pawn('white', 'h2', pygame.image.load("images/white_pawn.png"))
    rook1 = Classes.Rook('white', 'a1', pygame.image.load("images/white_rook.png"))
    rook2 = Classes.Rook('white', 'h1', pygame.image.load("images/white_rook.png"))
    knight1 = Classes.Knight('white', 'b1', pygame.image.load("images/white_knight.png"))
    knight2 = Classes.Knight('white', 'g1', pygame.image.load("images/white_knight.png"))
    bishop1 = Classes.Bishop('white', 'c1', pygame.image.load("images/white_bishop.png"))
    bishop2 = Classes.Bishop('white', 'f1', pygame.image.load("images/white_bishop.png"))
    queen = Classes.Queen('white', 'd1', pygame.image.load("images/white_queen.png"))
    king = Classes.King('white', 'e1', pygame.image.load("images/white_king.png"))
    computerpawn1 = Classes.Pawn('black', 'a7', pygame.image.load("images/black_pawn.png"))
    computerpawn2 = Classes.Pawn('black', 'b7', pygame.image.load("images/black_pawn.png"))
    computerpawn3 = Classes.Pawn('black', 'c7', pygame.image.load("images/black_pawn.png"))
    computerpawn4 = Classes.Pawn('black', 'd7', pygame.image.load("images/black_pawn.png"))
    computerpawn5 = Classes.Pawn('black', 'e7', pygame.image.load("images/black_pawn.png"))
    computerpawn6 = Classes.Pawn('black', 'f7', pygame.image.load("images/black_pawn.png"))
    computerpawn7 = Classes.Pawn('black', 'g7', pygame.image.load("images/black_pawn.png"))
    computerpawn8 = Classes.Pawn('black', 'h7', pygame.image.load("images/black_pawn.png"))
    computerrook1 = Classes.Rook('black', 'a8', pygame.image.load("images/black_rook.png"))
    computerrook2 = Classes.Rook('black', 'h8', pygame.image.load("images/black_rook.png"))
    computerknight1 = Classes.Knight('black', 'b8', pygame.image.load("images/black_knight.png"))
    computerknight2 = Classes.Knight('black', 'g8', pygame.image.load("images/black_knight.png"))
    computerbishop1 = Classes.Bishop('black', 'c8', pygame.image.load("images/black_bishop.png"))
    computerbishop2 = Classes.Bishop('black', 'f8', pygame.image.load("images/black_bishop.png"))
    computerqueen = Classes.Queen('black', 'd8', pygame.image.load("images/black_queen.png"))
    computerking = Classes.King('black', 'e8', pygame.image.load("images/black_king.png"))

board = [[computerrook1, computerknight1, computerbishop1, computerqueen, computerking,computerbishop2, computerknight2,computerrook2],
        [computerpawn1, computerpawn2, computerpawn3, computerpawn4, computerpawn5, computerpawn6, computerpawn7, computerpawn8],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8],
        [rook1, knight1, bishop1, queen, king, bishop2, knight2, rook2]]
pygame.init()
screen = pygame.display.set_mode((400, 400))
Board.printBoard(board, '', screen)
pygame.display.flip()
# define a variable to control the main loop
running = True
hightlighting = False
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            if hightlighting == True:
                pos = pygame.mouse.get_pos()
                destinationPiece = Board.getClickedPiece(board, pos)
                if destinationPiece and destinationPiece.color != targetPiece.color:
                    targetPiece.pos = destinationPiece.pos
                    ## delete destination piece
                    destinationPiece.color = 'none'
                    Board.printBoard(board, moveList, screen)
                    pygame.display.flip()
                    hightlighting = False
                    board = Board.fixGrid(board)

                if destinationPiece and destinationPiece.color == targetPiece.color:
                    moveList = ''
                    Board.printBoard(board, moveList, screen)
                    pygame.display.flip()
                    hightlighting = False

                else:
                    targetPiece.pos = Board.convertToGrid(pos)
                    moveList = ''
                    Board.printBoard(board, moveList, screen)
                    pygame.display.flip()
                    hightlighting = False
                    board =Board.fixGrid(board)

            else:
                pos = pygame.mouse.get_pos()
                targetPiece = Board.getClickedPiece(board, pos)
                #moveList = targetPiece.moves()
                moveList = ['a1']
                Board.printBoard(board, moveList, screen)
                pygame.display.flip()
                hightlighting = True
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

